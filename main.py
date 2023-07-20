from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# User Class

class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password
  def get_username(self):
    return self.username
  def get_password(self):
    return self.password
  def set_password(self, new_password):
    self.password = new_password

# User Dummy Data
users = [
  {
    "username": "johndoe",
    "password": "password123"
  },
  {
    "username": "janedoe",
    "password": "password123"
  },
  {
    "username": "admin",
    "password": "password123"
  }
]


@app.post("/users")
def create_user(user: dict):
    """Creates a new user account."""
    if User.get_by_username(user["username"]):
        raise ValueError('Username already exists.')
    user = User(username=user["username"], password=user["password"])
    user.put()
    users.append(user)
    return {"message": "User created successfully."}

@app.get("/users")
def get_users():
    return users

@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    user = User.get(user_id)
    user.username = user["username"]
    user.password = user["password"]
    user.put()
    return {"message": "User updated successfully."}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Deletes a user account."""
    user = User.get(user_id)
    user.delete()
    return {"message": "User deleted successfully."}

