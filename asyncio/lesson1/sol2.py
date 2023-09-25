import asyncio
import logging


async def client_connected_cb(reader, writer) -> None:
    line = await reader.readline()
    writer.write(line)
    await writer.drain()  # This is a flow control method that interacts with the underlying IO write buffer.
    writer.close()


async def echo_server() -> None:
    print("Starting a server")
    server = await asyncio.start_server(
        client_connected_cb, host="0.0.0.0", port="8080"
    )
    await server.serve_forever()


logging.basicConfig(level=logging.DEBUG)
asyncio.run(echo_server(), debug=True)
