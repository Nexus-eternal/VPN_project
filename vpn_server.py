import socket
import ssl


# Define server address and port
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 4443       # Secure port


# Create a standard TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Allow up to 5 connections


print(f"[*] Server listening on {HOST}:{PORT}")


# Wrap the socket with SSL encryption
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")



with context.wrap_socket(server_socket, server_side=True) as secure_socket:
    while True:
        conn, addr = secure_socket.accept()
        print(f"[+] New connection from {addr}")
        
        data = conn.recv(1024).decode()
        print(f"[Client]: {data}")
        
        conn.send("Secure connection established!".encode())
        conn.close()
