import asyncio
import socket
from settings import HOST_server, PORT

WRITERS = set()


async def echo_server(reader, writer):
    WRITERS.add(writer)
    addr = writer.get_extra_info('peername')
    print(f"Connected {addr}")
    while True:
        data = await reader.read(100)
        message = data.decode()
        if not data:
            writer.close()
            break
        for writers in WRITERS:
            if writers == writer:
                print(f"Receive {message} from {addr}")
                continue
            writers.write(data)
        await asyncio.gather(*(writers.drain() for writers in WRITERS if writers != writer))


async def main():
    server = await asyncio.start_server(
        echo_server, host=HOST_server, port=PORT
    )
    print(f'Server start at adress: {",".join(str(sock.getsockname()) for sock in server.sockets)}')
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())