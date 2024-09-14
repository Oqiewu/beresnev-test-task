from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .crud import create_user, get_user, get_users, update_user, delete_user
from typing import List

app = FastAPI()

class UserIn(BaseModel):
    name: str
    email: str

class UserOut(UserIn):
    id: int

@app.post("/api/users", response_model=UserOut)
async def create_user_endpoint(user: UserIn):
    db_user = await create_user(user.name, user.email)
    return db_user

@app.get("/api/users", response_model=List[UserOut])
async def get_users_endpoint():
    users = await get_users()
    return users

@app.get("/api/users/{user_id}", response_model=UserOut)
async def get_user_endpoint(user_id: int):
    user = await get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/api/users/{user_id}", response_model=UserOut)
async def update_user_endpoint(user_id: int, user: UserIn):
    updated_user = await update_user(user_id, user.name, user.email)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/api/users/{user_id}")
async def delete_user_endpoint(user_id: int):
    await delete_user(user_id)
    return {"detail": "User deleted"}
