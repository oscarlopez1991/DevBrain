"""
Collections API router — CRUD endpoints for collections.

TODO(PHASE-1): Implement the body of each endpoint.
Same pattern as the documents router.

Run: make verify-phase1
"""

import uuid
from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.document import CollectionCreate, CollectionRead, CollectionUpdate
from app.services.collection_service import CollectionService

router = APIRouter(prefix="/collections", tags=["collections"])


def _get_service(db: AsyncSession = Depends(get_db)) -> CollectionService:
    return CollectionService(db)


@router.get("/", response_model=list[CollectionRead])
async def list_collections(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    service: CollectionService = Depends(_get_service),
) -> Sequence[CollectionRead]:
    """List all collections with pagination."""

    collections = await service.list_collections(skip=skip, limit=limit)
    return [CollectionRead.model_validate(c) for c in collections]


@router.get("/{collection_id}", response_model=CollectionRead)
async def get_collection(
    collection_id: uuid.UUID,
    service: CollectionService = Depends(_get_service),
) -> CollectionRead:
    """Get a single collection by ID."""

    collection = await service.get_collection(collection_id)

    if not collection:
        raise HTTPException(status_code=404, detail="Collection don't found")

    collection_read = CollectionRead.model_validate(collection)
    return collection_read


@router.post("/", response_model=CollectionRead, status_code=201)
async def create_collection(
    data: CollectionCreate,
    service: CollectionService = Depends(_get_service),
) -> CollectionRead:
    """Create a new collection."""

    collection_created = await service.create_collection(data)
    collection_read = CollectionRead.model_validate(collection_created)
    return collection_read


@router.patch("/{collection_id}", response_model=CollectionRead)
async def update_collection(
    collection_id: uuid.UUID,
    data: CollectionUpdate,
    service: CollectionService = Depends(_get_service),
) -> CollectionRead:
    """Update a collection."""

    collection_updated = await service.update_collection(collection_id, data)

    if not collection_updated:
        raise HTTPException(status_code=404, detail="Collection don't found")

    collection_read = CollectionRead.model_validate(collection_updated)
    return collection_read


@router.delete("/{collection_id}", status_code=204)
async def delete_collection(
    collection_id: uuid.UUID,
    service: CollectionService = Depends(_get_service),
) -> None:
    """Delete a collection and all its documents."""

    result = await service.delete_collection(collection_id)

    if not result:
        raise HTTPException(status_code=404, detail="Collection don't found")

    return None
