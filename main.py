from fastapi import FastAPI
import uvicorn

from middlewares import ErrorHandlerMiddleWare
from routers import recipes


app = FastAPI()


app.add_middleware(ErrorHandlerMiddleWare)

app.include_router(recipes.router, prefix='/recipes')


if __name__ == '__main__':
    uvicorn.run(
        app, host='localhost', port=8080
    )
