from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from translate import TranslationService

app = FastAPI(title="Secure Translator API")
translator = TranslationService()

class TranslationRequest(BaseModel):
    text: str

@app.post("/api/translate")
async def translate_endpoint(req: TranslationRequest):
    if not req.text:
        raise HTTPException(status_code=400, detail="Text is required.")
        
    result = translator.translate_text(req.text)
    if result is None:
        raise HTTPException(status_code=500, detail="Translation failed. Check limits or network.")
        
    return {"original": req.text, "translation": result}

@app.get("/")
async def read_index():
    return FileResponse("index.html")