from socketify import App, AppOptions, AppListenOptions
import asyncio

app = App()


def xablau(res, req):
    raise RuntimeError("Xablau!")


async def async_xablau(res, req):
    raise RuntimeError("Async Xablau!")



# this can be async no problems
@app.on_error
def on_error(error, res, req):
    # here you can log properly the error and do a pretty response to your clients
    print("Somethind goes %s" % str(error))
    # response and request can be None if the error is in an async function
    if res != None:
        # if response exists try to send something
        res.write_status(500)
        res.end("Sorry we did something wrong")


app.get("/", xablau)
app.get("/async", async_xablau)

# you can also use set_error_handler
# app.set_error_handler(on_error)

app.listen(
    3000,
    lambda config: print(
        "Listening on port http://localhost:%s now\n" % str(config.port)
    ),
)
app.run()
