import socket
import threading
import sys

# initialize a empty clients list
clients = [] 


# Setup server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP = "localhost" # Server Ip addr for testing
PORT = 12345     # Port number


# Bind the server to IP and PORT
server_socket.bind((IP, PORT))
server_socket.listen(5) # Allows upto 5 connections
print(f"Server started on {IP}: {PORT}")

# GLobal flag to indicate shutdown 
shutdown_flag = False

# Function to broadcast message to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client()


# Function to handle receiving message from clients
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    client_socket.send("Welcome to this chat room! Type exit to leave.".encode('utf-8'))

    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8') #read up to 1024 bytes from the client at a time.
            if message :
                print(f"<{addr}> {message}")
                broadcast(f"<{addr}> {message}", client_socket) #format "<client_address> message"
            if message.lower() == "goodbye!":
                print(f"{addr} has disconnected.")
                remove_client(client_socket)
                client_socket.close()
                break
        except:
            remove_client(client_socket)
            client_socket.close()
            break


# Function to remove disconnected client
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)


# Function  to send message to clients
def server_send_msg():
    global shutdown_flag
    while True:
        message = input() #prompts the server administrator to enter a message. 
        if message.lower() == "exit":
            print("Server is shutting down..")
            shutdown_flag = True # set the shutdown flag
            for client in clients:
                try:
                    client.send("Server is shutting down. Goodbye!".encode('utf-8'))
                    client.close()
                except:
                    continue
            server_socket.close()
            sys.exit() # terminate the server program
        broadcast(f"<Server> {message}", None)



# Function to accept connections from clients in separate thread
def accept_connection():
    global shutdown_flag
    while not shutdown_flag:
        try:
            client_socket, client_addr = server_socket.accept() # waits for client to connect to server then returns two values
            clients.append(client_socket)
            print(f"{client_addr} connected")
            # Start new thread for each client
            thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
            thread.start()
        except OSError:
            break

# Start threads for accepting connections and sending messages
accept_thread = threading.Thread(target=accept_connection)
accept_thread.start()

server_send_msg()




