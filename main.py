from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from dotenv import load_dotenv
from api.bot_endpoints import router as api_router_bot

load_dotenv()
app = FastAPI()
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["*"],  # Allow all origins 
    allow_credentials=True, 
    allow_methods=["*"],  # Allow all methods 
    allow_headers=["*"], 
)

app.include_router(api_router_bot, prefix="/api")
