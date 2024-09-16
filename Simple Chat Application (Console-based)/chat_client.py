import socket # for building connection (client and server)
import threading # For handling multiple connections
import sys # for system-specific functions  such as exiting the program.

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8') # Receive and print messages from the server
            if message:
                print(message)
            if message.startswith("Server is shutting down.") or message.lower() == "goodbye!":
                print("Connection closed by server.")
                client_socket.close()
                sys.exit()  # Terminate the client program cleanly
        except:
            break  # Exit the loop on any error
          

# Setup client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server details (use the same IP and Port as the server)
IP = "localhost"
PORT = 12345
client_socket.connect((IP, PORT))# Connect to the server

# Start thread to receive messages from server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Allow the client to send messages to the server
try:
    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.send("Goodbye!".encode('utf-8'))
            client_socket.close()
            sys.exit()  # Terminate the client program cleanly
    else:
        client_socket.send(message.encode('utf-8'))
except:
    pass
