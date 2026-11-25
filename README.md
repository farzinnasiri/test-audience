<h1><img src="docs/test-audience.png" alt="Test audience — a dress rehearsal for your app" width="100%"></h1>

[![Claude Code](docs/agents/claude-code.png)](https://claude.com/product/claude-code) [![Codex](docs/agents/codex.png)](https://openai.com/codex/) [![Grok Build](docs/agents/grok-build.png)](https://docs.x.ai/build/overview) [![Grok Bot](docs/agents/grok-bot.png)](https://docs.x.ai/grok-bot/skills-routines-and-automations) [![Antigravity](docs/agents/antigravity.png)](https://antigravity.google/) [![Pi](docs/agents/pi.png)](https://pi.dev/) [![Cursor](docs/agents/cursor.png)](https://cursor.com/)

[![View on skills.sh](https://img.shields.io/badge/skills.sh-test--audience-245c53)](https://skills.sh/farzinnasiri/test-audience/test-audience) [![MIT license](https://img.shields.io/badge/license-MIT-444b50)](LICENSE)

**Where would a first-time user give up?** Give your coding agent a staging URL or test build and one task that matters. Five simulated users try it through the interface. You get the steps they took, screenshots of what went wrong, and a fix brief you can hand to a developer.

## Try it

```bash
npx skills add farzinnasiri/test-audience
```

Then ask your agent:

> Try my staging app as five first-time users. Start on the landing page and try to save a first project. Show me where each user finished or gave up.

The impatient user gets eight actions. The skeptic looks for pricing and privacy before signing up. The mobile user tries a small screen, the literal reader follows labels, and the breaker double-taps and goes back mid-flow. You approve the target, tools and test accounts before the run.

## Pick a run

| What do you want to learn? | What you get |
| --- | --- |
| [Can first-time users finish a task?](skills/test-audience/references/first-users.md) | Reproducible findings ranked by severity, then by how many personas hit them. |
| [What might block store review?](skills/test-audience/references/store-review.md) | A walkthrough of the build against your listing, risks with policy citations, and draft Apple Review Notes or Google Play App access instructions. |
| [Which concept should I test with people?](skills/test-audience/references/concept-panel.md) | Objections to 2–5 variants and, when scoring is available, a relative ranking. Treat it as a synthetic hypothesis. |
| [Did the fix work?](skills/test-audience/references/first-users.md#recheck) | A replay of the earlier findings on the new build, with a result for each and any new regressions. |

<details>
<summary><strong>Tools and test access</strong></summary>

[Claude Code](https://claude.com/product/claude-code) · [Codex](https://openai.com/codex/) · [Grok Build](https://docs.x.ai/build/overview) · [Antigravity](https://antigravity.google/) · [Pi](https://pi.dev/) · [Cursor](https://cursor.com/) · [All CLI agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

[Grok Bot private skill setup](https://docs.x.ai/grok-bot/skills-routines-and-automations)

For a walkthrough, the agent needs browser controls or a UI driver for a simulator, emulator or device. Use test accounts and sandbox payments. The report records what the chosen device could verify. [Supported surfaces](skills/test-audience/references/surfaces.md) · [Report format](skills/test-audience/references/evidence.md)

For a concept panel, supply the variants and intended audience. Numeric scoring uses Python, uv and a local embedding model downloaded on first use. Without scoring, you still get the objections.

</details>

<details>
<summary><strong>Credits and research</strong></summary>

Persona QA draws on the five-user launch prompt. Run planning, persona isolation and reporting draw on [first-user-audit](https://github.com/BarganConstantin/agent-skills) (MIT).

Concept scoring uses [PyMC Labs’ Semantic Similarity Rating](https://github.com/pymc-labs/semantic-similarity-rating). The [original study](https://arxiv.org/abs/2510.08338) evaluated stated purchase intent for personal-care concepts. For an app, use the panel to choose what to test with real people.

</details>
