import socket


def wait():
    input()


ip, port = "localhost", 4444
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"Created the the server object: {server}")
wait()

server.bind((ip, port))
print(f"Used bind method to assocaite the server with: {ip}:{port}")
wait()

response, address = server.recvfrom(1024)
print(f"Recived the Msg: {response.decode()}, from {address}")
wait()

msg = "Hello clinet"
print(f"Created the msg: {msg}, of type:{type(msg)}")
wait()

print(
    f"Note: In order to send the msg, it must be converted to raw bytes since that the 'send' method only takes raw bytes parameters NOT str parmaeters"
)
wait()

msg_encoded = msg.encode("UTF-8")
print(f"encoded the msg to raw bytes: {msg_encoded}, of type: {type(msg_encoded)}")
wait()

server.sendto(msg_encoded, address)
print(f"sent the msg:{msg}, to: {address}")
wait()

server.close()
print("Finished")
