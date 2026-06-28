# Chat Application — OIBSIP Python Programming, Task 5

A real-time command-line Chat Application built in Python using socket programming. The application follows a client-server architecture, allowing multiple users to exchange messages simultaneously over a local network.

No external libraries are required—it uses Python's built-in `socket` and `threading` modules.

## Features

* Real-time messaging between multiple clients
* Client-server architecture using TCP sockets
* Supports multiple users simultaneously
* Broadcasts join and leave notifications
* Gracefully handles client disconnections
* Allows users to exit the chat using the `exit` command
* Uses multithreading for simultaneous message sending and receiving

## How It Works

* `server.py` acts as the central server that accepts client connections and broadcasts messages.
* `client.py` connects to the server, sends messages, and receives messages from other connected users.
* Each client runs separate threads for sending and receiving messages, ensuring smooth real-time communication.

## How to Run

### Step 1 — Start the Server

```bash
python server.py
```

Expected output:

```text
Listening on 127.0.0.1:55555
Waiting for clients to connect...
```

### Step 2 — Start the First Client

Open a new terminal and run:

```bash
python client.py
```

Enter a nickname when prompted (for example, `Alice`).

### Step 3 — Start Another Client

Open another terminal and run:

```bash
python client.py
```

Enter a different nickname (for example, `Bob`).

You can now exchange messages between both clients in real time.

## Example Session

**Server**

```text
[SERVER] Alice joined the chat.
[SERVER] Bob joined the chat.
[Alice] Hello Bob!
[Bob] Hi Alice! How are you?
```

**Alice**

```text
You are connected! Start chatting.
You: Hello Bob!
[Bob] Hi Alice! How are you?
```

**Bob**

```text
You are connected! Start chatting.
[Alice] Hello Bob!
You: Hi Alice! How are you?
```

## Key Concepts Used

* Socket Programming (`socket`)
* TCP Client-Server Architecture
* Multithreading (`threading`)
* Real-time Communication
* Error Handling
* Network Programming Fundamentals

## Project Structure

```text
ShifaAgha_Task5/
├── server.py      # server program
├── client.py      # client program
└── README.md      # documentation
```

## Author

**Shifa Agha**
OIBSIP Python Programming Internship

GitHub: https://github.com/ShifaAgha/OIBSIP
