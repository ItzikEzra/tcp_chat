import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP="0.0.0.0"
PORT=8820
server_socket.bind((IP,PORT))

server_socket.listen()
print("server listen")

(client_socket,client_address)=server_socket.accept()
print("client connected")
while True:
    data=client_socket.recv(1024).decode()
    print("Client: ", data)
    if data == "Q":
        print("Closing..")
        client_socket.send("Bye".encode())
        break
    client_socket.send(data.encode())

client_socket.close()

server_socket.close()