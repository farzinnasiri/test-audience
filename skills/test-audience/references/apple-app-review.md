# Apple App Review checklist

**Snapshot:** November 2026, from the [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/). Reopen them before relying on this list. Section numbers are Apple's.

## A. Blockers a walkthrough can test

- **Completeness (§2.1).** No crashes, broken buttons, placeholder text, "lorem ipsum", TODO screens, test data or "coming soon" destinations. Designed empty states with a clear first action are fine.
- **Reviewer access (§2.1).**
  - **Credentials:** the credentials or demo mode in the Review Notes work on a clean install. They don't depend on a one-time code sent to the developer, and they reach every feature the listing claims.
  - **Backend:** stays reachable for the whole walkthrough.
- **Accurate metadata (§2.3).**
  - **Listing:** the description, screenshots and previews match what this build actually does. Each feature the listing claims is reachable.
  - **Paid items:** disclosed in the listing (§2.3.2).
  - **Prices:** none in the app name, subtitle, screenshots or previews (§2.3.7). The paywall itself still shows real prices.
  - **Other platforms:** no names or imagery of other mobile platforms in the app (§2.3.10).
- **Hidden functionality (§2.3.1).** No feature, mode or remote-config path the reviewer can't reach and that the Review Notes don't describe.
- **Purchases (§3.1).**
  - **Mechanism:** digital content and features use in-app purchase where required. Storefront rules differ, so report "external payment link seen in <storefront>" for the owner to judge; don't rule on it.
  - **Sandbox behavior:** products load. Trial and renewal terms on the paywall are truthful and visible before purchase. Restore works.
  - **After a lapse:** paid access ends correctly when the subscription expires (sandbox), while legal links and account controls stay usable.
- **Account deletion (§5.1.1(v)).** If the app lets users create an account, it has an in-app way to delete it, not just log out. Following it shows a clear result.
- **Sign-in options (§4.8).** If the app offers third-party or social login, check whether an equivalent privacy-focused login option is offered. Report what's offered; don't decide exemptions.
- **Content users create, and AI output (§1.2).** Where the app has user-generated content, sharing or generative AI:
  - **Filtering** of objectionable content;
  - **Reporting** with a visible way to report content;
  - **Blocking** of abusive users, where accounts interact;
  - **Contact:** published contact information.

  Try typed prompts and uploads, not only presets.
- **Privacy in behavior (§5.1).**
  - **Permission prompts:** each one has a purpose string that explains the real use, and appears in context.
  - **Denial paths:** denying a permission leaves the rest of the app usable.
  - **Third-party AI:** if personal data goes to a third-party AI service, the app discloses that and asks first (§5.1.2(i)).
  - **Policy link:** the privacy policy opens from inside the app and from the listing.
- **Tracking (§5.1.2).** If the app shows the App Tracking Transparency prompt, tracking-dependent features respect "Ask App Not to Track". Report SDK network calls seen before consent as observations, not verdicts.
- **Ratings and review prompts (§5.6.1).** Only the system rating prompt. No custom "rate us 5 stars" gate, and no incentive for ratings.

## B. Engineering readiness (blockers when the feature exists)

- **Devices and display:** a cold launch and the full core flow on the oldest and newest supported OS on this surface, plus iPad if it's supported. Check safe areas, rotation where supported, Dynamic Type at a large size, dark mode, and a VoiceOver label spot check.
- **Network:** offline and slow network give understandable errors and a way to retry.
- **Session lifecycle:** logout, login, reinstall and restore keep the user's data and entitlements as promised.

## C. Advice (report it, never blocking)

- **Reviewer video:** a screen recording that walks a reviewer through signup, deletion, purchase and moderation. Apple sometimes asks newer accounts for one. Record from the home screen or first launch.
- **Duplicates (§4.3):** if the app looks very similar to many in its category, note it for the owner. Differentiation is a product question this walkthrough can't settle.

## CHECK IN CONSOLE (the app can't show these)

- **Agreements:** the Paid Apps Agreement and banking status.
- **Store-side settings:** in-app products attached to the version, the age rating questionnaire, and the App Privacy answers matching observed behavior.
- **Requirements:** the Xcode and SDK minimums, and EU trader status where it applies.

## Draft Review Notes (fill from the walkthrough)

1. What the app does and for whom, in two sentences.
2. How to sign in: a credentials placeholder, the demo mode, and any steps.
3. Where each paid feature is and how to reach it.
4. Where to find account deletion, and reporting or blocking.
5. External services the app depends on, such as auth, backend, payments, analytics and AI, with what each does.
6. Regional differences, or "No regional differences."
