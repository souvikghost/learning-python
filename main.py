from fastapi import FastAPI

from routes.auth import router as auth_router

# routes.auth -> routes/ → folder & auth.py → file
# as auth_router -> rename for clarity

from routes.user import router as user_router

# app = the whole API server (logic-wise)
app=FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
