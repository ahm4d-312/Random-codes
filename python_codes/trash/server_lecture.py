import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def udp_server():
    while True:
        response, address = server.recvfrom(1024)
        operation = response.decode()
        if operation == "exit":
            server.sendto(b"exit", address)
            break
        print(f"received a msg from {address[0]}:{address[1]}, operation: {operation}")
        result = str(eval(operation)).encode()
        server.sendto(result, address)
    server.close()


def main():
    ip, port = "0.0.0.0", 4444
    server.bind((ip, port))
    udp_server()


if __name__ == "__main__":
    main()
