"""
╔══════════════════════════════════════════════════════════════════════════╗
║                    PHASE 1 VERIFICATION TESTS                          ║
║                                                                        ║
║  These tests verify your CRUD implementation is correct.               ║
║  They test the API endpoints end-to-end via HTTP requests.             ║
║                                                                        ║
║  Run: make verify-phase1                                               ║
║   or: cd backend && uv run pytest tests/verification/test_phase1_check.py -v  ║
║                                                                        ║
║  Target: 20/20 tests passing                                           ║
║                                                                        ║
║  IMPORTANT: Docker must be running (`make up`) for DB access.          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import uuid

import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


# ── Document CRUD Tests ──────────────────────────────────────────────────────


class TestDocumentCreate:
    """POST /api/v1/documents"""

    async def test_create_document(self, client: AsyncClient) -> None:
        """Creating a document returns 201 with the document data."""
        payload = {
            "title": "Test Document",
            "filename": "test.pdf",
            "content_type": "application/pdf",
            "file_size": 1024,
        }
        response = await client.post("/api/v1/documents/", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Document"
        assert data["filename"] == "test.pdf"
        assert data["status"] == "draft"
        assert "id" in data
        assert "created_at" in data

    async def test_create_document_minimal(self, client: AsyncClient) -> None:
        """Creating with only required fields works."""
        payload = {
            "title": "Minimal",
            "filename": "min.md",
            "content_type": "text/markdown",
        }
        response = await client.post("/api/v1/documents/", json=payload)
        assert response.status_code == 201
        assert response.json()["file_size"] == 0

    async def test_create_document_validation_error(self, client: AsyncClient) -> None:
        """Creating without required fields returns 422."""
        response = await client.post("/api/v1/documents/", json={})
        assert response.status_code == 422


class TestDocumentList:
    """GET /api/v1/documents"""

    async def test_list_documents_empty(self, client: AsyncClient) -> None:
        """Empty database returns empty list, not 404."""
        response = await client.get("/api/v1/documents/")
        assert response.status_code == 200
        assert response.json() == []

    async def test_list_documents_with_data(self, client: AsyncClient) -> None:
        """Lists documents after creation."""
        for i in range(3):
            await client.post(
                "/api/v1/documents/",
                json={
                    "title": f"Doc {i}",
                    "filename": f"doc{i}.pdf",
                    "content_type": "application/pdf",
                },
            )
        response = await client.get("/api/v1/documents/")
        assert response.status_code == 200
        assert len(response.json()) == 3

    async def test_list_documents_pagination(self, client: AsyncClient) -> None:
        """Pagination with skip and limit works."""
        for i in range(5):
            await client.post(
                "/api/v1/documents/",
                json={
                    "title": f"Doc {i}",
                    "filename": f"doc{i}.pdf",
                    "content_type": "application/pdf",
                },
            )
        response = await client.get("/api/v1/documents/?skip=2&limit=2")
        assert response.status_code == 200
        assert len(response.json()) == 2


class TestDocumentGet:
    """GET /api/v1/documents/{id}"""

    async def test_get_document(self, client: AsyncClient) -> None:
        """Getting an existing document returns it."""
        create = await client.post(
            "/api/v1/documents/",
            json={
                "title": "Get Me",
                "filename": "get.pdf",
                "content_type": "application/pdf",
            },
        )
        doc_id = create.json()["id"]
        response = await client.get(f"/api/v1/documents/{doc_id}")
        assert response.status_code == 200
        assert response.json()["title"] == "Get Me"

    async def test_get_document_not_found(self, client: AsyncClient) -> None:
        """Getting a non-existent document returns 404."""
        fake_id = uuid.uuid4()
        response = await client.get(f"/api/v1/documents/{fake_id}")
        assert response.status_code == 404


class TestDocumentUpdate:
    """PATCH /api/v1/documents/{id}"""

    async def test_update_document(self, client: AsyncClient) -> None:
        """Updating a document changes only the specified fields."""
        create = await client.post(
            "/api/v1/documents/",
            json={
                "title": "Original",
                "filename": "orig.pdf",
                "content_type": "application/pdf",
            },
        )
        doc_id = create.json()["id"]
        response = await client.patch(
            f"/api/v1/documents/{doc_id}",
            json={"title": "Updated"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated"
        assert data["filename"] == "orig.pdf"  # unchanged

    async def test_update_document_not_found(self, client: AsyncClient) -> None:
        """Updating a non-existent document returns 404."""
        fake_id = uuid.uuid4()
        response = await client.patch(
            f"/api/v1/documents/{fake_id}",
            json={"title": "Nope"},
        )
        assert response.status_code == 404


class TestDocumentDelete:
    """DELETE /api/v1/documents/{id}"""

    async def test_delete_document(self, client: AsyncClient) -> None:
        """Deleting a document returns 204 and removes it."""
        create = await client.post(
            "/api/v1/documents/",
            json={
                "title": "Delete Me",
                "filename": "del.pdf",
                "content_type": "application/pdf",
            },
        )
        doc_id = create.json()["id"]
        response = await client.delete(f"/api/v1/documents/{doc_id}")
        assert response.status_code == 204

        # Verify it's gone
        get_response = await client.get(f"/api/v1/documents/{doc_id}")
        assert get_response.status_code == 404

    async def test_delete_document_not_found(self, client: AsyncClient) -> None:
        """Deleting a non-existent document returns 404."""
        fake_id = uuid.uuid4()
        response = await client.delete(f"/api/v1/documents/{fake_id}")
        assert response.status_code == 404


# ── Collection CRUD Tests ────────────────────────────────────────────────────


class TestCollectionCreate:
    """POST /api/v1/collections"""

    async def test_create_collection(self, client: AsyncClient) -> None:
        """Creating a collection returns 201."""
        payload = {"name": "My Collection", "description": "Test collection"}
        response = await client.post("/api/v1/collections/", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "My Collection"
        assert "id" in data


class TestCollectionList:
    """GET /api/v1/collections"""

    async def test_list_collections_empty(self, client: AsyncClient) -> None:
        """Empty database returns empty list."""
        response = await client.get("/api/v1/collections/")
        assert response.status_code == 200
        assert response.json() == []


class TestCollectionGet:
    """GET /api/v1/collections/{id}"""

    async def test_get_collection(self, client: AsyncClient) -> None:
        """Getting an existing collection returns it."""
        create = await client.post(
            "/api/v1/collections/",
            json={"name": "Find Me"},
        )
        col_id = create.json()["id"]
        response = await client.get(f"/api/v1/collections/{col_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "Find Me"

    async def test_get_collection_not_found(self, client: AsyncClient) -> None:
        """Getting a non-existent collection returns 404."""
        fake_id = uuid.uuid4()
        response = await client.get(f"/api/v1/collections/{fake_id}")
        assert response.status_code == 404


class TestCollectionUpdate:
    """PATCH /api/v1/collections/{id}"""

    async def test_update_collection(self, client: AsyncClient) -> None:
        """Updating a collection changes only the specified fields."""
        create = await client.post(
            "/api/v1/collections/",
            json={"name": "Original", "description": "Keep me"},
        )
        col_id = create.json()["id"]
        response = await client.patch(
            f"/api/v1/collections/{col_id}",
            json={"name": "Updated"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Updated"
        assert data["description"] == "Keep me"  # unchanged

    async def test_update_collection_not_found(self, client: AsyncClient) -> None:
        """Updating a non-existent collection returns 404."""
        fake_id = uuid.uuid4()
        response = await client.patch(
            f"/api/v1/collections/{fake_id}",
            json={"name": "Nope"},
        )
        assert response.status_code == 404


class TestCollectionDelete:
    """DELETE /api/v1/collections/{id}"""

    async def test_delete_collection(self, client: AsyncClient) -> None:
        """Deleting a collection returns 204."""
        create = await client.post(
            "/api/v1/collections/",
            json={"name": "Bye"},
        )
        col_id = create.json()["id"]
        response = await client.delete(f"/api/v1/collections/{col_id}")
        assert response.status_code == 204

    async def test_delete_collection_not_found(self, client: AsyncClient) -> None:
        """Deleting a non-existent collection returns 404."""
        fake_id = uuid.uuid4()
        response = await client.delete(f"/api/v1/collections/{fake_id}")
        assert response.status_code == 404
