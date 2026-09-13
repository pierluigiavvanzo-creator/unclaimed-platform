from fastapi import FastAPI

app = FastAPI(title="Unclaimed Platform", version="0.1.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "unclaimed-platform"}
