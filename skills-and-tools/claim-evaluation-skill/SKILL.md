---
name: claim-evaluation-skill
description: Evaluate claims in written work by identifying assertions, assessing supporting evidence, verifying sources, and providing confidence ratings. This skill prevents "helpful but unfaithful" AI behavior by strictly distinguishing between what sources actually state versus what can be inferred or interpreted.
---

## Skill Purpose

Evaluate claims in written work by identifying assertions, assessing supporting evidence, verifying sources, and providing confidence ratings. This skill prevents "helpful but unfaithful" AI behavior by strictly distinguishing between what sources actually state versus what can be inferred or interpreted.

## When to Use This Skill

Use this skill when the user:
- Asks you to "check my claims" or "verify my sources"
- Requests evaluation of whether their writing accurately represents research
- Wants to know if citations support their arguments
- Needs confidence ratings on assertions in their draft
- Is concerned about accuracy or "stretching" evidence
- Requests fact-checking or source verification for academic/research writing

## Core Principles

### 1. Faithful Over Helpful
**CRITICAL:** Your primary obligation is accuracy to sources, not making the user's argument work. If a source doesn't support a claim, say so clearly—even if you could imagine a generous interpretation that might support it.

### 2. Three-Level Evidence Classification
Every claim-evidence relationship falls into one of three categories:
- **Direct Evidence:** Source explicitly addresses the claim
- **Reasonable Inference:** Source provides related information that logically suggests the claim
- **Interpretive Connection:** Requires significant interpretive leaps beyond source content

### 3. Verify Before Evaluating
Never evaluate a claim based on memory or assumptions about sources. Always:
1. Search for the actual source using the collaborative browser
   (`preview_navigate` to a search engine, database, or publisher site; `preview_snapshot`
   to review results) - this harness has no `web_search`/`web_fetch` tools
2. Read the full text when available (`preview_navigate` to the article URL, then
   `preview_snapshot`/`preview_evaluate` to extract text; `exec_command` for local files)
3. Quote directly from the source
4. Flag when you cannot access the full text

### 4. Distinguish Source Types
Different source types require different standards:
- **Empirical studies:** Focus on what was observed/measured, not speculation
- **Review papers:** Note they synthesize others' work; check if claims distinguish between reviewed findings vs. reviewer interpretation
- **Theoretical papers:** Acknowledge these are arguments, not empirical evidence
- **Popular/practitioner sources:** Flag as opinion/experience rather than research evidence

## Workflow

### Step 1: Extract Claims
Identify all factual assertions, especially those that:
- Reference research, data, or expert opinion
- Make generalizations about "research shows" or "studies demonstrate"
- Cite specific sources
- Use definitive language ("X causes Y," "experts do Z")

Output format:
```
**Claim 1:** [Quote the exact claim from user's text]
**Current citation:** [What source, if any, is cited]
**Evidence needed:** [What type of evidence would support this claim]
```

### Step 2: Verify Each Source
For each cited source:
1. Search for the source via the collaborative browser (`preview_navigate` with the
   citation, `preview_snapshot` to inspect results)
2. Verify citation details (author, year, title, publication)
3. Open the article URL in the browser (`preview_navigate`) and read the full text or
   abstract (`preview_snapshot`/`preview_evaluate`); read local files with `exec_command`
4. Extract relevant passages with direct quotes
5. Note access level: "Based on full text" / "Based on abstract only" / "Based on secondary sources"

### Step 3: Evaluate Evidence-Claim Alignment
For each claim, assess whether the source actually supports it:

**Ask these critical questions:**
- Does the source explicitly make this claim? (Quote it)
- Does the source provide data/findings that directly support this claim?
- Is the claim overgeneralized from what the source actually says?
- Does the claim add interpretation not present in the source?
- Are there caveats or limitations in the source that the claim ignores?

### Step 4: Classify Connection Type

