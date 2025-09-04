# API for Dummies

A simple project for learning and experimenting with the fundamental concepts of building a modern API from the ground up.

---

## Purpose

This project serves as a practical, hands-on sandbox for understanding how APIs work. The goal is to start with the most basic implementation possible—a simple REST API with in-memory data storage—and progressively add layers of complexity and modern tooling. It's a space to tinker, break things, and learn by doing, one concept at a time.

---

## Current Status

The API currently provides basic **CRUD** (Create, Read, Delete) functionality for managing document metadata.

* **Framework**: Python with **FastAPI**
* **Data Storage**: In-memory list (data is reset every time the server restarts)
* **Endpoints**:
    * `POST /documents/` - Create a new document.
    * `GET /documents/` - Retrieve the list of all documents.
    * `DELETE /documents/{id}` - Delete a specific document by its ID.

---

## How to Run Locally

1.  **Clone the repository and navigate into the directory.**

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the development server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be running at `http://127.0.0.1:8000`.

---

## Learning Roadmap

This project will be extended step-by-step to explore the following core concepts:

* [ ] **Data Persistency**: Transition from the in-memory list to a persistent database like **SQLite** to save data between server restarts.
* [ ] **Containerization**: Package the application into a **Docker** container to create a consistent, portable environment for development and deployment.
* [ ] **Automatic Documentation**: Leverage FastAPI's built-in support for **OpenAPI (Swagger UI)** to generate interactive API documentation automatically.
* [ ] **More Advanced Features**:
    * Implement the `UPDATE` (`PUT`/`PATCH`) endpoint.
    * Enhance data validation and error handling.
    * Add API testing.
