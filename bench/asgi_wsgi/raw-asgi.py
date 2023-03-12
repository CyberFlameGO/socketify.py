from socketify import ASGI

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })




if __name__ == "__main__":
    ASGI(app, lifespan=False).listen(8000, lambda config: print(f"Listening on port http://localhost:{config.port} now\n")).run(8)
