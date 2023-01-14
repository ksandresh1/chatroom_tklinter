from tkinter import *
import socket
import threading

def chatroom(window):
    host = socket.gethostbyname(socket.gethostname())
    port = 6968

    nickname = input("Enter the nickname")

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    def send(sendchatarea):
        k = sendChatarea.get("1.0", "end-1c")
        write(k)
        


    showChatFrame = Frame(window,width=500,height=250,bg="white")
    showChatFrame.pack(padx=10,pady=10)
    showChatFrame.pack_propagate(False)

    sendChatFrame = Frame(window,width=500,height=200,bg="white")
    sendChatFrame.pack(side="bottom",padx=10,pady=10)
    sendChatFrame.pack_propagate(False)

    showChatarea = Text(showChatFrame, height=500, width=250, bg="light cyan")
    showChatarea.pack()


    sendChatarea = Text(sendChatFrame, height=9, width=250, bg="light yellow")
    sendChatarea.pack()


    sendbtn = Button(sendChatFrame,text="Send",command=lambda:send(sendChatarea))
    sendbtn.pack()
    
    def showMessage(message):
        print(message)
        showChatarea.insert(END,message+'\n')
        pass

    def receive():
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                if message == 'NICK':
                    pass
                else:
                    showMessage(message)


            except:
                print("An error occured")
                client.close()
                break
    def write(word):
            message = f'{nickname}: {word}'
            client.send(message.encode('ascii'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    # write_thread = threading.Thread(target=write)
    # write_thread.start()