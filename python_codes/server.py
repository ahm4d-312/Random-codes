import socket
from datetime import datetime

ip, port = "0.0.0.0", 5556
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)
client, clinet_addr = server.accept()
print(f"accepted connection from {clinet_addr[0]}:{clinet_addr[1]}")
while True:
    msg = client.recv(1024)
    print(f"received: {msg.decode()}")
    if msg.decode() == "quit":
        client.send(msg)
        break
    if msg.decode() == "sync_time":
        current_time = str(datetime.now())
        client.send(current_time.encode())
        print(f"> {current_time}")
        continue
    msg = input("> ").encode()
    client.send(msg)
client.close()
