from socket import *

serverPort = 2300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('The server is ready to receive on port', serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    ip, port = addr
    print(f'Got connection from IP: {ip}, Port: {port}')

    request = connectionSocket.recv(1024).decode()
    print("Request received:\n", request)
    
    try:
        if 'GET / ' in request or 'GET /index.html' in request or 'GET /main_en.html' in request or 'GET /en' in request:
            with open('main_en.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html_content

        elif 'GET /ar' in request:
            with open('main_ar.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html_content

        elif 'GET /myform' in request:
            if 'keyword=bzu' in request:
                image_path = "C:\\Users\\HP\\Desktop\\networt\\images\\bzu.png"
                with open(image_path, 'rb') as file:
                    image_content = file.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\nContent-Length: {len(image_content)}\r\n\r\n"
                connectionSocket.sendall(response.encode() + image_content)
                print("mohammad")
                continue
            else:
                with open('myform.html', 'r', encoding='utf-8') as file:
                    html_content = file.read()
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html_content

        elif 'GET /jpg' in request:
            image_path = "C:\\Users\\HP\\Desktop\\networt\\images\\mohammadnemer.jpg"
            with open(image_path, 'rb') as file:
                image_content = file.read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: {len(image_content)}\r\n\r\n"
            connectionSocket.sendall(response.encode() + image_content)
            continue

        elif 'GET /png' in request:
            image_path = "C:\\Users\\HP\\Desktop\\networt\\images\\bzu.png"
            with open(image_path, 'rb') as file:
                image_content = file.read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: image/png\r\nContent-Length: {len(image_content)}\r\n\r\n"
            connectionSocket.sendall(response.encode() + image_content)
            continue

        elif 'GET /style.css' in request:
            with open('style.css', 'r', encoding='utf-8') as file:
                css_content = file.read()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n" + css_content

        elif 'GET /images/' in request:
            image_path = request.split(' ')[1][1:].lower()
            with open(image_path, 'rb') as file:
                image_content = file.read()
            if image_path.endswith('.jpg') or image_path.endswith('.jpeg'):
                content_type = "image/jpeg"
            elif image_path.endswith('.png'):
                content_type = "image/png"
            else:
                content_type = "application/octet-stream"
            response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(image_content)}\r\n\r\n"
            connectionSocket.sendall(response.encode() + image_content)
            continue

        elif 'GET /html' in request:
            with open('main_en.html', 'r', encoding='utf-8') as file:
                file_content = file.read()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n" + file_content

        elif 'GET /so' in request:
            response = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://stackoverflow.com\r\n\r\n"

        elif 'GET /itc' in request:
            response = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://itc.birzeit.edu\r\n\r\n"

        else:
            raise FileNotFoundError

    except FileNotFoundError:
        connectionSocket.send(b"HTTP/1.1 404 Not Found \r\n")
        connectionSocket.send(b"Content-Type: text/html \r\n")
        connectionSocket.send(b"\r\n")
        print("Response status: 404 Not Found")
        error_html = f'''
        <!DOCTYPE html>
        <html>
        <head><title>Error 404</title></head>
        <body style="text-align: center; font-size: large; font-weight: bold;">
            <h1 style="font-size: 50px; color: blue;">The file is not found</h1>
            <hr>
            <div><p>Mohammad Nemer - 1222300</p><p>Ahmad Rimawi  - 1221714</p><p>Mohammad Tomazi   - 1220078</p></div>
            <hr>
            <div><p>IP Address: {str(ip)}, Port number: {str(port)}</p></div>
        </body>
        </html>
        ''' 
        connectionSocket.sendall(error_html.encode())

    connectionSocket.sendall(response.encode())
    connectionSocket.close()
