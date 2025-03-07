import socket
import ssl

HOST = '0.0.0.0'
PORT = 4443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("[+] Waiting for connections...")

while True:
    conn, addr = server_socket.accept()
    print(f"[+] New connection from {addr}")

    try:
        secure_conn = context.wrap_socket(conn, server_side=True)
        
        while True:  # Оставляем соединение открытым для приёма данных
            data = secure_conn.recv(1024)
            if not data:
                break
            print("[Received]:", data.decode())

        secure_conn.close()
    except ssl.SSLError as e:
        print("[!] SSL Error:", e)
    except ConnectionResetError:
        print("[!] Client disconnected unexpectedly")