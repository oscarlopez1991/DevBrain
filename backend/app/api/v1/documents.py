"""
Documents API router — CRUD endpoints for documents.

TODO(PHASE-1): Implement the body of each endpoint.
The router structure, dependencies, and response models are provided.
You wire them to DocumentService methods.

Run: make verify-phase1
"""

import uuid
from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.document import DocumentCreate, DocumentRead, DocumentUpdate
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["documents"])


def _get_service(db: AsyncSession = Depends(get_db)) -> DocumentService:
    return DocumentService(db)


@router.get("/", response_model=list[DocumentRead])
async def list_documents(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    service: DocumentService = Depends(_get_service),
) -> Sequence[DocumentRead]:
    """List all documents with pagination."""

    documents = await service.list_documents(skip=skip, limit=limit)
    return [DocumentRead.model_validate(c) for c in documents]


@router.get("/{document_id}", response_model=DocumentRead)
async def get_document(
    document_id: uuid.UUID,
    service: DocumentService = Depends(_get_service),
) -> DocumentRead:
    """Get a single document by ID."""

    document = await service.get_document(document_id)

    if document is None:
        raise HTTPException(status_code=404, detail="Document don't found")

    document_read = DocumentRead.model_validate(document)
    return document_read


@router.post("/", response_model=DocumentRead, status_code=201)
async def create_document(
    data: DocumentCreate,
    service: DocumentService = Depends(_get_service),
) -> DocumentRead:
    """Create a new document."""

    document_created = await service.create_document(data)
    document_read = DocumentRead.model_validate(document_created)
    return document_read


@router.patch("/{document_id}", response_model=DocumentRead)
async def update_document(
    document_id: uuid.UUID,
    data: DocumentUpdate,
    service: DocumentService = Depends(_get_service),
) -> DocumentRead:
    """Update a document. Partial updates supported."""

    document_updated = await service.update_document(document_id, data)

    if document_updated is None:
        raise HTTPException(status_code=404, detail="Document don't found")

    document_read = DocumentRead.model_validate(document_updated)
    return document_read


@router.delete("/{document_id}", status_code=204)
async def delete_document(
    document_id: uuid.UUID,
    service: DocumentService = Depends(_get_service),
) -> None:
    """Delete a document."""

    result = await service.delete_document(document_id)

    if not result:
        raise HTTPException(status_code=404, detail="Document don't found")

    return None
