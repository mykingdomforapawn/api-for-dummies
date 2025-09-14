from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance that will be used by all tests
client = TestClient(app)


def test_read_documents_initially_empty():
    """
    Tests if the GET /documents/ endpoint initially returns an empty list.
    """
    # Act: Perform a get request to see if the endpoint works.
    response = client.get("/documents/")

    # Assert: Check that the response code is as expected.
    assert response.status_code == 200


def test_create_document():
    """
    Tests the creation of a new document.
    """
    # Arrange: Prepare test data to create a new document.
    document_data = {"name": "Test Document", "owner": "Tester", "type": "Test"}

    # Act: Perform the creation of the document.
    response = client.post("/documents/", json=document_data)

    # Assert: Check that the creation was successful.
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["name"] == document_data["name"]
    assert "id" in response_json


def test_update_document():
    """
    Tests that a document can be successfully updated.
    """
    # Arrange: First, create a document to update.
    initial_data = {"name": "Original Name", "owner": "Original Owner", "type": "PDF"}
    create_response = client.post("/documents/", json=initial_data)
    assert create_response.status_code == 201
    document_id = create_response.json()["id"]

    updated_data = {"name": "Updated Name", "owner": "New Owner", "type": "Word"}

    # Act: Perform the update on the created document.
    update_response = client.put(f"/documents/{document_id}", json=updated_data)

    # Assert: Check that the update was successful and the data changed.
    assert update_response.status_code == 200
    response_json = update_response.json()
    assert response_json["name"] == "Updated Name"
    assert response_json["owner"] == "New Owner"
    assert response_json["id"] == document_id


def test_delete_document():
    """
    Tests that a document can be successfully deleted.
    """
    # Arrange: First, create a document so there is something to delete.
    document_to_delete = {"name": "To Be Deleted", "owner": "Temp", "type": "File"}
    create_response = client.post("/documents/", json=document_to_delete)
    assert create_response.status_code == 201
    document_id = create_response.json()["id"]

    # Act: Delete the document we just created.
    delete_response = client.delete(f"/documents/{document_id}")

    # Assert: Check that the deletion was successful.
    assert delete_response.status_code == 204

    # Assert: Verify the document is gone by trying to get it again.
    get_response = client.get(f"/documents/{document_id}")
    assert get_response.status_code == 404
