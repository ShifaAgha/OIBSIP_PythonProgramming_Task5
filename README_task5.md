# Chat Application — OIBSIP Python Programming, Task 5

A real-time command-line chat application in Python using socket programming.
Supports multiple users chatting simultaneously through a central server.
No external libraries needed — uses Python's built-in `socket` and `threading`.

## How It Works

- `server.py` acts as the central hub — it receives messages and broadcasts
  them to all connected clients.
- `client.py` is run by each user — it connects to the server, sends messages,
  and displays messages from other users in real time.
- Each client runs two threads: one for sending, one for receiving — so
  messages appear instantly without blocking the user's input.

## How to Run

### Step 1 — Start the server (in one terminal):
```bash
python server.py
```
You'll see:
```
Listening on 127.0.0.1:55555
Waiting for clients to connect...
```

### Step 2 — Open a NEW terminal and start the first client:
```bash
python client.py
```
Enter a nickname when prompted (e.g. `Alice`).

### Step 3 — Open ANOTHER new terminal for the second client:
```bash
python client.py
```
Enter a different nickname (e.g. `Bob`).

Now Alice and Bob can chat with each other in real time!

## Example Session

**Terminal 1 (Server):**
```
[SERVER] Alice joined the chat.
[SERVER] Bob joined the chat.
[Alice] Hello Bob!
[Bob] Hi Alice! How are you?
```

**Terminal 2 (Alice):**
```
You are connected! Start chatting.
You: Hello Bob!
[Bob] Hi Alice! How are you?
You:
```

**Terminal 3 (Bob):**
```
You are connected! Start chatting.
[Alice] Hello Bob!
You: Hi Alice! How are you?
```

## Features

- Multiple clients can join the same chat room
- Real-time message delivery using threads
- Join/leave notifications broadcast to all users
- Type `exit` to leave the chat gracefully
- Handles disconnections and errors without crashing the server

## Key Concepts Used

- **Socket Programming** — `socket.AF_INET` / `socket.SOCK_STREAM` (TCP)
- **Threading** — separate thread per client on server; separate receive thread on client
- **Client-Server Model** — server broadcasts to all, clients send/receive
- **Error Handling** — graceful disconnection handling on both sides

## Project Structure

```
ShifaAgha_Task5/
├── server.py    # run this first
├── client.py    # run in separate terminals for each user
└── README.md    # this file
```

## Author

Shifa Agha — OIBSIP Python Programming Internship  
GitHub: https://github.com/ShifaAgha/OIBSIP
