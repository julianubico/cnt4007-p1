import socket

PORT = input("Please enter a port that you'd like to listen on (or press ENTER for 5106):")
PORT = int(PORT) if PORT.isdigit() else 5106

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', PORT))
    server_socket.listen(1)

    print(f"Server socket binded on port: {PORT}")
    while True:
        client, address = server_socket.accept()
        with client:
            print(f"Connection from {address}")
            data = client.recv(1024)
            command = data.decode()
            filename = command.split()[1]
            if command.startswith("get"):
                print(f"Sending file: {filename}")
                with open(filename, 'rb') as file:
                    file = open(filename, 'rb')
                    data = file.read(1024)
                    while data:
                        client.sendall(data)
                        data = file.read(1024)
                print(f"File sent {filename} successfully")
            elif command.startswith("upload"):
                print(f"Receiving file: {filename}")
                with open('new' + filename, 'wb') as file:
                    while True:
                        data = client.recv(1024)
                        if not data: break
                        file.write(data)
                print(f"File new{filename} received")