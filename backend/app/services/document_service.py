"""
Document service — Business logic for document operations.

TODO(PHASE-1): Implement all methods in this service.
Each method signature and docstring tells you WHAT it should do.
The verification tests define the expected behavior.

Run: make verify-phase1
"""

import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentUpdate


class DocumentService:
    """Handles all document-related business logic."""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def list_documents(self, *, skip: int = 0, limit: int = 20) -> list[Document]:
        """
        Return a paginated list of documents, ordered by created_at desc.

        TODO(PHASE-1): Implement this method.
        - Use select(Document) with .offset(skip).limit(limit)
        - Order by created_at descending (newest first)
        - Return the list (empty list if no documents, NOT None)
        """
        raise NotImplementedError

    async def get_document(self, document_id: uuid.UUID) -> Document | None:
        """
        Return a single document by ID, or None if not found.

        TODO(PHASE-1): Implement this method.
        - Use session.get() or select() with a where clause
        """
        raise NotImplementedError

    async def create_document(self, data: DocumentCreate) -> Document:
        """
        Create a new document and return it.

        TODO(PHASE-1): Implement this method.
        - Create a Document instance from the schema data
        - Add it to the session and flush to get the generated ID
        - Refresh the instance to load server defaults (timestamps)
        - Return the created document
        """
        raise NotImplementedError

    async def update_document(
        self, document_id: uuid.UUID, data: DocumentUpdate
    ) -> Document | None:
        """
        Update an existing document. Return the updated document or None if not found.

        TODO(PHASE-1): Implement this method.
        - Fetch the document by ID
        - If not found, return None
        - Apply only the fields that were explicitly set
          (use data.model_dump(exclude_unset=True))
        - Flush and refresh
        - Return the updated document
        """
        raise NotImplementedError

    async def delete_document(self, document_id: uuid.UUID) -> bool:
        """
        Delete a document by ID. Return True if deleted, False if not found.

        TODO(PHASE-1): Implement this method.
        - Fetch the document by ID
        - If not found, return False
        - Delete it from the session
        - Return True
        """
        raise NotImplementedError
