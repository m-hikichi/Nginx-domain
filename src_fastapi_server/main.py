from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="FastAPI Web Page",
    description="",
)


@app.get(
    "/",
    description="ホームページの表示"
)
async def index():
    display_text = """
    <h1>Welcome to FastAPI web page!</h1>
    """
    return HTMLResponse(content=display_text)