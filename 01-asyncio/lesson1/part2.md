# Asyncio - lesson 1.2

### Echo server

#

> Reading

Read: https://docs.python.org/3/library/asyncio-runner.html

Read: https://docs.python.org/3/library/asyncio-task.html

Read: https://docs.python.org/3/library/asyncio-stream.html

#

> Exercise

In this exercise you will write echo server.
Such a server should start the server and listen to clients.
Every time a new client connects, the server will receive the request and listen to a message from it.
The server will receive the message and also return the message that was written exactly (as if it was echoed).
After the message is printed, the connection will be terminated.

For this, we will use `asyncio`. The server runs on host="0.0.0.0", port="8080".

In order to simulate a client use the `nc` command in linux:

```
nc localhost 8080
```

Output Exmaple:

```
nc localhost 8080
Albert!
Albert!
```
