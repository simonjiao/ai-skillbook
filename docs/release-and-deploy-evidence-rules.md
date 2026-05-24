---
title: "Release And Deploy Evidence Rules"
type: reference
status: draft
tags: [rules, deploy, release, scripts, evidence, privacy]
updated: "2026-05-24"
---

# Release And Deploy Evidence Rules

This is a sanitized rule extraction from private project notes. Source-specific names, paths, hostnames, examples, and identifiers have been removed.

## Script Rules

- Persist every script that participates in deploy, rollback, preflight, post-deploy verification, release gates, version checks, remote state proof, or repeated operator maintenance.
- Temporary probes are fine for exploration, but their output should not become durable release evidence until the check is moved into a maintained script or runbook.
- Prefer improving an existing deploy, verify, or reconcile entrypoint before adding a new script with overlapping behavior.
- Shared path, environment, artifact, remote execution, redaction, and compose/rendering logic should live in helper libraries.
- Generated artifacts should live under ignored artifact directories, not in tracked source or docs.

## Shell And CLI Rules

- Shell scripts should use Bash with strict mode unless a narrower runtime requires otherwise.
- Avoid shell-specific syntax unless the script checks or documents the required shell version.
- Quote variable expansions unless word splitting is intentional.
- Prefer arrays for local command construction and maintained remote scripts over deeply nested quoting.
- Machine-consumed gates should emit stable key-value or JSON-like evidence. Human progress text is not enough.
- Deploy, verify, reconcile, and install entrypoints should provide `--help`.
- Complex or destructive scripts should support dry-run, preflight, or contract-test coverage.
- Scripts should be idempotent where possible. Re-running a verification or reconcile step must not corrupt state.

## Environment And Secret Rules

- Preserve the boundary between tracked templates, local operator configuration, remote deploy artifacts, and temporary deploy-time overrides.
- Do not treat a remote environment file as the source of truth for tracked repository behavior.
- Never print secrets, tokens, API keys, cookies, private keys, provider keys, or full secret-bearing environment lines.
- Keep redaction centralized when scripts read environment files, logs, reports, exported app state, or remote command output.
- Version and release scripts must not print token, key, or password values.

## Version Rules

- Keep one explicit version source of truth for a project or release unit.
- Use a single source-owned version bump for changes that affect build output, runtime behavior, local orchestration, deployable assets, or release evidence.
- Use a broader version bump for large features, cross-module behavior changes, runtime contract changes, schema changes, architecture refactors, or deployment boundary changes.
- Do not split one coherent feature into multiple narrow bumps just to avoid acknowledging a broader release boundary.
- Keep package metadata, lock files, container labels, compose defaults, scripts, tests, and release evidence synchronized with the source version.

## Deploy Evidence Rules

- A healthy remote process or container is not enough to prove the maintained deploy path.
- Deployment evidence should show that the maintained deploy entrypoint produced or verified the target state.
- Release proof should distinguish local rendered configuration, uploaded remote configuration, effective image reference, running image identity, version label or build metadata, live gate artifacts, and saved readiness report.
- Fallback, mock, replay, local no-upstream, and default-empty paths should be reported as degraded or non-production evidence unless the primary path also ran and passed.
- Missing tools, credentials, remote services, or source checkouts should produce `BLOCKED`, non-production status, or a release blocker. Do not convert missing prerequisites into a green result.
- Stale image references, stale version environment values, or manual overrides must not silently override the intended release version.

## Report Rules

- Release reports should keep production-ready flags derived from validated gates, not hand-edited status fields.
- Reports should reject secret-like values, raw user questions, high-cardinality ID lists, unbounded logs, and stale gate evidence.
- Browser or UI validation should be bound to saved evidence, canonical checked items, evidence file digests, release references, and public URL or route identity when applicable.
- Security scan status should be bound to the exact release artifact or image reference being shipped.
