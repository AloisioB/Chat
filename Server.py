import socket
import threading

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5555
server_socket.bind(('localhost', port))
server_socket.listen()

# List to keep track of all client sockets
client_sockets = []

# Function to handle receiving messages from a client
def receive_messages(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f'{client_address}: {message}')
                broadcast_messages(message, client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

# Function to broadcast a message to all clients
def broadcast_messages(message, sender_socket):
    for client_socket in client_sockets:
        try:
            client_socket.sendall(message.encode('utf-8'))
        except:
            remove_client(client_socket)

# Function to remove a client from the list of clients
def remove_client(client_socket):
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)

# Function to accept new client connections
def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        client_sockets.append(client_socket)
        client_socket.sendall('Welcome to the chat!\n'.encode('utf-8'))
        threading.Thread(target=receive_messages, args=(client_socket, client_address)).start()

# Function to send a message to all clients
def send_message():
    Name = input("Enter your name, please: ")
    while True:
        message = input()
        if message:
            message = Name + ": " + message
            print(message)
            broadcast_messages(message, None)

# Start the server, accept new clients, and start sending messages in separate threads
print(f'Server started. Listening on port {port}...')
threading.Thread(target=accept_clients).start()
threading.Thread(target=send_message).start()
