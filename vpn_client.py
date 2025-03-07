import socket
import ssl
import time


def measure_speed(secure_socket):
    data = b'X' * 1024 * 1024  # 1 MB of data
    start_time = time.time()
    secure_socket.send(data)
    secure_socket.recv(1024)  # Wait for acknowledgment
    end_time = time.time()
    
    speed_mbps = (1 / (end_time - start_time)) * 8  # Convert to Mbps
    print(f"Speed: {speed_mbps:.2f} Mbps")


HOST = '127.0.0.1'  # Server address
PORT = 4443         # Secure port


# Create a standard TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Wrap the socket with SSL
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE 
secure_socket = context.wrap_socket(client_socket, server_hostname=HOST)


secure_socket.connect((HOST, PORT))
secure_socket.send("Hello, Secure Server!".encode())


response = secure_socket.recv(1024).decode()
print(f"[Server]: {response}")



secure_socket.close()
