from fastapi import APIRouter

router = APIRouter()


@router.post("/signup")
def signup():
    return {"status", "signup successful"}


@router.post("/login")
def login():
    return {"message": "login successful"}
