from fastapi import FastAPI

app = FastAPI()

@app.get("/ask/")
async def ask(question: str):
    return {"response": ask_question(question)}
