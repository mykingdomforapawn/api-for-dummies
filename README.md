# API for Dummies

A simple project for learning and experimenting with the fundamental concepts of building a modern API from the ground up.

> **AI Disclaimer:** This project was developed with the assistance of Google's Gemini to guide the learning process, explain concepts, and generate code.

---

## Purpose

This project serves as a practical, hands-on sandbox for understanding how APIs work. The goal is to start with the most basic implementation possible—a simple REST API with in-memory data storage—and progressively add layers of complexity and modern tooling. It's a space to tinker, break things, and learn by doing, one concept at a time.

---

## Current Status

The API provides a full CI/CD pipeline for documentation, containerization, and basic CRUD functionality.

* **Framework**: Python with **FastAPI**
* **Data Storage**: In-memory list (data is reset every time the server restarts)
* **Automation**: Includes GitHub Actions workflows to:
    * Automatically generate and commit the `openapi.json` spec.
    * Run automated tests with `pytest` on every push.
    * Automatically build and push a Docker image to the GitHub Container Registry (GHCR) on changes to the API.
* **Endpoints (Full CRUD)**:
    * `POST /documents/` - Create a new document.
    * `GET /documents/` - Retrieve all documents.
    * `PUT /documents/{id}` - Update an existing document.
    * `DELETE /documents/{id}` - Delete a specific document.

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

## How to Run with Docker

You can also run the pre-built container image from the GitHub Container Registry.

1.  **Pull the latest image:**
    ```bash
    docker pull ghcr.io/mykingdomforapawn/api-for-dummies:sha-183691d
    ```

2.  **Run the container:**
    This command starts the container and maps your local port 8000 to the container's port 8000.
    ```bash
    docker run -d -p 8000:8000 --name my-api-container ghcr.io/your-username/your-repo:latest
    ```
3.  **Test it:**
    The API will be available at `http://localhost:8000/docs`.

---

## Learning Roadmap

This project will be extended step-by-step to explore the following core concepts:

* [x] **Automatic Documentation**: Use FastAPI's built-in support for **OpenAPI (Swagger UI)** to generate an API specification.
* [x] **CI/CD Automation**: Set up a **GitHub Actions** workflow to automatically generate and commit the OpenAPI spec.
* [x] **Containerization**: Package the application into a **Docker** container and set up a CI/CD workflow to automatically publish it to a registry.
* [x] **Advanced Features & Testing**:
    * [x] Implement the `UPDATE` (`PUT`) endpoint.
    * [x] Enhance data validation and error handling.
    * [x] Add API testing to the CI/CD workflow.
