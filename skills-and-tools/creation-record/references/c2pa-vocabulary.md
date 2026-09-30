# C2PA Vocabulary Reference

This file covers key C2PA assertion types and vocabulary for use in machine-readable creation records.
Reference: https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html

---

## Key Assertion Types

### `c2pa.ai.generatedContent`
Asserts that content was generated or substantially modified by an AI system.

Fields:
- `model_id`: Identifier for the AI model used
- `model_version`: Version string if known
- `provider`: Organization providing the AI service
- `role`: One of `produced_by`, `edited_by`, `assisted_by`, `reviewed_by`
- `prompt_summary`: Optional summary of how the AI was directed

### `c2pa.ai.training`
Asserts what training data an AI model was trained on (rarely relevant for disclosure statements, but noted here for completeness).

### `c2pa.creative.work`
Describes the nature of the creative or informational work.

Fields:
- `type`: One of `text`, `code`, `image`, `video`, `audio`, `data`, `presentation`, `mixed`
- `title`: Title or description of the work

### `c2pa.human.review`
Asserts that a human reviewed and/or modified the AI output.

Fields:
- `reviewer`: Name or role of reviewer
- `action`: One of `reviewed`, `approved`, `revised`, `fact-checked`
- `revision_extent`: One of `none`, `minor`, `moderate`, `substantial`, `complete-rewrite`

---

## Role Vocabulary

Use these values for `c2pa:role` in AI contribution assertions:

| Role | When to Use |
|---|---|
| `produced_by` | AI generated the primary content |
| `drafted_by` | AI created an initial draft that humans then revised |
| `assisted_by` | AI contributed to specific parts of human-led creation |
| `edited_by` | AI made edits to human-created content |
| `reviewed_by` | AI reviewed but did not modify the content |
| `summarized_by` | AI created a summary of source material |
| `translated_by` | AI translated content between languages |
| `coded_by` | AI wrote or completed code |

---

## Contribution Materiality

C2PA calls for indicating how material the AI contribution was. Map contribution labels to C2PA materiality values. Note: the label numbers are internal framework references only and should not appear in disclosure outputs.

| Label | C2PA Materiality |
|---|---|
| AI-Produced | `primary` |
| AI-Produced, Extensively Directed | `primary` |
| AI-Drafted, Human-Revised | `substantial` |
| AI-Assisted | `moderate` |
| AI-Supported | `minor` |
| Human-Created, AI-Reviewed | `incidental` |

## Prompt Characterization Vocabulary

The `c2pa:promptCharacterization` field describes how the AI was directed. Use these values:

| Value | Description |
|---|---|
| `single-brief-prompt` | One short, general request with minimal constraints |
| `structured-prompt` | Single detailed request with explicit constraints, format, audience, or source material |
| `iterative-prompting` | Multiple exchanges refining output, without substantial original intellectual input from human |
| `expert-directed-iterative-prompting` | Multiple exchanges in which human contributed domain knowledge, original arguments, or specific factual material |
| `iterative-with-human-source-material` | Human provided documents, data, or prior writing that the AI synthesized |

---

## Known Model Identifiers

Common values for `c2pa:model` — record the actual model used, regardless of provider.
Examples for common providers:

```json
{
  "c2pa:name": "Claude",
  "c2pa:version": "claude-sonnet-4-6",
  "c2pa:provider": "Anthropic"
}
```

```json
{
  "c2pa:name": "Codex",
  "c2pa:version": "gpt-5.x",
  "c2pa:provider": "OpenAI"
}
```

Note: The exact model version is often unavailable to users of the platform. If unknown, use:
```json
{
  "c2pa:name": "Claude",
  "c2pa:version": null,
  "c2pa:provider": "Anthropic",
  "c2pa:versionNote": "version not specified by platform"
}
```

---

## W3C PROV Integration

For richer provenance, the JSON-LD record can include W3C PROV-O terms:

```json
{
  "prov:wasGeneratedBy": {
    "@type": "prov:Activity",
    "prov:startedAtTime": "2025-06-04T00:00:00Z",
    "prov:wasAssociatedWith": {
      "@type": "prov:SoftwareAgent",
      "schema:name": "Claude",
      "schema:provider": "Anthropic"
    }
  },
  "prov:wasAttributedTo": {
    "@type": "prov:Person",
    "schema:name": "[Human author/reviewer name or role]"
  }
}
```

---

## Schema.org Alignment

For web publishing contexts, `schema:CreativeWork` properties can supplement C2PA:

```json
{
  "@type": "schema:CreativeWork",
  "schema:author": { "@type": "schema:Person", "schema:name": "[author]" },
  "schema:contributor": {
    "@type": "schema:SoftwareApplication",
    "schema:name": "Claude",
    "schema:applicationCategory": "GenerativeAI"
  },
  "schema:dateCreated": "[ISO date]",
  "schema:usageInfo": "[link to disclosure page if applicable]"
}
```
