# test-audience

An agent skill that checks whether your app is really ready by putting it in front of a **test audience** before real people see it. The agent uses the running app the way people will, through a browser, simulator, emulator, cloud device or computer use, and never reads your source code.

```bash
npx skills add farzinnasiri/test-audience
```

Works with Claude Code, Codex, Cursor and the other agents the [`skills` CLI](https://github.com/vercel-labs/skills) supports. Then ask your agent something like "test my app like first-time users would", "would App Store review reject this build?" or "which of these three paywalls should I test with real users?"

## Modes

| Mode | Who's looking | What you get |
|---|---|---|
| `first-users` | Five first-time users with hard behavior rules: **impatient** (8 actions, quits at the first error), **skeptic** (reads pricing, terms and privacy first), **mobile** (375px or the smallest device, slow network), **literal** (only what labels say, keyboard and accessibility tree), **breaker** (bad input, double taps, back mid-flow). Optional: returning, interrupted, or your own segment. | Findings with screenshots and steps to reproduce, ranked by severity then by how many personas hit them, plus a fix brief for your coding agent |
| `store-review` | An Apple App Review or Google Play reviewer on a clean install, using only your listing, review notes and test credentials | A checklist with guideline citations, the rejection risks found, draft Review Notes or App access instructions, and what to check in the console |
| `concept-panel` | A synthetic consumer panel scoring 2–5 concepts, pages or prices with Semantic Similarity Rating | A relative ranking with uncertainty and the top objections, always labeled **synthetic hypothesis** |
| `recheck` | The same personas, fresh, after you fix things | Each finding marked fixed, still failing or changed, plus new regressions |

## How a run works

1. **The skill picks the mode** from your request and asks at most three short questions if something's missing: where the app runs, the first-success moment, and test access.
2. **It checks which tools you have** and picks the most faithful surface. It lists up front what that surface can't test. For example, a mobile app in a desktop browser can't test native gestures, permission sheets, purchases or push.
3. **It shows a run plan and waits for your yes:** target, surface, personas, what's not testable, cost and output folder.
4. **It runs and reports.** It never edits your code. Fixing is a separate step with whatever agent owns the code, followed by `recheck`.

## Safety defaults

- No production targets unless you name one and accept it in the plan.
- Only test accounts and sandbox or test payments. No real messages to real people.
- Uploading a build to a cloud device service needs its own approval.
- Screenshots are checked for secrets and personal data before they're saved.
- Untested things are reported as `NOT TESTABLE HERE` or `NOT RUN`, never as passes.

## What it needs

- **Web:** a browser automation tool, such as [agent-browser](https://github.com/vercel-labs/agent-browser) or Playwright MCP.
- **iOS:** Xcode's Simulator plus a UI driver, such as [mobile-mcp](https://github.com/mobile-next/mobile-mcp), [Maestro](https://maestro.dev) or agent-device.
- **Android:** an emulator or device with `adb`, plus one of the same drivers.
- **Concept panel scoring:** Python and [uv](https://docs.astral.sh/uv/). The first run downloads a small local embedding model.

Without a usable tool, the skill stops and tells you what to install.

## Limits

These are simulated people. Persona runs find real defects and friction, but they can't tell you whether people want the product. Store-review mode can't predict a reviewer's decision. Concept-panel scores are relative and unvalidated for apps. The evidence behind them comes from consumer product concepts, and independent studies find synthetic respondents flatter than real ones. Use the results to decide what to put in front of real people first.

## Credits

- Persona QA idea popularized in a viral prompt. Gate, isolation and report ideas informed by [first-user-audit](https://github.com/BarganConstantin/agent-skills) (MIT).
- Semantic Similarity Rating: Maier et al., [*LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings*](https://arxiv.org/abs/2510.08338) (2025), using PyMC Labs' [semantic-similarity-rating](https://github.com/pymc-labs/semantic-similarity-rating) package.
- Store review checklists are summaries of Apple's and Google's public guidelines. Always check the current versions.

## License

MIT
