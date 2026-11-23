# Mode: store-review

Answer: if an app reviewer installed this build today, what would they hit? This mode walks the app the way a reviewer does. It doesn't predict approval. Review outcomes depend on people, history and policy changes this run can't see.

Load the platform reference as well: [apple-app-review.md](apple-app-review.md) or [google-play-review.md](google-play-review.md). For a store app on both platforms, run them as two separate walkthroughs with two verdicts.

## Inputs (ask for what's missing, in one message)

Reviewers see more than the app. Without these, the related checks are `NOT VERIFIED`, never assumed fine:
- **The build:**
  - **Apple:** a simulator build or a device or TestFlight install.
  - **Google:** an APK, or AAB-derived install, or an internal-track install.
- **The listing:** name, subtitle or short description, description, screenshots, previews, and category or age rating. The owner pastes them or gives the store URL if it's live.
- **What the reviewer is told:**
  - **Apple:** the Review Notes.
  - **Google:** the App access instructions, plus any demo credentials.
- **What's sold:** in-app products and subscriptions, and what each unlocks.
- **Privacy declarations:** the privacy label answers (Apple) or the Data safety answers (Google), copied as text.
- **Policy pages:** the privacy policy, terms and support URLs.
- **Market details:** the regions where it launches, and anything regulated (health, finance, kids, gambling or loans).

Copied store-console text is allowed because a reviewer sees it too. Reading the source code is still off-limits.

## The reviewer persona

```
You are an experienced <Apple App Review | Google Play> reviewer looking at this build on a clean install of the latest OS.
First read only what the store gives you: the listing, the review notes or app access instructions, and the credentials.
Then try every feature the listing or notes claim, and the paths reviewers check first:
- launch, then sign up, sign in, sign out and delete the account;
- purchase, restore and cancel paths in the sandbox;
- deny each permission, and check content moderation where users create or share content or there's AI output;
- links to the privacy policy, terms and support;
- anything that looks unfinished, hidden, misleading, or different from the listing.
You have limited time and no access to the developer. If something needs explanation the notes don't give, that's a finding.
Use only the interface. Screenshot every issue.
```

Run the reviewer once from a fresh install. Then work through the platform checklist on the same build for anything the walkthrough didn't touch.

## Recording results

Every checklist item gets one of:
- **PASS:** observed working on this surface.
- **FAIL:** observed problem. Include the guideline or policy citation and the evidence.
- **NOT VERIFIED:** the input is missing, or the step wasn't reached.
- **NOT TESTABLE HERE:** the surface can't exercise it (see [surfaces.md](surfaces.md)).
- **CHECK IN CONSOLE:** a store-side setting the app can't show, such as agreements, the toolchain or SDK level, declarations or trader status.
- **N/A:** the feature doesn't exist in this app.

## Verdict

- **Rejection risks found:** any FAIL in a platform blocker section.
- **No rejection risks found on this surface:** no FAILs, and the blocker items not covered (NOT VERIFIED or NOT TESTABLE HERE) are listed.
- **Not verified:** the core flows couldn't be exercised.

Never say "will be approved".

## Output

- Verdict, plus the checklist table (blockers first, then advice).
- Findings in the [evidence.md](evidence.md) format, each with its guideline or policy citation.
- **A draft for the reviewer:**
  - **Apple:** Review Notes.
  - **Google:** App access instructions.

  Based only on what the walkthrough showed a reviewer would need: steps, credentials placeholder, features to look at, external services, regional differences. Never put real secrets in the draft.
- The fix brief, and a `CHECK IN CONSOLE` list for the owner.

**Policies change.** If web access is available, reopen the current guideline pages linked in the platform reference before the run, and note the date. If they can't be reopened, say the checklist is from the reference's snapshot date.
