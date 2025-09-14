from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


# --- Model for data coming IN from the client ---
class DocumentCreate(BaseModel):
    name: str
    owner: str
    type: str


# --- Model for data going OUT ---
class Document(BaseModel):
    id: int
    name: str
    owner: str
    type: str


# Create "in-memory database" and a counter for IDs
app = FastAPI(
    title="Document API for Dummies",
    version="0.1.0",
    description="A simple API to learn the basics and experiment with documents.",
)
db: List[Document] = []
id_counter = 0


# --- The POST endpoint ---
@app.post("/documents/", response_model=Document, status_code=201)
def create_document(document: DocumentCreate):
    global id_counter
    id_counter += 1

    # Create the full document using data from the input model
    new_document = Document(
        id=id_counter, name=document.name, owner=document.owner, type=document.type
    )
    db.append(new_document)
    return new_document


# --- The GET endpoints ---
@app.get("/documents/", response_model=List[Document])
def get_documents():
    return db


@app.get("/documents/{document_id}", response_model=Document)
def get_document_by_id(document_id: int):
    for doc in db:
        if doc.id == document_id:
            return doc
    raise HTTPException(status_code=404, detail="Document not found")


# --- The PUT endpoint ---
@app.put("/documents/{document_id}", response_model=Document)
def update_document(document_id: int, document_update: DocumentCreate):
    for i, doc in enumerate(db):
        if doc.id == document_id:
            # Create a new document object with the updated data
            updated_doc = Document(id=document_id, **document_update.model_dump())
            # Replace the old document in the list
            db[i] = updated_doc
            return updated_doc
    # If the loop finishes without finding the document, raise an error
    raise HTTPException(status_code=404, detail="Document not found")


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
