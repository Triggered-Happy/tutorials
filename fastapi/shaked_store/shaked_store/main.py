from fastapi import FastAPI
import uvicorn
from shaked_store.routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        log_level="debug",
        reload=True,
    )
