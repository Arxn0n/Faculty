from fastapi import FastAPI
from database import Base, engine
from routes import employeer
import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(employeer.router)

if __name__ == "__main__": uvicorn.run("main:app", reload=True)