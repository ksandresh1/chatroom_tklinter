import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 6968

nickname = input("Enter the nickname")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()