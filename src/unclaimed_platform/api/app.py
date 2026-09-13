from fastapi import FastAPI

from .reviewer import router as reviewer_router

app = FastAPI(title="Unclaimed Platform", version="0.1.0")
app.include_router(reviewer_router)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "unclaimed-platform"}
