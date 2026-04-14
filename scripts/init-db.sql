-- ━━━ LEARN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- Database Initialization Script
--
-- This script runs ONCE when the PostgreSQL container is first created.
-- It enables the extensions we need for DevBrain.
--
-- pgvector: Adds vector data type and similarity search operators
--   - Stores AI embeddings (dense numeric arrays)
--   - Enables cosine similarity, L2 distance, inner product searches
--   - Works with standard SQL queries
--
-- Compare with ASP.NET / SQL Server:
--   In SQL Server, you might need a separate vector database.
--   With pgvector, everything stays in PostgreSQL — simpler architecture.
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

-- Enable the pgvector extension for vector similarity search
-- This adds the `vector` data type and operators like <=> (cosine distance)
CREATE EXTENSION IF NOT EXISTS vector;

-- Enable the pg_trgm extension for trigram-based text search
-- This will be used for BM25/keyword search in the hybrid search pipeline
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Enable uuid-ossp for generating UUIDs as primary keys
-- UUIDs are better than auto-increment IDs for distributed systems
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
