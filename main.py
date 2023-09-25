from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.models import Base, db_helper
from items_views.items_views import router as items_router
from users.views import router as users_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)




@app.get("/")
def hello_world():
    return {"message": "hello world"}





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
