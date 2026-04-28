"""
Collection service — Business logic for collection operations.

TODO(PHASE-1): Implement all methods in this service.
Each method signature and docstring tells you WHAT it should do.
The verification tests define the expected behavior.

Run: make verify-phase1
"""

import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Collection
from app.schemas.document import CollectionCreate, CollectionUpdate


class CollectionService:
    """Handles all collection-related business logic."""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def list_collections(self, *, skip: int = 0, limit: int = 20) -> Sequence[Collection]:
        """ Return a paginated list of collections, ordered by created_at desc. """

        stmt = select(Collection).order_by(Collection.created_at.desc()).offset(skip).limit(limit)
        result = await self.db.execute(stmt)

        return result.scalars().all()

    async def get_collection(self, collection_id: uuid.UUID) -> Collection | None:
        """ Return a single collection by ID, or None if not found. """

        result = await self.db.get(Collection, collection_id)
        return result # type: ignore

    async def create_collection(self, data: CollectionCreate) -> Collection:
        """ Create a new collection and return it. """

        new_collection = Collection(**data.model_dump())

        self.db.add(new_collection)
        await self.db.flush()
        await self.db.refresh(new_collection)

        return new_collection

    async def update_collection(self, collection_id: uuid.UUID, data: CollectionUpdate) -> Collection | None:
        """ Update an existing collection. Return updated or None if not found. """

        collection = await self.db.get(Collection, collection_id)

        if collection is None:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(collection, key, value)

        await self.db.flush()
        await self.db.refresh(collection)

        return collection # type: ignore

    async def delete_collection(self, collection_id: uuid.UUID) -> bool:
        """ Delete a collection by ID. Return True if deleted, False if not found. """

        collection = await self.db.get(Collection, collection_id)

        if collection is None:
            return False

        await self.db.delete(collection)
        await self.db.flush()

        return True
