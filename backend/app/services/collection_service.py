"""
Collection service — Business logic for collection operations.

TODO(PHASE-1): Implement all methods in this service.
Each method signature and docstring tells you WHAT it should do.
The verification tests define the expected behavior.

Run: make verify-phase1
"""

import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Collection
from app.schemas.document import CollectionCreate, CollectionUpdate


class CollectionService:
    """Handles all collection-related business logic."""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def list_collections(
        self, *, skip: int = 0, limit: int = 20
    ) -> list[Collection]:
        """
        Return a paginated list of collections, ordered by created_at desc.

        TODO(PHASE-1): Implement this method.
        """
        raise NotImplementedError

    async def get_collection(self, collection_id: uuid.UUID) -> Collection | None:
        """
        Return a single collection by ID, or None if not found.

        TODO(PHASE-1): Implement this method.
        """
        raise NotImplementedError

    async def create_collection(self, data: CollectionCreate) -> Collection:
        """
        Create a new collection and return it.

        TODO(PHASE-1): Implement this method.
        """
        raise NotImplementedError

    async def update_collection(
        self, collection_id: uuid.UUID, data: CollectionUpdate
    ) -> Collection | None:
        """
        Update an existing collection. Return updated or None if not found.

        TODO(PHASE-1): Implement this method.
        """
        raise NotImplementedError

    async def delete_collection(self, collection_id: uuid.UUID) -> bool:
        """
        Delete a collection by ID. Return True if deleted, False if not found.

        TODO(PHASE-1): Implement this method.
        """
        raise NotImplementedError
