# 2. utilize system environment variables for secrets

Date: 2025-02-04

## Status

Accepted

## Context

Applications require secure management of secrets such as API keys, database credentials, and encryption keys.
Storing secrets in configuration files or source code increases security risks.
A solution is needed to ensure secrets are managed securely and remain separate from the application code.

## Decision

We have decided to use system environment variables for configuring secrets.
This approach keeps sensitive information out of version control and reduces exposure risk.
It also integrates well with containerized and cloud-based deployments.

## Consequences

Secrets management becomes dependent on the hosting environment’s configuration.
Developers must ensure environment variables are properly set and secured.
Additional tooling may be required for managing secrets in different deployment environments.
