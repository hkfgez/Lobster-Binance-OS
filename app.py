from fastapi import FastAPI
from models import AnalyzeRequest, AnalyzeResponse
from main import analyze
from sample_data import get_demo_request

app = FastAPI(title="Lobster Binance OS", version="0.1.0")


@app.get("/")
def root():
    return {
        "name": "Lobster Binance OS",
        "message": "Unified intent routing and task orchestration layer for Binance ecosystem.",
    }


@app.get("/demo", response_model=AnalyzeResponse)
def demo():
    return analyze(get_demo_request())


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_route(request: AnalyzeRequest):
    return analyze(request)