**Direct Evidence:**
- Source explicitly discusses the topic in the claim
- Uses the same or synonymous terminology
- Makes the same or very similar assertion
- Example: Claim: "Expert designers are solution-focused" → Source states: "expert designers are solution-focused, not problem-focused"

**Reasonable Inference:**
- Source discusses related concepts or provides data that logically suggests the claim
- Requires modest interpretive step but follows logically
- The inference is defensible and researchers in the field would likely agree
- Example: Claim: "Designers integrate problem and solution thinking" → Source shows "designers alternate rapidly between problem definition and solution generation in protocol studies"

**Interpretive Connection:**
- Requires significant interpretive work
- Source discusses different topic/domain
- Connection requires assuming unstated relationships
- Experts might reasonably disagree about whether source supports claim
- Example: Claim: "Design requires co-evolution" → Source discusses "labor organization in Victorian architecture" (Ruskin)

### Step 5: Assign Confidence Level

**HIGH:**
- Source directly addresses the claim's topic
- Uses explicit language matching the claim
- Multiple direct quotes available
- Methodology supports the generalization level of the claim

**MEDIUM:**
- Source addresses related concepts
- Connection requires modest inference
- Evidence is suggestive rather than conclusive
- OR: Multiple sources weakly support, creating cumulative case

**LOW:**
- Source requires significant interpretation
- Connection depends on assumed relationships
- Evidence is tangential or from different domain
- Claim generalizes beyond what source demonstrates

## Output Format

For each claim evaluated, provide:

```markdown
## Claim [N]: "[Quote exact claim]"

**Current Citation:** [Source as cited in user's text]

### Source Verification
**Verified Citation (APA):** [Full, corrected APA citation with DOI if available]

**Access Level:** [Full text / Abstract only / Secondary sources]

**Summary:** [Summarize the source's actual findings and conclusions. Stay close to what the source explicitly states. Use direct quotes when making specific claims about what the source says. If uncertain about any detail, flag it.]

**Methodology/Evidence:** [What type of study was this? Empirical/Theoretical/Review? What was the evidence base? Sample size, methods, data sources?]

### Evidence-Claim Alignment

**Relevance to Claim:**

1. **Direct Evidence** (if any): 
   [Quote the source showing it directly supports the claim]
   
   "The source explicitly states: '[direct quote]' which directly supports the claim that [explanation]."

2. **Reasonable Inference** (if applicable): 
   [Explain the logical connection]
   
   "While the source doesn't explicitly state [claim], it shows [evidence], which suggests [claim] because [logical reasoning]."

3. **Interpretive Connection** (if applicable):
   [Acknowledge the interpretive leap]
   
   "This source could be read as relevant because [reasoning], though this requires inferring [X] from evidence about [Y]."

**Confidence Level:** [HIGH / MEDIUM / LOW]

**Justification:** [Explain why this confidence level]

### Recommended Revisions (if needed)

**Current claim:** "[Original]"

**Suggested revision:** "[More accurate version]"

**Rationale:** [Why this revision better matches the evidence]
```

## Special Guardrails Against "Helpful but Unfaithful" Patterns

### Red Flags to Watch For

❌ **Relevance Pressure:** Feeling compelled to make sources "work" for the user's argument
❌ **Synthesis Creep:** Adding interpretation while summarizing what sources say
❌ **Generous Reading:** Stretching source meaning to support user's claim
❌ **Confidence Inflation:** Rating evidence quality higher than warranted
❌ **Omitting Contradictions:** Ignoring parts of sources that complicate the claim

### Mandatory Checks

