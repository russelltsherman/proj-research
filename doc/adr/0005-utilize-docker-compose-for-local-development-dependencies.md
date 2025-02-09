# 2. utilize docker compose for local development dependencies

Date: 2025-02-04

## Status

Accepted

## Context

Modern software development often requires multiple services, such as databases, message brokers, and caching layers, to be available for local development.
Managing these dependencies manually can be time-consuming and error-prone.
A solution is needed to standardize development environments, simplify dependency management, and facilitate efficient onboarding of project participants.

## Decision

We will use Docker Compose to define and run local development dependencies.
This ensures consistency across development environments and simplifies setup.
Developers can start all required services with a single command (docker-compose up).

## Consequences

Developers must install Docker and Docker Compose.
There may be an initial learning curve for those unfamiliar with containerization.
Workstation resource requirements will be greater compared to utilizing hosted services.
