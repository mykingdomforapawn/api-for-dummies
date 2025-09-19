# API for Dummies

A simple project for learning and experimenting with the fundamental concepts of building a modern API from the ground up.

> **AI Disclaimer:** This project was developed with the assistance of Google's Gemini to guide the learning process, explain concepts, and generate code.

---

## Purpose

This project serves as a practical, hands-on sandbox for understanding how APIs work. The goal is to start with the most basic implementation possible—a simple REST API with in-memory data storage—and progressively add layers of complexity and modern tooling. It's a space to tinker, break things, and learn by doing, one concept at a time.

---

## Current Status

The API provides a professional CI/CD pipeline for testing, continuous integration, and versioned releases.

* **Framework**: Python with **FastAPI**
* **Data Storage**: In-memory list (data resets every time the server restarts)
* **Automation**: A CI/CD setup using GitHub Actions:
    * **On pushes to `main`**: Workflows automatically run tests and publish a `:latest` Docker image to GHCR.
    * **On pushing a version tag** (e.g., `v1.0.0`): A separate workflow publishes a versioned Docker image and creates a GitHub Release with the `openapi.json` spec attached as a downloadable artifact.
* **Endpoints (Full CRUD)**:
    * `POST /documents/` - Create a new document.
    * `GET /documents/` - Retrieve all documents and a single document by ID.
    * `PUT /documents/{id}` - Update an existing document.
    * `DELETE /documents/{id}` - Delete a specific document.

---

## How to Create a Release

This project uses Git tags to trigger the release process.

1.  **Tag a new version:**
    ```bash
    git tag v1.0.0
    ```
2.  **Push the tag to GitHub:**
    ```bash
    git push origin v1.0.0
    ```
This will automatically trigger the `publish-release` workflow, creating a new GitHub Release with the attached `openapi.json` and a versioned Docker image.

---

## How to Run Locally (for Development)

1.  **Clone the repository and navigate into the directory.**

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies from `requirements.txt`:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  **Start the development server:**
    The `--reload` flag automatically restarts the server when you change the code.
    ```bash
    uvicorn main:app --reload
    ```
    The API will be running at `http://127.0.0.1:8000`.

---

## How to Run with Docker

You can run either the latest development build or a specific versioned release.

### Running the Latest Development Build
1.  **Pull the latest image:**
    ```bash
    docker pull ghcr.io/mykingdomforapawn/api-for-dummies:latest
    ```
2.  **Run the container:**
    ```bash
    docker run -d -p 8000:8000 --name my-api-container ghcr.io/mykingdomforapawn/api-for-dummies:latest
    ```

### Running a Specific Versioned Release
1.  **Pull a versioned image** (e.g., v1.0.0):
    ```bash
    docker pull ghcr.io/mykingdomforapawn/api-for-dummies:v1.0.0
    ```
2.  **Run the container:**
    ```bash
    docker run -d -p 8000:8000 --name my-api-container ghcr.io/mykingdomforapawn/api-for-dummies:v1.0.0
    ```
After running, the API will be available at `http://localhost:8000/docs`.

---

## Learning Roadmap

This project has explored the following core concepts:

* [x] **Automatic Documentation**: Used FastAPI's built-in support for **OpenAPI** to generate an API specification.
* [x] **CI/CD Automation**: Set up workflows for both continuous integration (testing, pushing `:latest` builds) and formal releases (pushing versioned artifacts on Git tags).
* [x] **Containerization**: Packaged the application into a **Docker** container and integrated it into the CI/CD pipeline.
* [x] **Testing & Validation**: Implemented a test suite with `pytest` and added robust data validation with Pydantic.
* [x] **CRUD Implementation**: Built a full set of Create, Read, Update, and Delete endpoints.

The final major concept to explore for this project would be:
* [ ] **Data Persistency**: Transition from the in-memory list to a persistent database like **SQLite**.
