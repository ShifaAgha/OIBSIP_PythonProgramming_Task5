"""
Chat Application - CLIENT
OIBSIP Python Programming Task 5
----------------------------------
Run server.py FIRST, then run this file in one or more terminal windows.
Each window = one chat user.

Run:
    python client.py
"""

import socket
import threading
import sys

HOST = "127.0.0.1"   # server address (localhost for same machine)
PORT = 55555          # must match server.py


def receive_messages(client):
    """Continuously listen for incoming messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message:
                print(f"\r{message}")           # overwrite current input line
                print("You: ", end="", flush=True)
            else:
                print("\n[CLIENT] Disconnected from server.")
                client.close()
                sys.exit()
        except Exception:
            print("\n[CLIENT] Connection lost.")
            client.close()
            sys.exit()


def send_messages(client, nickname):
    """Read messages from the user and send them to the server."""
    print(f"\nWelcome, {nickname}! Type your message and press Enter.")
    print("Type 'exit' to leave the chat.\n")

    while True:
        try:
            print("You: ", end="", flush=True)
            message = input()

            if message.lower() in ("exit", "quit", "bye"):
                print("[CLIENT] Leaving the chat. Goodbye!")
                client.close()
                sys.exit()

            if message.strip():
                client.send(message.encode("utf-8"))
            # empty messages are silently ignored

        except (EOFError, KeyboardInterrupt):
            print("\n[CLIENT] Disconnected.")
            client.close()
            sys.exit()


def get_nickname():
    """Prompt user for a nickname (non-empty)."""
    while True:
        nickname = input("Enter your nickname: ").strip()
        if nickname:
            return nickname
        print("  Nickname cannot be empty. Please try again.")


def main():
    print("=" * 50)
    print("  Chat Client - OIBSIP Python Task 5")
    print("=" * 50)

    nickname = get_nickname()

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f"\n[ERROR] Could not connect to server at {HOST}:{PORT}")
        print("  Make sure server.py is running first.")
        sys.exit(1)

    print(f"[CLIENT] Connected to server as '{nickname}'.\n")

    # Send nickname to server immediately
    client.send(nickname.encode("utf-8"))

    # Thread to receive messages in background
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()

    # Main thread handles sending
    send_messages(client, nickname)


if __name__ == "__main__":
    main()
