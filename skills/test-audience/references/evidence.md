# Evidence, ranking and report format

## A finding

Each problem gets a stable ID (`OI-001`, …) that's reused when several personas hit the same problem at the same step. Different root causes get different IDs, even on the same screen. Keep a mapping of anything you merged.

```
OI-007  Checkout button hidden behind keyboard on phone viewport
Class:     defect | friction | coverage-gap
Severity:  S1 | S2 | S3 | S4
Hit by:    mobile, impatient  (2 of 5)
Surface:   iOS Simulator, iPhone SE (3rd gen), iOS <version>, slow network profile
Where:     <screen or URL> after <step>
Steps:     1. … 2. … 3. …
Expected:  <what a user would reasonably expect>
Actual:    <what happened>
Evidence:  shots/mobile-03.png; console: "TypeError …" (12:04:31); network: POST /api/… 500
Observed or inferred: observed
```

- **Defect:** something is broken, blocked, wrong or crashes.
- **Friction:** observed hesitation, a misclick, backtracking, a wrong path or abandonment, with the action trail as evidence.
- **Coverage gap:** something that mattered but couldn't be tested on this surface.
- **Opinions** ("the colors feel dated") are dropped at merge time. An opinion survives only if it caused an observed wrong action.

## Severity

| Level | Meaning |
|---|---|
| S1 blocker | Can't reach first success, crash, data loss, wrong charge, security or privacy exposure, or a likely store rejection |
| S2 functional | Wrong behavior with a workaround a user might not find |
| S3 friction | Slowed, confused or misdirected a persona but they recovered |
| S4 polish | Minor; noticed with evidence but no effect on the task |

## Ranking

Sort by severity, then by breadth (how many personas hit it), then by how early in the journey it happens. Never rank by breadth alone: a double charge found only by the breaker outranks a copy complaint all five personas hit.

## Report (written to the output folder as `report.md`)

```
# Test audience report: <mode>, <date>
Verdict: <ready for first users / not ready / not verified> (one line on why)
Target / build / environment / surface / tool versions
First success: <definition>; reached by <personas>, with action count each
Isolation: independent agents | one agent in sequence (reduced isolation)

## Findings (ranked)
<table: ID | severity | class | title | hit by | where>
<full findings below the table>

## Coverage
NOT TESTABLE HERE: …
NOT RUN: …

## Per persona
<path taken, where they quit or succeeded, actions used against budget>

## Fix brief
<see below>

## Next step
```

## Fix brief (for a coding agent that wasn't here)

List the S1 and S2 findings first. Each entry is self-contained:
- **ID and title**
- **Steps to reproduce** on a named surface
- **Expected and actual** behavior
- **Evidence paths**
- **The owner decision needed, if any**, for example "truncate or wrap?" or a pricing or legal wording change

Describe symptoms only. This run never saw the code, so don't guess file names or causes.

Pricing, legal text, data-handling promises, auth, billing and security changes are marked `needs owner decision`. They are not given as instructions.

End with: "After fixing, run `test-audience recheck` against <report path>."

## Privacy of artifacts

Before saving, check every screenshot for tokens, emails, passwords, payment data or real personal data. Redact the screenshot or drop it, and say so.
