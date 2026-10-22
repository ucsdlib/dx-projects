# Search Log: Undergraduate Capstone Landscape

## Run overview

- **Working question:** What factors help undergraduate capstone projects and courses succeed?
- **Breadth tier:** Focused
- **UC Library Search mode:** Primo PNX REST fallback (keyless campus mount; no `PRIMO_KEY` present)
- **Tools used:** UC Library Search, Crossref, OpenAlex
- **Records screened:** 26 API records; 22 unique after title-level deduplication
- **Selected for landscape:** 11

## Query log

### `landscape`

- **Text:** `("undergraduate capstone" OR "senior capstone") AND ("project-based learning" OR "research mentoring")`
- **Filter:** `facet_searchcreationdate,exact,[2016 TO 2026]`
- **Purpose:** Focused landscape of capstone project-based learning and mentoring
- **Records screened:** 12 on one page
- **Approximate fidelity:** 67% on topic or useful adjacent
- **Decision:** Sufficient for initial themes; run one component search to test saturation.

### `component`

- **Text:** `("undergraduate capstone" OR "senior capstone") AND ("course design" OR "project design")`
- **Filter:** `facet_searchcreationdate,exact,[2016 TO 2026]`
- **Purpose:** Component search on course and project design
- **Records screened:** 14 on one page
- **Approximate fidelity:** 60% on topic or useful adjacent
- **Decision:** Added course-design and professional-preparation perspectives without requiring another page.

## Screened records

| Source ID | Query | Classification | Selected | Title | Access level | Confidence |
|---|---|---|---|---|---|---|
| `landscape-01` | landscape | on_topic | Yes | Design thinking for engaged learning in animal science: lessons from five semesters of a senior capstone course | Abstract only | high |
| `landscape-02` | landscape | on_topic | Yes | Exploring Student Perspectives of Project-Based Learning in an Agricultural Communications Capstone Course | Abstract only | high |
| `landscape-03` | landscape | on_topic | Yes | Modeling conflicting incentives in engineering senior capstone projects: A multi-player game theory approach | Abstract only | high |
| `landscape-06` | landscape | on_topic | Yes | Engaged Student Learning through IoT-based Capstone Projects: Particular Look at Student Engagement in Historically Underrepresented Groups | Abstract only | medium |
| `landscape-07` | landscape | adjacent | No | AI Augmented Software Engineering - A Case of Competency-Based Education and its Institutional Effectiveness | Abstract only | low |
| `landscape-08` | landscape | adjacent | No | A contextualized, experiential learning approach to quantitative engineering analysis | Abstract only | low |
| `landscape-09` | landscape | on_topic | Yes | A Systematic Course Design Approach to Guide the Development of a Construction Engineering and Management Capstone Course | Abstract only | medium |
| `landscape-10` | landscape | on_topic | Yes | A Learning-Centered Paradigm for Engineering Graphics and Design: Engineering Technology Students' Skill Gains and Capstone Preparation | Abstract only | medium |
| `landscape-11` | landscape | adjacent | No | Progressive Integration of Design Process into Civil Engineering Curriculum | Abstract only | low |
| `landscape-12` | landscape | adjacent | No | The Palgrave handbook of teaching and research in political science  | Abstract only | low |
| `component-01` | component | on_topic | Yes | Comparing STEM Students' and Employers' Emphases on Career Information Literacy : A Study on Undergraduate Capstone Units | Abstract only | medium |
| `component-03` | component | on_topic | Yes | Student Perceptions Concerning their Experience in a Flipped Undergraduate Capstone Course | Abstract only | medium |
| `component-05` | component | on_topic | Yes | Employing the ENHANCE Learning Model to Inform a High-Impact Course Design | Abstract only | medium |
| `component-06` | component | on_topic | Yes | An Innovative Approach to the Psychology Capstone Course | Abstract only | medium |
| `component-07` | component | adjacent | No | Unbounded: Integrating real-world problems into an undergraduate information design course | Abstract only | low |
| `component-08` | component | adjacent | No | Teaching Out-of-Order Processor Design with the RISC-V ISA | Abstract only | low |
| `component-09` | component | on_topic | Yes | Structure and Management of an Engineering Senior Design Course | Abstract only | medium |
| `component-10` | component | adjacent | No | Preliminary Design Review | Abstract only | low |
| `component-11` | component | adjacent | No | The Engineering Design Team | Abstract only | low |
| `component-12` | component | adjacent | No | Handbook of teaching and learning in sociology  | Abstract only | low |
| `component-13` | component | duplicate | No | Handbook of teaching and learning in sociology  / edited by Sergio A. Cabrera (assistant professor), Stephen Sweet (professor, department of sociology, Ithaca College, US). | Abstract only | low |
| `component-14` | component | noise | No | Research anthology on adult education and the development of lifelong learners  | Abstract only | low |

## Verification log

- Crossref confirmed citation metadata for `landscape-01`, `landscape-03`, `landscape-09`, and `component-09`.
- OpenAlex confirmed the title and venue for `component-01`; no DOI was present in the retrieved record.
- Crossref title search did not locate `component-01`, so OpenAlex was used as the alternative metadata check.

## Limitations

- All selected records were screened from abstracts or publisher descriptions; full texts were not reviewed.
- UC Library Search was used through the keyless Primo PNX REST fallback because no PRIMO_KEY was present.
- The focused landscape and one component search identified capstone-specific literature, but coverage is not exhaustive.
- Several useful sources were excluded as adjacent or duplicates during screening.
