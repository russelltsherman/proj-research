# 6. Implement Timescaledb with pgvectorscale and pgai Extensions for Time Series DataStorage

Date: 2025-02-04

## Status

Accepted

## Context

Many llm agentic workflows may want to make use of vector data stores to facilitate specialization of agents knowledge base.
Our application will require a scalable, high-performance time-series database with vector search capabilities for AI-driven analytics.
TimescaleDB, an extension of PostgreSQL, offers efficient time-series data handling, while VectorScale enhances vector search performance.
The pgAI extension provides built-in AI/ML functions, reducing external dependencies and improving query efficiency.
A unified database solution simplifies infrastructure and reduces operational complexity.  

## Decision

We will use TimescaleDB as our primary database, leveraging its time-series optimizations for efficient data ingestion and querying.
VectorScale will be added to support high-performance vector search, enabling fast similarity searches for AI-driven features.
The pgAI extension will be included to perform AI/ML operations directly within the database, reducing data movement overhead.
This approach ensures a seamless integration of time-series, vector, and AI functionalities within a single PostgreSQL-compatible system.  

## Consequences

This decision simplifies architecture by consolidating multiple functionalities within a single database, reducing the need for additional vector databases like Pinecone or FAISS.
Query performance benefits from PostgreSQL’s indexing and optimization features, but careful tuning may be required for large-scale workloads.
The reliance on TimescaleDB and its extensions introduces a dependency on Timescale’s ecosystem, which may impact long-term flexibility. Future scalability considerations may require partitioning strategies and infrastructure optimizations.  
