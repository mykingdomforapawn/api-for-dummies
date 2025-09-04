from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


# --- Model for data coming IN from the client ---
class DocumentCreate(BaseModel):
    name: str
    owner: str
    type: str


# --- Model for data going OUT (includes the server-generated id) ---
class Document(BaseModel):
    id: int
    name: str
    owner: str
    type: str


# Create your "in-memory database" and a counter for IDs
app = FastAPI()
db: List[Document] = []
id_counter = 0


# --- The POST endpoint ---
@app.post("/documents/", response_model=Document)
def create_document(document: DocumentCreate):  # Expect the input model
    global id_counter
    id_counter += 1

    # Create the full document using data from the input model
    new_document = Document(
        id=id_counter, name=document.name, owner=document.owner, type=document.type
    )
    db.append(new_document)
    return new_document


# --- The GET endpoint ---
@app.get("/documents/", response_model=List[Document])
def get_documents():
    return db


# --- The DELETE endpoint ---
@app.delete("/documents/{document_id}", status_code=204)
def delete_document(document_id: int):
    document_to_delete = None
    for doc in db:
        if doc.id == document_id:
            document_to_delete = doc
            break

    if document_to_delete is None:
        raise HTTPException(status_code=404, detail="Document not found")

    db.remove(document_to_delete)
    return
