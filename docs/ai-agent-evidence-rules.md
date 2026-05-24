---
title: "AI Agent Evidence Rules"
type: reference
status: draft
tags: [rules, agents, evidence, safety]
updated: "2026-05-24"
---

# AI Agent Evidence Rules

This is a sanitized rule extraction from private project notes. Source-specific names, paths, hostnames, examples, and identifiers have been removed.

## Core Rules

- Put evidence before expression. Complex answers should be assembled from verified evidence first, then rendered for the user.
- When evidence is missing, say that the evidence is missing. Do not use model memory, broad priors, or plausible narrative to fill the gap.
- Keep evidence layers separate. Direct source facts, commentary, version differences, user-provided context, and model inference should not collapse into one undifferentiated claim.
- Every substantial claim should have a support boundary: what it supports, what it does not support, and what remains uncertain.
- A summary can help retrieval or orientation, but it is not a citable source unless the summary itself is the object being evaluated.
- The final user-facing answer should not expose internal evidence IDs, source paths, raw traces, reviewer records, or template text.

## Agent Boundary Rules

- Protocol adapters and gateways should coordinate flow, security, policy, and audit. They should not become hidden answer-generation agents.
- Each agent should receive only the tools and context needed for its role.
- Retrieval agents retrieve; review agents review; answer composers render. Avoid role drift where one component quietly does another component's job.
- Internal specialist agents, reviewer profiles, and routing plans should not be exposed as user-facing product choices unless the product explicitly supports that.
- Unknown consumer, tool, runtime, or policy combinations should fail closed with an auditable reason instead of mapping to a default profile.

## Fallback And Degraded Path Rules

- Fallback is not forbidden, but it cannot count as primary-path success.
- A degraded path must produce an explicit status, audit event, metric, report field, or user-visible limitation.
- A mock, replay, default-empty value, old code path, or local no-upstream path must identify itself in the returned type, report, log, or fixture name.
- Release or readiness language should distinguish design alignment, local implementation, target-environment validation, and production-ready evidence.
- Do not declare production-ready from documentation, unit tests, local smoke tests, or one successful replay alone.

## Implementation Rules

- Prefer typed domain contracts over ad hoc JSON, stringly typed state, and vague common helpers.
- Keep production behavior explicit: trace IDs, audit records, idempotency keys, ownership leases, policy decisions, and degraded states should remain observable.
- Reuse after the third repeated pattern. If handlers, DTO mapping, config loading, audit append logic, or test fixtures repeat more than twice, introduce a local helper, builder, trait, or template.
- Templates must preserve domain boundaries. They should not hide lifecycle state, policy decisions, trace identity, ownership, or audit decisions behind generic helper names.
- User-visible errors should expose stable error codes and correlation IDs, not raw database, provider, token, network, or secret-bearing strings.

## Verification Rules

- Design that cannot be verified should not be treated as ready for implementation.
- Tests for fallback or degraded behavior should prove both sides: the primary path passes when dependencies are healthy, and the degraded path is explicitly observable when dependencies fail.
- Broaden verification when shared models, public contracts, lifecycle behavior, concurrency, security, or release gates change.
- Keep evidence for readiness concrete: command output, report path, artifact digest, status field, commit hash, target-environment proof, or audited trace.
