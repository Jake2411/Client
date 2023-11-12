from itertools import filterfalse
import socket
logIn = False
UserName = False
Password = False
userExists = True


host = '127.0.0.1'
port = 50001

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))

message = input(">> ")

while message.lower().strip() != 'quit':
    while logIn == False:
        data = clientSocket.recv(1024).decode()
        print(str(data))
        message = input(">> ")
        try:
            message = int(message)
        except ValueError:
            print("Wrong input")
            quit()
        clientSocket.send(str(message).encode())
        if message == 1:
            data = clientSocket.recv(1024).decode()
            print(str(data))
            while UserName == False:
                message = input(">> ")
                clientSocket.send(message.encode())
                data = clientSocket.recv(1024).decode()
                print(str(data))
                if (str(data) == "Now please enter your password"):
                    UserName = True
                    while Password == False:
                        message = input(">> ")
                        clientSocket.send(message.encode())
                        data = clientSocket.recv(1024).decode()
                        print(str(data))
                        if (str(data) == "Correct Password! Welcome to the chat app!"):
                            Password = True
                            logIn = True
        elif message == 2:
            data = clientSocket.recv(1024).decode()
            print(str(data))
            while userExists == True:
                

    message = input(">> ")
    clientSocket.send(message.encode())
    data = clientSocket.recv(1024).decode()
    print(str(data))

clientSocket.close()
