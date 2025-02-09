# 5. commit adr records to git before implementation

Date: 2025-02-04

## Status

Accepted

## Context

To ensure transparency, accountability, and maintainability in our Python applications, it is essential to commit ADR documents to version control systems like Git before their implementation.
This decision helps us establish a clear audit trail of our design choices and provides future developers with valuable context for understanding our system's architecture.
In addition, committing ADRs to Git ensures that we can track changes in the system and identify areas for improvement over time.
By making this process explicit, we can also facilitate collaboration among team members and promote a culture of iterative development and continuous learning.

## Decision

From now on, every ADR document must be committed to the repository with the commit message prefixed with the string 'adr:'
The commit message should closely reflect the title and filename of the decision record.
This will facilitate searching the git repo for commits associated with a specific ADR.
i.e. when working on a feature branch the first commit of the branch should be the ADR document commit including no other changes.
if squash merging feature branches the final git commit message should be the ADR commit message.

## Consequences

Committing ADRs to Git before implementation allows us to maintain a historical record of our design evolution, which can be beneficial when:

* Onboarding new team members who need to understand the current system architecture
* Resolving support requests or addressing technical debt related to legacy code
* Evaluating changes and making informed decisions about future development cycles

By consistently using this convention, we can increase transparency, facilitate collaboration, and build a more maintainable and adaptable software application.
