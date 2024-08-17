import socket

serverPort = 5151
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', serverPort))
server_socket.listen(5)
print("Server is ready")

try:
    while True:
        connection_socket, client_address = server_socket.accept()
        print('Got connection from', f"IP: {client_address[0]}, Port: {client_address[1]}")

        message = connection_socket.recv(1024).decode()
        print(f"Request: {message}")

       
        
        connection_socket.sendall(response.encode())
        connection_socket.close()

except KeyboardInterrupt:
    server_socket.close()
    print("Server closed.")
