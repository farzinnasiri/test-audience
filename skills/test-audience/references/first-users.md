# Mode: first-users

Answer: can a first-time user get from the front door to first success, and where do they get stuck, confused or leave?

## Before the run (part of the plan)

1. **First success.** Get one observable moment from the owner, such as "sees their first generated plan", not "taps Sign up". If the owner can't name one, propose one based on looking at the landing page or listing, and confirm it in the plan.
2. **Start point.** The front door a real user arrives at: the landing page, store listing or install, or the first app launch.
3. **Personas.** Default to the core five in [personas.md](personas.md). For a native app with accounts or subscriptions, offer `returning`. Use fewer if the owner wants a quick check, and say what that skips.
4. **Isolation.** Use one independent agent per persona when the runtime supports subagents. Otherwise run them in sequence in this agent and disclose reduced isolation. Never claim agents you didn't run.
5. **State.**
   - **Accounts:** each persona gets its own test account or signup identity (for example `name+ta-impatient-<run>@…` on a domain the owner controls).
   - **Fresh start:** a fresh browser profile, or cleared app data.
   - **Order:** run `breaker` last if personas share any data.

## During the run

- Hand each persona agent exactly the brief in [personas.md](personas.md). Nothing else.
- Watch budgets. A persona that loops or stalls is stopped and its last state recorded.
- If an S1 blocker stops every persona at the same step, stop the run early. Report it rather than spending budget rediscovering it.

## Merge

1. Collect each persona's path, result and findings.
2. Deduplicate by symptom and location, not by wording, and keep the merge mapping.
3. Drop pure opinions (see [evidence.md](evidence.md)).
4. Rank by severity, then breadth, then how early it happens in the journey.
5. Record per persona whether they reached first success and their action count. Whether that persona would come back is a heuristic guess; label it so.

## Report

Use the report and fix brief formats in [evidence.md](evidence.md).

The verdict is:
- **ready for first users:** no S1 findings, and at least the impatient and mobile personas reached first success;
- **not ready:** any S1 finding;
- **not verified:** core personas weren't run, or the surface couldn't exercise the core path.

## Recheck

Input: the earlier report.
1. Show a recheck plan: same target and surface, the build or version under test, which findings and which personas.
2. Replay each fixed finding's exact reproduction steps first. Mark each `fixed`, `still failing` or `changed`; the last means something different now happens, so describe it.
3. Rerun the personas that failed or quit, using fresh agents and fresh state. They must not see the earlier report, or they'd walk straight to the fix.
4. A full rerun of all personas is optional. Offer it for large changes.
5. Report new findings separately as possible regressions.

Suggest the owner turn each confirmed fix into a deterministic end-to-end test in their own test suite. Exploratory personas are a discovery tool, not a regression suite.
