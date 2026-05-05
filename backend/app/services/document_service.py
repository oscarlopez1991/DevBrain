"""
Document service — Business logic for document operations.

TODO(PHASE-1): Implement all methods in this service.
Each method signature and docstring tells you WHAT it should do.
The verification tests define the expected behavior.

Run: make verify-phase1
"""

import uuid
from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentUpdate


class DocumentService:
    """Handles all document-related business logic."""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def list_documents(
        self, *, skip: int = 0, limit: int = 20
    ) -> Sequence[Document]:
        """Return a paginated list of documents, ordered by created_at desc."""

        stmt = (
            select(Document)
            .order_by(Document.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        result = await self.db.execute(stmt)

        return result.scalars().all()

    async def get_document(self, document_id: uuid.UUID) -> Document | None:
        """Return a single document by ID, or None if not found."""

        document = await self.db.get(Document, document_id)
        return document

    async def create_document(self, data: DocumentCreate) -> Document:
        """Create a new document and return it."""

        new_document = Document(**data.model_dump())

        self.db.add(new_document)
        await self.db.flush()
        await self.db.refresh(new_document)

        return new_document

    async def update_document(
        self, document_id: uuid.UUID, data: DocumentUpdate
    ) -> Document | None:
        """Update an existing document.
        Return the updated document or None if not found."""

        document = await self.db.get(Document, document_id)

        if document is None:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(document, key, value)

        await self.db.flush()
        await self.db.refresh(document)

        return document

    async def delete_document(self, document_id: uuid.UUID) -> bool:
        """Delete a document by ID. Return True if deleted, False if not found."""

        document = await self.db.get(Document, document_id)

        if document is None:
            return False

        await self.db.delete(document)
        await self.db.flush()

        return True
