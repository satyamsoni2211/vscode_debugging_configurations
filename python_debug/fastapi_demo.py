import json
import asyncio
from uvicorn import run, Server, Config
from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.on_event("startup")
async def startup():
    queue = asyncio.Queue()
    app.state.queue = queue
    event = asyncio.Event()
    app.state.event = event
    tasks = asyncio.create_task(worker(queue, event), name="worker")
    app.state.task = tasks


async def worker(queue: asyncio.Queue, event: asyncio.Event):
    try:
        task = asyncio.tasks.current_task()
        name = task.get_name()
        print(f"started {name} ... ")
        while not event.is_set():
            try:
                elem = queue.get_nowait()
                print(f"{name} got {elem=}")
                queue.task_done()
                await asyncio.sleep(1)
            except asyncio.QueueEmpty:
                await asyncio.sleep(1)
        print("quitting !")
    except asyncio.CancelledError as e:
        print(f"exception occurred ! {e}")
        raise e


@app.on_event("shutdown")
async def shutdown():
    event = app.state.event
    event.set()
    task = app.state.task
    t_ = task.cancel(msg=f"Cancelling {task.get_name()}...")
    print(f"cancelled {task.get_name()} {t_=}")
    print("waiting for tasks to finish ...")
    exceptions = await asyncio.gather(task, return_exceptions=True)
    print(exceptions)


@app.get("/")
async def home(request: Request):
    await request.app.state.queue.put("from home ")
    return {"message": "Hello World"}

if __name__ == "__main__":
    # run("demo:app", host="0.0.0.0", port=8000, reload=True)
    config = Config(app='demo:app', host="0.0.0.0"
                    )
    server = Server(config=config)
    server.run()
