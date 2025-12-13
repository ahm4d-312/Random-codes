import socket as s


def tcp_server():
    ip, port = "0.0.0.0", 9001
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)
    client, addr = server.accept()
    i = 0
    while True:
        if i == 10:
            break
        i += 1
        response = client.recv(1024)
        print(f"Received: {response.decode()}")
        if response.decode() == "exit":
            client.send(b"exit")
            print("Connection closed.")
            break
        reply = input("> ").encode()
        client.send(reply)
        print(f"Sent: {reply.decode()}")
    client.close()


def main():
    tcp_server()


if __name__ == "__main__":
    main()