Before assigning any confidence level, ask yourself:
1. **Can I quote the source directly supporting this claim?** (If no → not HIGH)
2. **Would I make this claim if I were the source author?** (If no → acknowledge gap)
3. **Am I inferring something the source doesn't state?** (If yes → flag as inference)
4. **Does the source include caveats I'm ignoring?** (If yes → include them)
5. **Am I using different terminology than the source?** (If yes → justify why they're equivalent)

### When to Push Back

If the user's claim is NOT supported by their cited evidence, you must clearly state:
- "This source does not directly support this claim."
- "The source discusses [X], but the claim asserts [Y], which requires assuming [Z]."
- "While the source is relevant, the claim overgeneralizes what was actually demonstrated."

Then offer:
- More accurate phrasing that the source DOES support
- Additional sources that might support the claim
- Acknowledgment that the connection is interpretive

## Examples

### Example 1: HIGH Confidence

**Claim:** "Expert designers are solution-focused, not problem-focused."

**Source:** Cross, N. (2004). Expertise in design: An overview. *Design Studies*, 25(5), 427-441.

**Evaluation:**
- Direct quote from source (p. 432): "Many studies of expert design behavior suggest that designers move rapidly to early solution conjectures, and use these conjectures as a way of exploring and defining problem-and-solution together."
- Source explicitly addresses expert designer behavior
- Uses exact terminology from claim
- Synthesizes multiple empirical studies

**Confidence: HIGH** - The source directly supports the claim using matching language.

---

### Example 2: MEDIUM Confidence

**Claim:** "Research shows collaborative teams co-evolve problems and solutions."

**Source:** Wiltschnig et al. (2013). Collaborative problem-solution co-evolution in creative design. *Design Studies*, 34(5), 515-542.

**Evaluation:**
- Source title explicitly includes "collaborative problem-solution co-evolution"
- Protocol study of one design team, not multiple teams
- Claim generalizes "collaborative teams" but source studied one team

**Confidence: MEDIUM** - Direct evidence from one empirical study. Claim slightly overgeneralizes ("teams" plural vs. one team studied), but finding is specific and strong.

**Suggested revision:** "Research demonstrates that design teams can co-evolve problems and solutions (Wiltschnig et al., 2013)."

---

### Example 3: LOW Confidence  

**Claim:** "Historical movements in design education confirm that thinking and making must be integrated."

**Source:** Ruskin, J. (1853). The nature of Gothic. In *The stones of Venice*.

**Evaluation:**
- Ruskin wrote about labor organization and craft, not design education or cognition
- Quote: "it is only by labour that thought can be made healthy, and only by thought that labour can be made happy"
- Source is social/moral argument about Victorian labor practices
- Connection to design cognition requires 170-year interpretive leap

**Confidence: LOW** - The source is about labor ethics in Victorian architecture, not design education or cognitive processes. The principle is analogous but requires significant interpretive work to connect to modern design research.

**Suggested revision:** "Historical articulations like Ruskin (1853) argued that thinking and making are inseparable in craft practice, prefiguring modern design research findings."

## Error Patterns to Avoid

### Pattern 1: Quote Mining
❌ Taking a phrase out of context that sounds supportive
✅ Reading the full paragraph/section and representing the author's actual point

### Pattern 2: Synonym Substitution Without Verification
❌ Assuming "problem framing" = "problem definition" = "problem structuring"
✅ Checking whether source authors use these terms interchangeably or distinctly

### Pattern 3: Ignoring Study Limitations
❌ "Research shows X" based on one small qualitative study
✅ "One qualitative study found X" or "Initial research suggests X"

### Pattern 4: Treating Reviews as Primary Evidence
❌ Citing a review paper as if it's the original research
✅ Noting "According to a review by Y, multiple studies show X"

### Pattern 5: Inferring Causation from Correlation
❌ Source shows correlation, claim asserts causation
✅ Accurately representing the type of relationship the source demonstrated

## Final Reminders

- **Default to skepticism:** If uncertain, rate confidence LOWER
- **Quote liberally:** Direct quotes are your evidence for evaluation
- **Distinguish carefully:** Direct evidence ≠ Reasonable inference ≠ Interpretive connection
- **No circular reasoning:** Don't use your own summaries from earlier in the conversation as evidence
- **Access matters:** Always note whether you had full text, abstract only, or relied on secondary sources
- **The user benefits from accuracy:** Helping them strengthen their argument means ensuring every claim is bulletproof, not stretching weak evidence
