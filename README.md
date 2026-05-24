# ai-skillbook

A public field notebook for practical AI skills, tools, plugins, prompts, workflows, and automations.

The goal is to keep reusable AI operating knowledge in a form that is easy to search, review, and improve over time.

## Structure

- `skills/` - reusable agent or coding-assistant skills.
- `plugins/` - plugin notes, setup guides, and capability maps.
- `tools/` - command-line tools, MCP servers, APIs, and integrations.
- `prompts/` - prompt patterns and prompt-review notes.
- `workflows/` - end-to-end operating workflows.
- `automations/` - recurring checks, monitors, and scheduled tasks.
- `docs/` - taxonomy, review rules, and repository conventions.
- `templates/` - entry templates for new notes.
- `scripts/` - local maintenance helpers.

## Common Commands

```bash
make new TYPE=tool SLUG=example-tool TITLE="Example Tool"
make catalog
make check
```

## Entry Format

Each note should start with a small YAML front matter block:

```yaml
---
title: Example
type: tool
status: draft
tags: [ai, cli]
updated: 2026-05-24
---
```

Keep entries evidence-based: describe what worked, what failed, where it applies, and what should be verified before reuse.
