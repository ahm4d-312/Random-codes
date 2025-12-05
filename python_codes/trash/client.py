import socket

ip, port = "127.0.0.1", 5556
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
print(f"connected to: {ip}:{port}")
while True:
    msg = input("> ").encode()
    client.send(msg)
    msg = client.recv(1024)
    print(f"received: {msg.decode()}")
    if msg.decode() == "quit":
        client.send(msg)
        break
client.close()
