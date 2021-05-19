import socket
import select

IP = "0.0.0.0"
PORT = 8820
MAX_LEN = 1024


def print_client_Sockets(sockets):
    for c in sockets:
        print("\t",c.getpeername())

print("Setting up")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()
print("listen to clients")
client_sockets = []
while True:
    ready_to_read, ready_to_write, in_error = select.select([server_socket] + client_sockets, [], [])
    for current_socket in ready_to_read:
        if current_socket is server_socket:
            (client_socket,client_address)=current_socket.accept()
            print("New client joined ", client_address)
            client_sockets.append(client_socket)
            print_client_Sockets(client_sockets)
        else:
            print("new data from client")
            data=current_socket.recv(1024).decode()
            print(data)
            for c in client_sockets:
                client_socket.send(data.encode())
            if data == "":
                print("connection closed")
                client_sockets.remove(current_socket)
                print_client_Sockets(client_sockets)
                current_socket.close()
server_socket.close()