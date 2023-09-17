import asyncio
import logging

active_clients = 0


async def client_connected_cb(reader, writer) -> None:
    global active_clients
    active_clients += 1
    print(f"New client connected. Now there are {active_clients} clients")
    line = await reader.readline()
    writer.write(line)
    await writer.drain()  # This is a flow control method that interacts with the underlying IO write buffer.
    writer.close()
    active_clients -= 1
    print(f"Client left. Now there are {active_clients} clients")


async def echo_server() -> None:
    print("Starting a server")
    server = await asyncio.start_server(
        client_connected_cb, host="0.0.0.0", port="8080"
    )
    await server.serve_forever()


logging.basicConfig(level=logging.DEBUG)
asyncio.run(echo_server(), debug=True)
