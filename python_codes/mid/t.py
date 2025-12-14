import hashlib
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def sha1_hash(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode())
    return sha1.hexdigest()


def response_handler(response: str):
    index = response.find("> ")
    indicator, message = response[: index + 1]


def tcp_server():
    ip, port = "localhost", 9001
    server.bind((ip, port))
    server.listen(1)
    clinet, addr = server.accept()
    while True:
        response = clinet.recv(1024)
        print(f"Received: {response.decode()}, from {addr[0]}:{addr[1]}")
        if response.decode() == "exit":
            clinet.send(b"exit")
            print("Connection closed.")
            break
        reply = response_handler()
        clinet.send(reply.encode())
        print(f"Sent: {reply}")

    clinet.close()
    server.close()
