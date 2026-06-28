"""
Chat Application - SERVER
OIBSIP Python Programming Task 5
----------------------------------
Run this file FIRST, then run client.py in separate terminal windows.
Supports multiple clients chatting in real-time.

Run:
    python server.py
"""

import socket
import threading

HOST = "127.0.0.1"   # localhost
PORT = 55555          # port to listen on

# Store connected clients and their nicknames
clients   = []
nicknames = []


def broadcast(message, sender_conn=None):
    """Send a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except Exception:
                remove_client(client)


def remove_client(client):
    """Cleanly remove a disconnected client."""
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        clients.remove(client)
        nicknames.remove(nickname)
        client.close()
        broadcast(f"[SERVER] {nickname} has left the chat.".encode("utf-8"))
        print(f"[SERVER] {nickname} disconnected.")


def handle_client(client, address):
    """Handle incoming messages from a single client in its own thread."""
    print(f"[SERVER] New connection from {address}")

    # First message from client is always their chosen nickname
    try:
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"[SERVER] {nickname} joined the chat.")
        broadcast(f"[SERVER] {nickname} has joined the chat!".encode("utf-8"), sender_conn=client)
        client.send("[SERVER] You are connected! Start chatting.\n".encode("utf-8"))

        # Listen for messages continuously
        while True:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            full_message = f"[{nickname}] {message}"
            print(full_message)
            broadcast(full_message.encode("utf-8"), sender_conn=client)

    except Exception:
        pass
    finally:
        remove_client(client)


def start_server():
    print("=" * 50)
    print("  Chat Server - OIBSIP Python Task 5")
    print("=" * 50)
    print(f"  Listening on {HOST}:{PORT}")
    print("  Waiting for clients to connect...")
    print("  Press Ctrl+C to stop the server.\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    try:
        while True:
            client, address = server.accept()
            thread = threading.Thread(target=handle_client, args=(client, address))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down...")
    finally:
        server.close()


if __name__ == "__main__":
    start_server()
