from fastapi import Request, FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import SqlManager
import os
import auth
import uvicorn

db = SqlManager()
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/api/{schema}/{table}/{id}")
async def get(schema, table, id, req: Request, tkn = Depends(auth.validate_token)):
    request_args = dict(req.query_params)
    return db.get(schema, table, id, params=request_args)

@app.post("/api/{schema}/{table}")
async def post(schema, table, request: Request, tkn = Depends(auth.validate_token)):
    data = await request.json()
    return db.post(schema, table, data)

@app.put("/api/{schema}/{table}/{id}")
async def put(schema, table, id, request: Request, tkn = Depends(auth.validate_token)):
    data = await request.json()
    return db.put(schema, table, id, data)

@app.delete("/api/{schema}/{table}/{id}")
async def delete(schema, table, id, tkn = Depends(auth.validate_token)):
    return db.delete(schema, table, id)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("API_PORT")),
        reload=True,
        ssl_keyfile="./server.key",
        ssl_certfile="./server.crt"
    )