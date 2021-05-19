import socket

# socket.AF_INET declaration of ip protocol
# socket.SOCK_STREAM declaration of tcp protocol
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# IP= server address
IP="127.0.0.1"
PORT=8820
socket.connect((IP, PORT))

data=""
while data!="Bye":
    msg=input("Enter your message\n")
    socket.send(msg.encode())
    data=socket.recv(1024).decode()
    print("server: ", data)

socket.close()