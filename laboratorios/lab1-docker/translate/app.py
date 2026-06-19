from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from translate import TranslationService

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Secure Translator API")

# Instancia como dependencia controlada, no global mutable
def get_translator() -> TranslationService:
    return TranslationService()

class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, description="Texto a traducir")

@app.post("/api/translate")
async def translate_endpoint(req: TranslationRequest):
    # La validación de longitud ya la hace Pydantic con max_length
    translator = get_translator()
    result = translator.translate_text(req.text)
    if result is None:
        raise HTTPException(status_code=500, detail="Translation failed. Check limits or network.")
    return {"original": req.text, "translation": result}

@app.get("/")
async def read_index():
    index_path = BASE_DIR / "index.html"
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="index.html not found")
    return FileResponse(str(index_path))

@app.get("/health")
async def health_check():
    """Endpoint para el healthcheck del contenedor."""
    return {"status": "ok"}
