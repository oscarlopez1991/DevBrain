"""Pydantic schemas for Document and Collection API validation."""

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.document import DocumentStatus

# ──────────────────────────────────────────────────────────────
# Collection Schemas
# ──────────────────────────────────────────────────────────────


class CollectionCreate(BaseModel):
    """Schema for creating a new collection."""

    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = Field(None, max_length=2000)


class CollectionUpdate(BaseModel):
    """Schema for updating a collection. All fields optional."""

    name: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, max_length=2000)


class CollectionRead(BaseModel):
    """Schema for reading a collection (API response)."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime


# ──────────────────────────────────────────────────────────────
# Document Schemas
# ──────────────────────────────────────────────────────────────


class DocumentCreate(BaseModel):
    """Schema for creating a new document."""

    title: str = Field(..., min_length=1, max_length=500)
    filename: str = Field(..., min_length=1, max_length=500)
    content_type: str = Field(..., min_length=1, max_length=100)
    file_size: int = Field(0, ge=0)
    status: DocumentStatus = DocumentStatus.DRAFT
    content_text: str | None = None
    collection_id: uuid.UUID | None = None


class DocumentUpdate(BaseModel):
    """Schema for updating a document. All fields optional."""

    title: str | None = Field(None, min_length=1, max_length=500)
    status: DocumentStatus | None = None
    content_text: str | None = None
    collection_id: uuid.UUID | None = None


class DocumentRead(BaseModel):
    """Schema for reading a document (API response)."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    filename: str
    content_type: str
    file_size: int
    status: DocumentStatus
    content_text: str | None
    collection_id: uuid.UUID | None
    created_at: datetime
    updated_at: datetime
