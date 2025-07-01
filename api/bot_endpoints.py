from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
import uuid
from services.pdf_parser import parse_pdf
from services.chroma_store import store_pdf_in_chroma
from services.qa_engine import get_qa_chain

router = APIRouter()
SESSIONS = {}

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    session_id = str(uuid.uuid4())
    texts = parse_pdf(pdf_bytes)
    store_pdf_in_chroma(session_id, texts)
    chain = get_qa_chain(session_id)
    SESSIONS[session_id] = chain
    return {"session_id": session_id, "message": "PDF uploaded and processed."}

@router.post("/chat/")
async def chat(session_id: str = Form(...), question: str = Form(...)):
    if session_id not in SESSIONS:
        return JSONResponse(status_code=404, content={"error": "Session ID not found."})
    chain = SESSIONS[session_id]
    result = chain.run(question)
    return {"question": question, "answer": result}