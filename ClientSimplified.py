import socket
import threading

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))

# Function to receive and print messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            break

# Start a new thread to handle receiving messages from the server
threading.Thread(target=receive_messages).start()

# Loop to read messages from the console and send them to the server
while True:
    message = input()
    if message:
        client_socket.sendall(message.encode('utf-8'))