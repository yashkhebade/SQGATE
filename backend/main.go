package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"sync"

	"github.com/gin-gonic/gin"
	"github.com/gorilla/websocket"
	"github.com/jackc/pgx/v5/pgxpool"
	"github.com/redis/go-redis/v9"
)

var (
	db       *pgxpool.Pool
	rdb      *redis.Client
	ctx      = context.Background()
	upgrader = websocket.Upgrader{
		CheckOrigin: func(r *http.Request) bool {
			return true
		},
	}
)

type Hub struct {
	sync.RWMutex
	rooms map[string]map[*websocket.Conn]bool
}

var hub = &Hub{
	rooms: make(map[string]map[*websocket.Conn]bool),
}

func main() {
	initDB()
	initRedis()

	r := gin.Default()

	// CORS Middleware
	r.Use(func(c *gin.Context) {
		c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
		c.Writer.Header().Set("Access-Control-Allow-Headers", "Origin, Content-Type, Authorization")
		if c.Request.Method == "OPTIONS" {
			c.AbortWithStatus(204)
			return
		}
		c.Next()
	})

	r.GET("/health", func(c *gin.Context) {
		c.JSON(200, gin.H{"status": "ok"})
	})

	r.GET("/ws/:projectId", handleWebSocket)

	// Mock endpoints for users and projects
	api := r.Group("/api")
	{
		api.POST("/auth/login", loginUser)
		api.POST("/projects", createProject)
		api.GET("/projects/:id", getProject)
	}

	log.Println("Backend server running on :8080")
	r.Run(":8080")
}

func initDB() {
	dbURL := os.Getenv("DB_URL")
	if dbURL == "" {
		dbURL = "postgres://schemio:schemiopassword@localhost:5432/schemio_db?sslmode=disable"
	}
	var err error
	db, err = pgxpool.New(ctx, dbURL)
	if err != nil {
		log.Printf("Unable to connect to database: %v\n", err)
	} else {
		log.Println("Connected to PostgreSQL")
	}
}

func initRedis() {
	redisURL := os.Getenv("REDIS_URL")
	if redisURL == "" {
		redisURL = "localhost:6379"
	}
	rdb = redis.NewClient(&redis.Options{
		Addr: redisURL,
	})
	if err := rdb.Ping(ctx).Err(); err != nil {
		log.Printf("Unable to connect to Redis: %v\n", err)
	} else {
		log.Println("Connected to Redis")
	}
}

func handleWebSocket(c *gin.Context) {
	projectId := c.Param("projectId")
	conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
	if err != nil {
		log.Println("WebSocket Upgrade Error:", err)
		return
	}

	// Register client to the room
	hub.Lock()
	if hub.rooms[projectId] == nil {
		hub.rooms[projectId] = make(map[*websocket.Conn]bool)
	}
	hub.rooms[projectId][conn] = true
	hub.Unlock()

	defer func() {
		hub.Lock()
		delete(hub.rooms[projectId], conn)
		if len(hub.rooms[projectId]) == 0 {
			delete(hub.rooms[projectId])
		}
		hub.Unlock()
		conn.Close()
	}()

	// Listen for messages and broadcast to other clients in the same room
	for {
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			log.Println("Read error:", err)
			break
		}

		hub.RLock()
		room := hub.rooms[projectId]
		for client := range room {
			if client != conn { // Broadcast to everyone EXCEPT the sender
				err := client.WriteMessage(messageType, p)
				if err != nil {
					log.Println("Write error:", err)
					client.Close()
					delete(room, client)
				}
			}
		}
		hub.RUnlock()
	}
}

func loginUser(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"token": "mock-jwt-token"})
}

func createProject(c *gin.Context) {
	c.JSON(http.StatusCreated, gin.H{"id": 1, "share_code": "X9F2A"})
}

func getProject(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"name": "Untitled Circuit", "data": "{}"})
}
