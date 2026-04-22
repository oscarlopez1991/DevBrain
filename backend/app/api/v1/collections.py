"""
Collections API router — CRUD endpoints for collections.

TODO(PHASE-1): Implement the body of each endpoint.
Same pattern as the documents router.

Run: make verify-phase1
"""

import uuid

from fastapi import APIRouter, Depends, Query
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
) -> list[CollectionRead]:
    """
    List all collections with pagination.

    TODO(PHASE-1): Call the service and return collections.
    """
    raise NotImplementedError


@router.get("/{collection_id}", response_model=CollectionRead)
async def get_collection(
    collection_id: uuid.UUID,
    service: CollectionService = Depends(_get_service),
) -> CollectionRead:
    """
    Get a single collection by ID.

    TODO(PHASE-1): Call the service, return 404 if not found.
    """
    raise NotImplementedError


@router.post("/", response_model=CollectionRead, status_code=201)
async def create_collection(
    data: CollectionCreate,
    service: CollectionService = Depends(_get_service),
) -> CollectionRead:
    """
    Create a new collection.

    TODO(PHASE-1): Call the service to create and return the collection.
    """
    raise NotImplementedError


@router.patch("/{collection_id}", response_model=CollectionRead)
async def update_collection(
    collection_id: uuid.UUID,
    data: CollectionUpdate,
    service: CollectionService = Depends(_get_service),
) -> CollectionRead:
    """
    Update a collection.

    TODO(PHASE-1): Call the service, return 404 if not found.
    """
    raise NotImplementedError


@router.delete("/{collection_id}", status_code=204)
async def delete_collection(
    collection_id: uuid.UUID,
    service: CollectionService = Depends(_get_service),
) -> None:
    """
    Delete a collection and all its documents.

    TODO(PHASE-1): Call the service, return 404 if not found.
    """
    raise NotImplementedError
