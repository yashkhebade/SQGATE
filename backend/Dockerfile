FROM golang:1.21-alpine AS builder

WORKDIR /app
# Download Go modules
COPY go.mod ./
RUN go get github.com/gin-gonic/gin github.com/jackc/pgx/v5/pgxpool github.com/redis/go-redis/v9 github.com/gorilla/websocket
RUN go mod tidy

# Copy the source code
COPY . .
# Build
RUN go build -o main .

# Final stage
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/main .

EXPOSE 8080
CMD ["./main"]
