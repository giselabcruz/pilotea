import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from src.pilotea.orchestrator import PiloteaOrchestrator
from typing import Any

load_dotenv()

app = FastAPI(title="Pilotea API")

orchestrator = PiloteaOrchestrator()

class QueryRequest(BaseModel):
    query: str

@app.post("/api/query")
async def handle_query(request: QueryRequest):
    try:
        result = await orchestrator.handle_query(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
