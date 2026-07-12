package api

import (
	"encoding/json"
	"net/http"

	"github.com/schemio/backend/db"
)

type Credentials struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

type Project struct {
	ID      int    `json:"id"`
	Name    string `json:"name"`
	OwnerID int    `json:"owner_id"`
}

func LoginHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	
	var creds Credentials
	if err := json.NewDecoder(r.Body).Decode(&creds); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	// In a real app, hash password and verify
	var id int
	err := db.DB.QueryRow("SELECT id FROM users WHERE username = $1 AND password_hash = $2", creds.Username, creds.Password).Scan(&id)
	if err != nil {
		http.Error(w, "Invalid credentials", http.StatusUnauthorized)
		return
	}

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]interface{}{"token": "dummy-jwt-token", "user_id": id})
}

func RegisterHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	
	var creds Credentials
	if err := json.NewDecoder(r.Body).Decode(&creds); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	// In a real app, hash password before storing
	_, err := db.DB.Exec("INSERT INTO users (username, password_hash) VALUES ($1, $2)", creds.Username, creds.Password)
	if err != nil {
		http.Error(w, "Error creating user", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(map[string]string{"message": "User registered successfully"})
}

func ProjectsHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodGet {
		rows, err := db.DB.Query("SELECT id, name, owner_id FROM projects")
		if err != nil {
			http.Error(w, "Error fetching projects", http.StatusInternalServerError)
			return
		}
		defer rows.Close()

		var projects []Project
		for rows.Next() {
			var p Project
			if err := rows.Scan(&p.ID, &p.Name, &p.OwnerID); err != nil {
				continue
			}
			projects = append(projects, p)
		}

		json.NewEncoder(w).Encode(projects)
	} else if r.Method == http.MethodPost {
		var p Project
		if err := json.NewDecoder(r.Body).Decode(&p); err != nil {
			http.Error(w, "Invalid request body", http.StatusBadRequest)
			return
		}

		err := db.DB.QueryRow("INSERT INTO projects (name, owner_id) VALUES ($1, $2) RETURNING id", p.Name, p.OwnerID).Scan(&p.ID)
		if err != nil {
			http.Error(w, "Error creating project", http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusCreated)
		json.NewEncoder(w).Encode(p)
	} else {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}
