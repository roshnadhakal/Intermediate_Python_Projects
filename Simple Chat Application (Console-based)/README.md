# Chat Server and Client
This is a simple chat application built using Python sockets. It allows multiple clients to connect to a server and send messages to each other.

## Requirements
Python 3.12.4 or higher

## Usage
Run the chat_server.py script to start the server. The server will listen on localhost at port 12345.  
Run the chat_client.py script to start a client. The client will connect to the server running on localhost:12345.  
Once connected, you can start sending messages. Type exit to disconnect from the server.  
To shut down the server, type exit in the server console. This will send a shutdown message to all connected clients and terminate the server.  

## Code Explanation
**chat_client.py**
1. The client code imports necessary modules: socket for building the connection, threading for handling multiple connections, and sys for system-specific functions.  
2. The receive_messages function is defined to receive messages from the server in a separate thread.  
3. The client socket is created and connected to the server using the specified IP and port.  
4. A separate thread is started to receive messages from the server using the receive_messages function.  
5. The client enters a loop to allow the user to send messages to the server. Typing exit will send a "Goodbye!" message to the server and terminate the client program.  
   
**chat_server.py**
1. The server code imports necessary modules: socket for building the connection, threading for handling multiple connections, and sys for system-specific functions.  
2. An empty list clients is initialized to store connected clients.  
3. The server socket is created, configured with the necessary options, and bound to the specified IP and port.  
4. The broadcast function is defined to send a message to all connected clients except the sender.  
5. The handle_client function is defined to handle receiving messages from a specific client. It prints the received message, broadcasts it to other clients, and removes the client if they send "Goodbye!" or if an error occurs.  
6. The remove_client function is defined to remove a disconnected client from the clients list.  
7. The server_send_msg function is defined to allow the server administrator to send messages to all connected clients. Typing exit will send a shutdown message to all clients and terminate the server.  
8. The accept_connection function is defined to accept incoming connections from clients in a separate thread. It adds new clients to the clients list and starts a new thread for each client using the handle_client function.  
9. Two separate threads are started: one for accepting connections using accept_connection and one for sending messages using server_send_msg. 
10. The server_send_msg function is called to allow the server administrator to send messages and initiate the shutdown process if needed.
    
##Limitations
1. The chat application currently supports only text messages.  
2. The server can only run on localhost. To allow clients to connect from other machines, you need to modify the IP address accordingly.  
3. The server can handle multiple clients, but it doesn't have advanced features like user authentication or private messaging.

##Contributing
Feel free to modify and extend the code to add more functionality as per your requirements.  

