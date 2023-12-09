import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import files

app = FastAPI()
app.include_router(files.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    return "Hello World!"


if __name__ == '__main__':
    print("Server is running on http://127.0.0.1:8000/")
    uvicorn.run(app, host="127.0.0.1", port=8000)