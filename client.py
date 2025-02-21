import socket

PORT = input("Please enter a port that you'd like to connect to (or press ENTER for 5106): ")
PORT = int(PORT) if PORT.isdigit() else 5106

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost', PORT))
        command = input("""Options:
    1. get <filename>
    2. upload <filename>
    3. exit
Please enter a command: """)

        if command.startswith("exit"):
            break
        elif command.startswith("upload"):
            client_socket.sendall(command.encode())
            filename = command.split()[1]
            with open (filename, 'rb') as file:
                data = file.read(1024)
                while data: 
                    client_socket.sendall(data)
                    data = file.read(1024)
            print(f"File sent {filename} successfully")
        elif command.startswith("get"):
            client_socket.sendall(command.encode())
            filename = 'new' + command.split()[1]
            with open(filename, 'wb') as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data: break
                    file.write(data)

            print(f"File received {filename} successfully")
        else:
            print("Invalid command")
            continue