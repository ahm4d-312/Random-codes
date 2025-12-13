import socket


def main():
    ip, port = "localhost", 9001
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    while True:
        msg = input("> ").encode()
        client.send(msg)
        print(f"Sent: {msg.decode()}")
        response = client.recv(1024)
        print(f"Received: {response.decode()}")
        if response.decode() == "exit":
            client.send(b"exit")
            print("Connection closed.")
            break
    client.close()


if __name__ == "__main__":
    main()
# 8021x
