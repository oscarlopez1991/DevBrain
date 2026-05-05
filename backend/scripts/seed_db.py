import asyncio


from sqlalchemy import delete
from app.core.database import async_session_factory
from app.models.document import Collection, Document, DocumentStatus

async def seed_data() -> None:
    print("🌱 Starting database seeding...")
    
    async with async_session_factory() as session:
        # 1. Clean existing data (so we don't get duplicates if we run this multiple times)
        print("🧹 Cleaning old data...")
        await session.execute(delete(Document))
        await session.execute(delete(Collection))
        
        # 2. Create mock Collections
        print("📁 Creating collections...")
        col1 = Collection(name="Python Architecture", description="Best practices for Python backends")
        col2 = Collection(name="Frontend Foundations", description="React and Next.js resources")
        
        session.add_all([col1, col2])
        # We flush to send them to the DB immediately so they get assigned UUIDs
        await session.flush() 
        
        # 3. Create mock Documents linked to those collections
        print("📄 Creating documents...")
        docs = [
            Document(
                title="FastAPI Guide",
                filename="fastapi_guide.md",
                content_type="text/markdown",
                file_size=1024,
                status=DocumentStatus.READY,
                collection_id=col1.id,
                content_text="# FastAPI\nFastAPI is a modern web framework..."
            ),
            Document(
                title="Next.js App Router",
                filename="nextjs.pdf",
                content_type="application/pdf",
                file_size=2048576,
                status=DocumentStatus.PROCESSING,
                collection_id=col2.id,
                content_text="App Router introduces a new paradigm..."
            ),
            Document(
                title="Docker Compose Mastery",
                filename="docker-compose.yml",
                content_type="text/yaml",
                file_size=512,
                status=DocumentStatus.DRAFT,
                collection_id=None,
                content_text="version: '3.8'\nservices:..."
            )
        ]
        
        session.add_all(docs)
        
        # 4. Commit all changes to the database
        await session.commit()
        
        print(f"✅ Seeding complete! Created 2 Collections and {len(docs)} Documents.")

if __name__ == "__main__":
    # In Python 3.10+, this is the standard way to run an async function from a script
    asyncio.run(seed_data())
