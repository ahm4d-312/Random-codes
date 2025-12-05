import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ("127.0.0.1", 4444)
    while True:
        operatoin = input("> ").encode()
        client.sendto(operatoin, (address))
        print(f"sent: {operatoin.decode()},to {address[0]}:{address[1]}")
        response, address = client.recvfrom(1024)
        if response.decode() == "exit":
            break
        print(f"result: {response.decode()}")
    client.close()


if __name__ == "__main__":
    main()
