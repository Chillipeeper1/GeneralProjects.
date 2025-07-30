from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI


load_dotenv()  


HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("Por favor, define la variable de entorno HF_TOKEN con tu token de Hugging Face.")


try:
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",  
        api_key=HF_TOKEN,
    )
except Exception as e:
    raise RuntimeError(f"Error al conectar con Hugging Face: {e}")

app = FastAPI()

# Configura CORS para permitir conexiones desde tu frontend (React en localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo esperado en el POST
class QAInput(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: QAInput):
    """
    Recibe una pregunta y devuelve una respuesta del modelo DeepSeek.
    """
    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            messages=[
                {"role": "user", "content": data.question}
            ],
            max_tokens=512,
            temperature=0.7,
        )
        answer = completion.choices[0].message.content.strip()
        return {"answer": answer}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="No se pudo generar una respuesta.")