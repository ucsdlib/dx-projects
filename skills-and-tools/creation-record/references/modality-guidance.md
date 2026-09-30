# Modality-Specific Guidance

This file provides tailored guidance for non-text modalities: **code**, **images**, and
**audio/video**. For text/writing (articles, reports, emails, policy documents, etc.),
the main SKILL.md framework applies without modification.

Each section covers:
- How to identify and ask about AI involvement for this modality
- How to adapt the contribution label framework
- Modality-specific fields for the AI assertion block in JSON-LD
- Vocabulary and terminology conventions
- Known limitations of provenance documentation for this modality

---

## A. Code

### Why code is different

Code provenance is more complex than writing provenance for three reasons:

1. **Integration depth**: AI-generated code is rarely used as a standalone output. It gets
   integrated into larger codebases, modified over time, tested, refactored, and maintained.
   Unlike a revised essay (where "before" and "after" are relatively clear), a function
   scaffolded by AI and then modified by a developer over six months may be genuinely
   impossible to attribute at the line level.

2. **Ongoing modification**: A creation record for code describes a point in time. Living
   codebases evolve, and AI-generated components may be refactored beyond recognition or
   deleted entirely. Records should note this temporal quality.

3. **Licensing and security stakes**: AI-generated code raises unresolved questions about
   training data copyright (outputs may resemble licensed code in the training set). Security
   vulnerabilities in AI-generated code may not be caught by the original human reviewer.
   These stakes are different in kind from writing.

