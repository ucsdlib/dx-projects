# QSF Conventions (UCSD Qualtrics Import)

Patterns for generating importable QSF files. CONFIRMED patterns appear
in real exports from the UCSD instance and/or survived successful
imports. UNCONFIRMED patterns are extrapolated; verify against a real
export before relying on them, and never mark a build complete while it
depends on an unconfirmed pattern without telling the user.

## Spec format (input to scripts/assemble_qsf.py)

```json
{
  "survey_name": "...",
  "questions": [ { ...SQ payload objects... } ],
  "blocks": [ { ...BL payload array entries... } ],
  "flow": { ...FL payload object... }
}
```

`questions` entries are full question payloads (the value of an SQ
element's Payload, including QuestionID). `blocks` is the array assigned
to the BL element's Payload. `flow` is the object assigned to the FL
element's Payload. assemble_qsf.py wraps questions into SQ elements
(PrimaryAttribute = QuestionID, SecondaryAttribute = QuestionDescription),
replaces BL/FL payloads, sets the QC count, keeps every other element and
SurveyEntry verbatim from the base export, and validates references.

## Root structure (CONFIRMED)

- Root keys are exactly `SurveyEntry` and `SurveyElements`. The importer
  requires a root `SurveyEntry`; missing it fails with
  `ImportProjectRequest.SurveyEntry ... 'required'`. Other format errors
  surface as a generic "Something went wrong and the project wasn't
  created" UI message.
- Keep SurveyID, response-set id, Preview Link, Survey Options (skin),
  Scoring, and Statistics verbatim from the base export. Reusing the
  export's SurveyID on import is safe; Qualtrics assigns a new survey id.

## SurveyEntry (CONFIRMED)

SurveyID (SV_ + 16 chars), SurveyName, SurveyDescription, SurveyOwnerID,
SurveyBrandID ("ucsd"), DivisionID, SurveyLanguage ("EN"),
SurveyActiveResponseSet (matches RS element), SurveyStatus ("Inactive"),
SurveyStartDate/SurveyExpirationDate/LastAccessed/LastActivated
("0000-00-00 00:00:00"), SurveyCreationDate/LastModified
("YYYY-MM-DD HH:MM:SS"), Deleted (null).

## SurveyElements anatomy (CONFIRMED)

Every element: SurveyID, Element (SQ/BL/FL/PL/PROJ/QC/RS/SCO/SO/STAT),
PrimaryAttribute, SecondaryAttribute, TertiaryAttribute, Payload.
SQ: PrimaryAttribute QIDn, SecondaryAttribute = question description.
QC: SecondaryAttribute = question count as string, Payload null.
Export element order: BL, FL, PL, PROJ, QC, RS, SCO, SO, SQ*, STAT.
Payloads are JSON objects, not strings.

## Question payloads

Common fields (CONFIRMED): QuestionText, DataExportTag (Qn, unique),
QuestionType, Selector, DataVisibility {Private:false, Hidden:false},
Configuration {QuestionDescriptionOption:"UseText"}, QuestionDescription,
Validation, GradingData [], Language [], NextChoiceId (choices+1),
NextAnswerId (1), QuestionID. TE adds SearchSource
{AllowFreeResponse:"false"}. There is no `Required` field: required is
`Validation: {"Settings": {"ForceResponse": "ON", "Type": "None"}}`,
optional uses "OFF".

| Mach type | Qualtrics payload | Status |
|---|---|---|
| section | Standard block (Description = label), not a question | CONFIRMED |
| page_break | {"Type": "Page Break"} in BlockElements | CONFIRMED |
| text, url | TE / SL | CONFIRMED |
| textarea | TE / ML | CONFIRMED |
| simple_name, simple_name_wmiddle | TE / SL single field | CONFIRMED |
| email | TE / SL, ContentType "ValidEmail" | CONFIRMED |
| select | MC / DL, ChoiceOrder strings | CONFIRMED |
| radio | MC / SAVR, SubSelector "TX", ChoiceOrder numbers | CONFIRMED |
| checkbox | MC / MAVR, SubSelector "TX", ChoiceOrder strings | CONFIRMED |
| date | TE / SL, ContentType "ValidDate" | CONFIRMED |
| phone, simple_phone | TE / SL, ContentType "ValidPhone" | CONFIRMED |
| address | TE / FORM multiple TextEntry fields | CONFIRMED pattern |
| number | TE / SL, ContentType "ValidNumber" + ValidNumber Min/Max/NumDecimals | UNCONFIRMED (structure observed; live sample needed) |
| money | TE / SL + currency validation | UNCONFIRMED |
| time | TE / SL + time validation | UNCONFIRMED |
| matrix | Matrix / Likert / SingleAnswer | CONFIRMED |
| rating | Matrix / Likert custom scale | CONFIRMED pattern |
| media | DB question with image | UNCONFIRMED |
| file | No reliable QSF path; flag for manual handling | UNCONFIRMED |
| signature | No QSF equivalent; flag for manual handling | UNCONFIRMED |

Choices: {"1": {"Display": "..."}}, NextChoiceId = highest id + 1.
DB (descriptive text): QuestionType "DB", Selector "TB", ChoiceOrder [],
Validation Settings Type "None" without ForceResponse, DefaultChoices
false; QuestionText holds HTML.

Matrix (CONFIRMED): QuestionType "Matrix", Selector "Likert", SubSelector
"SingleAnswer". Statements in Choices/ChoiceOrder (strings); scale in
`Answers` and `AnswerOrder` (numbers); NextAnswerId = scale size + 1.
Configuration adds "TextPosition": "inline", "RepeatHeaders": "none",
"WhiteSpace": "OFF", "MobileFirst": true, optional "Autoscale":
{"XScale": {"Name": "agreeDisagree", "Type": "likert", "Reverse": false}};
plus "ChoiceDataExportTags": false and ColumnLabels. Multi-answer matrix
(SubSelector "MultipleAnswer") is UNCONFIRMED.

## Validation patterns

- Required: ForceResponse "ON" (CONFIRMED).
- Content validation on a standalone single-line field (CONFIRMED, the
  UCSD staff preference for email/phone/date): Validation Settings
  {"ForceResponse": "...", "Type": "ContentType", "MinChars": "1",
  "ContentType": "ValidEmail" | "ValidDate" | "ValidPhone",
  "ValidDateType": "DateWithFormat", "ValidPhoneType": "ValidUSPhone",
  "ValidZipType": "ValidUSZip", "ValidNumber": {"Min": "", "Max": "",
  "NumDecimals": ""}}. The export keeps every auxiliary key present
  regardless of the active ContentType; replicate the full object and
  change only ContentType (plus ForceResponse as needed).
- TE/FORM fields (CONFIRMED): field Choices entries carry "TextEntry":
  "on" plus "TextEntryValidation": "ValidEmail", "DateWithFormat", or
  "USPhone", optionally "TextEntryLength": "Short". TE/FORM remains the
  pattern for multi-field composites such as addresses.
- Min characters (CONFIRMED): Validation Settings {"ForceResponse":
  "OFF", "ForceResponseType": "ON", "Type": "MinChar", "MinChars": "1"}.

## Blocks (CONFIRMED)

BL Payload array: first block Type "Default", one Type "Trash" block
("Trash / Unused Questions", no BlockElements), then Type "Standard"
blocks with "SubType": "". Block IDs: BL_ + 16 chars. No Options key.
BlockElements: {"Type": "Question", "QuestionID": "QIDn"} and
{"Type": "Page Break"}. When validating block/question references,
exclude Page Break entries - they carry no QuestionID and must not be
counted as unknown questions.

## Survey flow (CONFIRMED unless noted)

FL Payload: {"Type": "Root", "FlowID": "FL_1", "Flow": [...],
"Properties": {"Count": N}} with N = highest FlowID used and sequential
FL_ ids. Block references: {"Type": "Block", "ID": ..., "FlowID": ...,
"Autofill": []} for the Default block; {"Type": "Standard", ...} for
Standard blocks. Branches: {"Type": "Branch", "FlowID": ...,
"Description": ..., "BranchLogic": ..., "Flow": [...]}.

BranchLogic (CONFIRMED, keep Qualtrics' "Conjuction" misspelling):

```json
{
  "0": {
    "0": {expression},
    "1": {expression, "Conjuction": "And"},
    "Type": "If"
  },
  "Type": "BooleanExpression"
}
```

Expression for a selected choice (CONFIRMED):

```json
{
  "LogicType": "Question", "QuestionID": "QID1",
  "QuestionIsInLoop": "no",
  "ChoiceLocator": "q://QID1/SelectableChoice/1",
  "Operator": "Selected", "QuestionIDFromLocator": "QID1",
  "LeftOperand": "q://QID1/SelectableChoice/1",
  "Type": "Expression",
  "Description": "<span class=\"ConjDesc\">If</span> <span class=\"QuestionDesc\">...question text...</span> <span class=\"LeftOpDesc\">Yes</span> <span class=\"OpDesc\">Is Selected</span> "
}
```

Choice number 1 = first choice, 2 = second; conjunct words are "If" for
the first expression and "And"/"Or" for later ones.

Ending paths (CONFIRMED strategy): put continuation blocks INSIDE a
branch (e.g., both gate answers No -> item blocks) so exclusive paths end
at their redirect block without an EndSurvey element. EndSurvey flow
element syntax is UNCONFIRMED.

## Known gaps

Numeric/currency/time ContentType values (the ValidNumber object
structure is observed in exports, but a live number-field sample is
needed to confirm its ContentType usage), file upload, media/image,
signature, EndSurvey element, quotas. When an export containing these
becomes available, extract and confirm the patterns here.
