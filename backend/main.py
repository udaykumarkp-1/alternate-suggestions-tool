from fastapi import FastAPI
from routers import search_router, save_router, status_router

app = FastAPI(title="Alternate Suggestions API")

# Include routers
app.include_router(search_router.router)
app.include_router(save_router.router)
app.include_router(status_router.router)

# Run locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)