**Reference framework**: SPDX (Software Package Data Exchange, https://spdx.dev) is the
Linux Foundation's open standard for software bill of materials (SBOM). For formal or
organizational code provenance contexts, SPDX is the most recognized standard. The creation
record skill does not produce SPDX-compliant records, but its JSON-LD can note SPDX
compatibility or reference an SPDX document if one exists.

### Step 1 additions for code

When work type is identified as code, ask these additional questions:

**About integration:**
> "Is this AI-generated code a standalone script or file, or is it integrated into a
> larger codebase you or your team maintain?"

- **Standalone**: contribution label applies straightforwardly
- **Integrated**: note the integration context; use integration depth descriptor (see below)

**About modification extent:**
> "How much of the AI-generated code remains in its original form? Roughly:
> — Used mostly as-is (minor fixes only)
> — Substantially modified (significant rewrites, but AI structure remains)
> — Heavily refactored (AI output served as a scaffold; most code is now human-written)
> — Replaced/deleted (AI output was a starting point that no longer exists in the codebase)"

**About testing and review:**
> "Did you review, test, or audit the AI-generated code before using it?
> If so, what did that involve — running tests, code review, security review, or other?"

**About ongoing maintenance:**
> "Is this a living codebase that will be maintained over time, or a one-time output?"

- **Living codebase**: note this in the record; recommend updating the creation record
  at major version milestones or when AI involvement changes significantly
- **One-time output**: standard record applies

### Contribution labels for code

The standard labels apply but with code-specific interpretation:

| Label | Code interpretation |
|---|---|
| **AI-Produced** | AI wrote the code; human reviewed and approved with minimal changes |
| **AI-Produced, Extensively Directed** | AI wrote all code; human provided detailed specs, constraints, and iterative direction across multiple exchanges |
| **AI-Drafted, Human-Revised** | AI scaffolded the code; human made meaningful modifications to logic, structure, or implementation |
| **AI-Assisted** | Human wrote primary codebase; AI contributed specific functions, modules, or completions |
| **AI-Supported** | Human wrote all code; AI used for debugging assistance, documentation, code review suggestions, or explanation |
| **Human-Created, AI-Reviewed** | Human wrote all code; AI reviewed for issues, suggestions not incorporated or minimally incorporated |

**Integration depth descriptor** — use in addition to (not instead of) the contribution label:

| Descriptor | Meaning |
|---|---|
| `standalone` | AI-generated code used as a complete, self-contained output |
| `integrated-limited` | AI-generated code integrated into a larger codebase with clear boundaries |
| `integrated-extensive` | AI-generated code woven throughout a codebase; line-level attribution impractical |
| `scaffolded-refactored` | AI output served as initial structure; substantially rewritten by humans |
| `deprecated` | AI-generated code has since been replaced or removed |

### JSON-LD fields for code

Add these fields to the `c2pa:assertions` block for code work:

```json
{
  "c2pa:mediaType": "code",
  "c2pa:codeLanguage": "[Python | JavaScript | SQL | etc.]",
  "c2pa:integrationDepth": "[standalone | integrated-limited | integrated-extensive | scaffolded-refactored | deprecated]",
  "c2pa:modificationExtent": "[used-as-is | substantially-modified | heavily-refactored | replaced]",
  "c2pa:humanReviewType": "[none | manual-review | unit-testing | integration-testing | security-review | code-review | multiple]",
  "c2pa:isLivingCodebase": "[true | false]",
  "c2pa:spdxReference": "[SPDX document identifier or URL, or null]",
  "c2pa:licensingNote": "[note any known or potential licensing concerns with AI-generated code, or null]"
}
```

### Terminology conventions for code

- Use **"written"** or **"implemented"**, not "drafted"
- Use **"scaffolded"** when AI produced a structural starting point the human built from
- Use **"completed"** when AI filled in a function or block from human-written context
- Use **"refactored"** when human substantially rewrote AI-generated code
- Use **"integrated"** not "used" when describing how AI code entered a larger codebase
- Use **"reviewed"** and **"tested"** precisely — distinguish between these activities

### Limitations note for code

Code creation records document AI involvement as understood at a point in time. For integrated
or maintained codebases, this record may become inaccurate as code evolves. The record
should note whether the codebase is actively maintained and recommend review at significant
milestones. Line-level or function-level attribution is rarely practical and should not be
attempted unless the codebase is small and the AI output clearly bounded.

---

## B. Images and Visual Design

### Why images are different

Image generation operates differently from text generation in ways that affect provenance:

1. **Generation vs. selection**: Image AI tools typically produce multiple candidates from
   a single prompt. The human's choice among those candidates — and rejection of others — is
   a meaningful creative act not captured by "prompt characterization" alone.

2. **Style references and input images**: Many image generation workflows involve providing
   reference images, style guides, sketches, or subject photographs as inputs. These human-
   provided visual inputs are creative contributions that the current framework doesn't
   capture well.

3. **Post-processing**: AI-generated images are routinely edited in tools like Photoshop,
   Figma, or Lightroom after generation. The extent of this editing varies enormously — from
   color correction to substantial compositional changes — and is meaningful for provenance.

4. **C2PA native support**: C2PA was originally designed primarily for image and media
   provenance. The full C2PA spec includes richer fields for images than this skill currently
   uses — particularly around training data assertions and content binding (cryptographic
   hashing). For high-stakes image provenance, note that a full C2PA implementation offers
   stronger guarantees than a self-reported creation record.

### Step 1 additions for images

When work type is identified as an image, photograph, illustration, or visual design asset:

**About generation inputs:**
> "Did you provide any visual inputs to the AI — such as reference images, style guides,
> sketches, or subject photographs? If so, what were they?"

**About selection:**
> "Did the AI tool generate multiple options you chose among? If so, roughly how many
> alternatives were generated before you selected or stopped?"

**About post-processing:**
> "Was the AI-generated image edited or modified after generation? If so, how substantially —
> for example: color/exposure adjustments only, selective compositing, significant retouching,
> or full compositional reworking?"

**About intended use:**
> "Where will this image be used — for example, web publication, print, internal
> presentations, or as a component within a larger design?"

This matters because some contexts (journalism, public communications) have stricter
norms around AI-generated imagery than others.

### Contribution labels for images

| Label | Image interpretation |
|---|---|
| **AI-Produced** | AI generated the image; human wrote the prompt and approved the result with no post-processing |
| **AI-Produced, Extensively Directed** | AI generated the image through multiple iterative prompting rounds with significant human visual direction |
| **AI-Drafted, Human-Revised** | AI generated a base image that was meaningfully edited or composited by a human |
| **AI-Assisted** | Human created the primary image (photography, illustration, design); AI used for specific elements, effects, or suggestions |
| **AI-Supported** | Human created the image; AI used for minor enhancement (upscaling, noise reduction, color grading) |
| **Human-Created, AI-Reviewed** | Human created the image; AI tools used for assessment or quality check only |

**Style reference descriptor** — use when human-provided visuals influenced generation:

| Descriptor | Meaning |
|---|---|
| `no-reference` | No visual inputs provided; prompt-only generation |
| `style-reference` | Reference image(s) provided for stylistic direction |
| `subject-reference` | Reference image(s) provided showing the subject (person, object, place) |
| `sketch-reference` | Human sketch or rough provided as compositional input |
| `brand-constrained` | Generation constrained by provided brand guidelines or design system |
| `composite-source` | AI output combined with human-created or human-sourced visual elements |

### JSON-LD fields for images

Add these fields to the `c2pa:assertions` block for image work:

```json
{
  "c2pa:mediaType": "image",
  "c2pa:imageFormat": "[jpeg | png | svg | webp | etc.]",
  "c2pa:generationTool": "[tool name — e.g. Midjourney, DALL-E 3, Firefly, Stable Diffusion]",
  "c2pa:styleReferenceDescriptor": "[no-reference | style-reference | subject-reference | sketch-reference | brand-constrained | composite-source]",
  "c2pa:styleReferenceDescription": "[plain-language description of visual inputs provided, or null]",
  "c2pa:selectionNote": "[how many alternatives were generated; basis for selection, or null]",
  "c2pa:postProcessing": "[none | minor-adjustments | selective-editing | substantial-reworking]",
  "c2pa:postProcessingTools": "[tools used for post-processing, e.g. Photoshop, Figma — or null]",
  "c2pa:postProcessingDescription": "[plain-language description of post-processing work, or null]",
  "c2pa:intendedUse": "[web | print | internal | component | other]",
  "c2pa:fullC2PANote": "[note if a cryptographically-bound C2PA manifest is also available, or null]"
}
```

### Terminology conventions for images

- Use **"generated"**, not "drafted" or "written"
- Use **"composited"** when AI and human-created elements are combined
- Use **"directed"** when describing iterative visual prompt refinement
- Use **"selected from"** when describing the human's choice among AI-generated candidates
- Use **"post-processed"** for editing after generation
- Use **"retouched"**, **"color-graded"**, **"composited"**, or **"reworked"** specifically
  when describing post-processing, rather than the generic "edited"
- For design assets: **"generated and adapted"** when AI output was refined to fit a
  design system

### Limitations note for images

Self-reported creation records for AI-generated images cannot provide the tamper-evidence
of a cryptographically-bound C2PA manifest. For contexts where verifiability matters
(journalism, public communications, legal use), a creation record should be accompanied by
a note that it is self-reported and cannot be independently verified without a full C2PA
implementation. Some image generation tools (e.g., Adobe Firefly, certain versions of
DALL-E) attach C2PA-compliant metadata automatically — note this in the record if applicable.

---

## C. Audio and Video

### Why audio/video is different

Audio and video provenance is underserved by existing frameworks. The main challenges:

1. **AI enters at multiple layers**: In a video production, AI may be involved in scripting,
   voiceover synthesis, background music generation, automated editing (scene detection, auto-
   captioning, silence trimming), visual effects, thumbnail generation, and translation/
   dubbing — often by different tools, at different stages, with different levels of human
   oversight. Each needs to be described separately.

2. **Synthetic voice raises distinct stakes**: AI-generated voice (text-to-speech or voice
   cloning) carries specific ethical and legal weight — audience consent, identity representation,
   and emerging regulations around synthetic media. This warrants explicit treatment in any
   creation record.

3. **Temporal media and editing**: Unlike a document or image, audio and video have a timeline.
   AI assistance at the editing stage (trimming, pacing, transitions) is qualitatively different
   from AI generating source material. The creation record should distinguish source generation
   from editing assistance.

4. **Transcription-based editing**: A common workflow involves AI generating a transcript of
   recorded audio or video, which the human then edits as text (deleting words/sentences to
   edit the media). This is AI-Assisted — the AI processed the source but humans made all
   editorial decisions.

### Step 1 additions for audio/video

When work type is identified as audio, video, podcast, or multimedia:

**About AI involvement by layer** — ask about each layer separately:
> "Did AI play a role in any of these areas? (check all that apply)
> — Script or narration writing
> — Voiceover or narration (AI-synthesized voice)
> — Background music or sound design
> — Video editing (auto-cut, pacing, transitions)
> — Captioning or transcription
> — Translation or dubbing
> — Visual effects or motion graphics
> — Thumbnail or still image generation
> — Other"

For each "yes": ask whether the AI output was used directly, modified, or served as a basis
for human-created replacement.

**About synthetic voice specifically** (if applicable):
> "Was any voice in this content AI-synthesized or AI-cloned? If so:
> — Is it a generic synthetic voice, or a cloned voice based on a real person?
> — If a real person's voice, do you have their consent for this use?
> — Will the audience be informed that the voice is AI-generated?"

This question is asked not to gatekeep but to ensure the creation record accurately reflects
the nature and stakes of the AI involvement.

**About source recordings** (if applicable):
> "Does this work include original recordings (voice, music, footage) by human contributors?
> If so, who are they, and what did they record?"

This captures the human creative contribution of performers, speakers, and videographers.

### Contribution labels for audio/video

Because AI may enter at multiple layers, the overall contribution label describes the
**net balance** of AI vs. human creative contribution across the work as a whole. Specific
layer-by-layer detail goes in the AI Contribution Summary section.

| Label | Audio/Video interpretation |
|---|---|
| **AI-Produced** | AI generated the primary content (script, voice, music, or footage); human directed and approved |
| **AI-Produced, Extensively Directed** | AI generated primary content through substantive iterative direction from human creator |
| **AI-Drafted, Human-Revised** | AI generated source content that humans substantially edited, re-recorded, or reworked |
| **AI-Assisted** | Humans created primary content; AI used for specific elements or editing assistance |
| **AI-Supported** | Humans created all primary content; AI used for processing tasks (transcription, captioning, noise reduction) |
| **Human-Created, AI-Reviewed** | Humans created all content; AI used only for assessment or suggestion |

### JSON-LD fields for audio/video

The AI assertion block should include a `c2pa:productionLayers` array, one entry per
AI-involved layer:

```json
{
  "c2pa:mediaType": "[audio | video | podcast | multimedia]",
  "c2pa:duration": "[HH:MM:SS or null]",
  "c2pa:productionLayers": [
    {
      "c2pa:layer": "[script | voiceover | music | video-editing | captioning | translation | visual-effects | thumbnail | other]",
      "c2pa:layerRole": "[produced_by | assisted_by | supported_by]",
      "c2pa:layerModel": "[tool/model name and provider]",
      "c2pa:layerDescription": "[plain-language description of AI's role in this layer]",
      "c2pa:humanModification": "[used-as-is | lightly-edited | substantially-reworked | replaced]"
    }
  ],
  "c2pa:syntheticVoice": {
    "c2pa:present": "[true | false]",
    "c2pa:voiceType": "[generic-tts | voice-clone | null]",
    "c2pa:consentObtained": "[true | false | not-applicable | null]",
    "c2pa:audienceDisclosure": "[true | false | null]"
  },
  "c2pa:originalRecordings": "[description of human-created recordings included, or null]"
}
```

### Terminology conventions for audio/video

- Use **"synthesized"** for AI-generated voice, not "recorded"
- Use **"generated"** for AI-created music or sound design
- Use **"AI-assisted editing"** for editing workflows using AI tools
- Use **"transcription-based editing"** for the specific workflow of editing via AI transcript
- Use **"dubbed"** or **"AI-dubbed"** specifically for AI-translated voice replacement
- Use **"captioned"** for AI-generated captions (distinguishing from human-written subtitles)
- Use **"composited"** when AI-generated visual elements are combined with recorded footage
- Distinguish **"source creation"** (script, recording, footage) from **"post-production"**
  (editing, effects, color grading) — AI involvement at each stage has different weight

### Limitations note for audio/video

AI-assisted audio and video editing tools are often embedded in production software
(Adobe Premiere, DaVinci Resolve, CapCut, etc.) and may operate automatically without
explicit user invocation. Creators may not be fully aware of all AI processing applied
to their media. Creation records for audio/video should note this and recommend that
creators review their production tools' AI feature disclosures. Records are necessarily
incomplete if AI features were applied automatically without the creator's knowledge.

Synthetic voice records in particular should note whether audience disclosure was made,
as norms and emerging regulations vary by context and jurisdiction.

---

## D. Mixed-Modality Works

Many real-world outputs combine modalities — a web page (text + images + code), a
presentation (text + images), a podcast with show notes (audio + text), a data report
(text + visualizations + data). For these:

1. **Identify the primary modality** for the contribution label — what is the work
   primarily experienced as?
2. **Apply modality-specific guidance per component** in the AI Contribution Summary —
   describe AI involvement in text, image, and code components separately
3. **Use multiple assertion blocks** in JSON-LD when different AI tools were used for
   different components
4. **The process narrative** should describe the work's creation holistically, noting
   where different modalities came together

The multi-party web redesign example (Example 8 in creation-record-examples.md)
demonstrates this pattern for a project spanning UX research, design, code, and content.

---

## E. When to Recommend a Stronger Standard

Self-reported creation records are honest but not verifiable. In some contexts, a stronger
standard is appropriate:

| Context | Recommendation |
|---|---|
| Journalism / news photography | Full C2PA implementation with cryptographic binding; note https://c2pa.org |
| Legal or evidentiary use | Consult legal counsel; creation records are not sufficient for evidentiary purposes |
| Academic publication | Follow publisher's specific AI use requirements; cite this record as supplementary |
| Production code in regulated industries | Consider SPDX-compliant SBOM alongside creation record |
| Public communications with synthetic voice | Explicit audience disclosure recommended; check applicable regulations |
| High-volume AI image generation | Full C2PA implementation or tool-native provenance metadata preferred |
