from tkinter import *
import socket
import threading
import mysql
from mysql.connector import Error
from datetime import datetime
  
def chatroom(window,username):
    try:
        con = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin',
                database='chatbox'
            )
    except:
        print("[ + ] Cannot connect database in chatroom")

    host = socket.gethostbyname(socket.gethostname())
    port = 6969

    nickname = username

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    
    
    def save_chat(nickname,word):
        print("here")
        k = datetime.now()
        format_date = k.strftime("%Y/%m/%d %H:%M:%S")
        check_chat_database()
        cursor = con.cursor(buffered=True)
        cursor.execute(f"""
        insert into chats (name, message, msg_datetime)
        values("{nickname}","{word}","{format_date}")
        """)
        con.commit()
        pass 
    
    def check_chat_database():
        table_require = "chats"
        tables=[]
        cursor = con.cursor(buffered=True)
        cursor.execute("show tables;")
        k = cursor.fetchall()
        for i in k:
            tables.extend(i)
        if table_require not in tables:
            cursor.execute(f"""
                create table {table_require}
                (id int not null auto_increment primary key,
                name varchar(50),
                message varchar(200),
                msg_datetime datetime
                )            
            """)
        pass
    
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
            save_chat(nickname,word)
            message = f'{nickname}: {word}'
            client.send(message.encode('ascii'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()


    # write_thread = threading.Thread(target=write)
    # write_thread.start()
