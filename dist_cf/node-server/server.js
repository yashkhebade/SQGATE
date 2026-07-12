const express = require('express');
const { WebSocketServer } = require('ws');
const http = require('http');

const app = express();
const server = http.createServer(app);
const wss = new WebSocketServer({ server, path: '/ws/default' });

// In-memory room state: { projectId: Set(ws) }
const rooms = new Map();

wss.on('connection', (ws) => {
    let currentRoom = 'default';

    if (!rooms.has(currentRoom)) {
        rooms.set(currentRoom, new Set());
    }
    rooms.get(currentRoom).add(ws);

    console.log(`[+] Client connected to room: ${currentRoom}`);

    ws.on('message', (messageAsString) => {
        try {
            const data = JSON.parse(messageAsString);
            
            // Handle project joining
            if (data.type === 'join' && data.projectId) {
                // Leave old room
                rooms.get(currentRoom).delete(ws);
                if (rooms.get(currentRoom).size === 0) {
                    rooms.delete(currentRoom);
                }

                // Join new room
                currentRoom = data.projectId;
                if (!rooms.has(currentRoom)) {
                    rooms.set(currentRoom, new Set());
                }
                rooms.get(currentRoom).add(ws);
                console.log(`[*] Client switched to room: ${currentRoom}`);
                return;
            }

            // Broadcast to all OTHER clients in the same room
            const roomClients = rooms.get(currentRoom);
            if (roomClients) {
                for (const client of roomClients) {
                    if (client !== ws && client.readyState === 1 /* OPEN */) {
                        client.send(messageAsString);
                    }
                }
            }
        } catch (e) {
            console.error('Invalid message format:', e);
        }
    });

    ws.on('close', () => {
        console.log(`[-] Client disconnected from room: ${currentRoom}`);
        if (rooms.has(currentRoom)) {
            rooms.get(currentRoom).delete(ws);
            if (rooms.get(currentRoom).size === 0) {
                rooms.delete(currentRoom);
            }
        }
    });
});

const PORT = 8080;
server.listen(PORT, () => {
    console.log(`Node.js Multiplayer Hub running on http://localhost:${PORT}`);
});
