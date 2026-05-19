# CODEOWNERS Team Reviewer Demo

This repository is intentionally small. It exists to test whether a pull request
that changes team-owned code produces a team reviewer in GitHub webhook payloads.

## Owned Area

The file below is owned by the team configured in `.github/CODEOWNERS`:

- `src/billing/discounts.py`

Create a pull request that changes that file, then inspect the resulting
`pull_request` webhook payload. Team ownership should appear through requested
teams, not only requested individual reviewers.
