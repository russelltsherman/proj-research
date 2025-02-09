# 2. utilize direnv for automating local virtual environment loading

Date: 2025-02-04

## Status

Accepted

## Context

Managing environment variables and virtual environments manually can be cumbersome and error-prone.
Developers often need to activate virtual environments and set environment variables when switching between projects.
Automating this process improves efficiency and reduces the likelihood of misconfiguration.

## Decision

We have decided to use direnv to automatically load virtual environments and environment variables for local development.
direnv allows for seamless project-specific environment management by automatically applying configurations defined in .envrc files.
This approach simplifies workflow and reduces setup overhead.

## Consequences

Developers must install and configure direnv on their machines.
Properly setting up .envrc files becomes essential to ensure correct environment configurations.
This decision improves development efficiency but may require initial learning and setup effort.
