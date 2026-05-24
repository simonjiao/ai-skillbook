---
title: "Context And Memory Privacy Rules"
type: reference
status: draft
tags: [rules, context, memory, privacy, safety]
updated: "2026-05-24"
---

# Context And Memory Privacy Rules

This is a sanitized rule extraction from private project notes. Source-specific names, paths, hostnames, examples, and identifiers have been removed.

## Context Scope

- Treat the current conversation window as a request-level input, not as long-term memory and not as evidence.
- Build a bounded context package for audit and replay, then project only the role-specific subset each agent needs.
- Agent-facing context should be narrower than operator-facing audit context.
- Retrieval and specialist agents should receive a validated question plus scoped retrieval parameters, not the full conversation history.
- Answer composers may use a compact intent summary for phrasing and clarification, but not as factual evidence.
- Reviewers may use compact intent context to detect wrong target, drift, or internal-field leakage, but not to invent missing evidence.

## Compression Rules

- Context compression is a controlled step, not a free-form summary.
- Compressors should extract only from their input window and attach source references to every retained item.
- A compressor must not add entities, sources, conclusions, evidence, retrieval queries, final answers, or reviewer decisions that were not present in the input.
- If the compressed context is partial, invalid, rejected, or timed out, the main path should clarify or fail closed rather than continuing with untrusted context.
- Do not silently drop important information when the context window exceeds budget. Record what was omitted, why, and how the system handled the omission.

## Memory Rules

- Long-term memory should be produced through explicit policy, scope, access control, lifecycle, and audit paths.
- Memory can represent preferences, background, working style, and long-term context summaries. It should not become a source of factual evidence.
- Memory must not replace source evidence, close tasks, confirm approvals, change reviewer decisions, or override explicit current-window facts.
- Low-confidence or older memory should not override high-confidence current-window context.
- Memory access should be fail-closed when scope, user, profile, policy, or access control does not match.
- Revoked, expired, legally held, or disabled memory must stop appearing in new context packages immediately.

## Privacy Rules

- Do not expose raw provider output, system prompts, private memory, raw journals, full transcripts, internal drafts, reviewer notes, or audit internals in public responses.
- Metrics and ordinary logs should avoid raw user text, high-cardinality IDs, private memory IDs, trace internals, and provider payloads.
- Public responses should not leak candidate pools, rule IDs, internal context identifiers, prompt fragments, or raw retrieval internals.
- Export, anonymization, legal hold, backup, and restore behavior should cover context records, journals, memory candidates, memory cards, policy decisions, and audit chains.
- Credentials must not be passed through command-line arguments or printed in logs. Use environment files, secret providers, or operator-managed secret paths.

## Validation Rules

- Validate that a resolved question is non-empty before retrieval.
- Validate that any referent binding comes from the current window, an allowed candidate pool, or an explicitly referenced prior context.
- Require clarification text when the system decides clarification is needed.
- Reject outputs that contain forbidden fields or raw provider output.
- Record candidate source, confidence, rule identifier, and rule catalog version in audit logs, while keeping those details out of public responses.
