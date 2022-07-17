
#Socket is used to stablize the connextion between the client and server.
#Threading is used to run the parallel connection simultaneously. 
# One client should not wait for process because of other client. 
import socket
import threading

#HEADER tells about the length of message of 64 bytes.
HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

#defining the type of sockets for particular task.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg recieved".encode(FORMAT))
    conn.close()



def start():
    server.listen()
    print(f"[LISTENING] server is listening on {server}...")
    #to store the ip address and port of connection.
    while True:
        conn, addr = server.accept()

        #accept the connections and pass to the handle_client
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION {threading.activeCount()-1}")

    
print("[STARTING] server is starting...")
start()
