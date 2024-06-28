import os
from fastapi import FastAPI
import uvicorn
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/streamlit")
def run_streamlit():
    cmd = ["streamlit", "run", "app.py"]
    subprocess.Popen(cmd)
    return {"message": "Streamlit app is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
