from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --------------------
# Data Model
# --------------------
class Tea(BaseModel):
    id: int
    name: str
    origin: str


# In-memory storage
teas: list[Tea] = []


# --------------------
# Root
# --------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to chai code"}


# --------------------
# Get all teas
# --------------------
@app.get("/teas")
def get_teas():
    return teas
~

# --------------------
# Add tea
# --------------------
@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea


# --------------------
# Update tea
# --------------------
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            updated_tea.id = tea_id
            teas[index] = updated_tea
            return updated_tea

    raise HTTPException(status_code=404, detail="Tea not found")


# --------------------
# Delete tea
# --------------------
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return deleted

    raise HTTPException(status_code=404, detail="Tea not found")