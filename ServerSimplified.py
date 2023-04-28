import socket
import threading

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5555
server_socket.bind(('localhost', port))
server_socket.listen()

# Accept a client connection
client_socket, client_address = server_socket.accept()

# Function to receive and print messages from the client
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            break