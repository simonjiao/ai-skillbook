---
title: "Eval Feedback Loop Rules"
type: reference
status: draft
tags: [rules, eval, feedback, quality, governance]
updated: "2026-05-24"
---

# Eval Feedback Loop Rules

This is a sanitized rule extraction from private project notes. Source-specific names, paths, hostnames, examples, and identifiers have been removed.

## Case Generation Rules

- Do not rely only on hand-written cases. Use seed data, question templates, quality rules, and runtime checks to generate repeatable coverage.
- Keep seed data separate from question templates and quality rules.
- Include positive, negative, relation, follow-up, alias, boundary, and privacy-leak cases when the system handles conversational or knowledge-grounded answers.
- First batches should prioritize high-quality, explainable, reproducible cases over large volume.
- Generated cases should be explicit about expected intent, required retrieval or tool behavior, expected answer shape, and forbidden output.

## Runtime Collection Rules

- Eval runs should collect the final answer plus enough trace, package, reviewer, retrieval, and quality observations to explain failures.
- The first version of a conversation eval loop should write artifacts and reports, not automatically modify code or submit governance tasks.
- Remote or live eval runners should not guess deployment targets. Required host, project, environment, or transport inputs should be explicit.
- Store run outputs under generated artifact directories and avoid committing raw transcripts unless they have been intentionally scrubbed for public use.

## Quality Gates

- Deterministic checks should catch internal template leakage, raw path leakage, markup leakage, evidence dumping, missing retrieval, missing review, and failure to answer the actual question.
- Semantic checks should catch unsupported assertions, false certainty, answer drift, relation confusion, and failure to distinguish source facts from inference.
- Human or expert sampling should focus on failure clusters, boundary clusters, and confident answers with thin evidence.
- Quality thresholds should be explicit. Examples include zero internal-template leaks, zero raw evidence dumps, required retrieval for relation questions, and no fabrication for negative cases.

## Failure Taxonomy

Use stable failure tags so fixes can be grouped and regression-tested.

- `intent_misclassified`
- `followup_subject_lost`
- `alias_expansion_missing`
- `retrieval_not_triggered`
- `evidence_not_hit`
- `answer_renderer_failure`
- `raw_evidence_dump`
- `internal_template_leak`
- `reviewer_missed`
- `unsupported_assertion`
- `privacy_leak`
- `tool_or_trace_missing`

## Feedback Loop Rules

- Eval exists to expose problem clusters, not to maximize case count.
- Every failure should move through attribution, clustering, governance task creation, targeted fix, regression run, and closure.
- Feedback artifacts should separate confirmed failures from suspected failures.
- Do not let LLM-as-judge replace deterministic checks where deterministic checks are available.
- Do not let eval artifacts publish private user text, raw provider output, secrets, internal prompts, private endpoints, or unredacted logs.
- Regression reports should preserve enough structured evidence for future comparison without retaining unnecessary raw private content.
