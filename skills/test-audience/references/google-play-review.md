# Google Play review checklist

**Snapshot:** official Play Console Help pages read on 2026-11-23. Reopen them before relying on this list. Play's crawler, the pre-launch report, already runs on uploaded builds. Read its crashes and accessibility results if the owner shares them, and spend this walkthrough on what a crawler misses.

Sources:
- [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455)
- [Account deletion](https://support.google.com/googleplay/android-developer/answer/13327111)
- [Target API level](https://support.google.com/googleplay/android-developer/answer/11926878)
- [Closed testing for new personal accounts](https://support.google.com/googleplay/android-developer/answer/14151465)
- [Pre-launch report](https://support.google.com/googleplay/android-developer/answer/9842757)
- [Developer Program Policy](https://support.google.com/googleplay/android-developer/topic/9858052)

## A. Blockers a walkthrough can test

- **App access.**
  - **What to provide:** if any part of the app needs a login, the owner must provide access details in the Play Console under App content. There's room for up to five sets of instructions, plus a field for one-time passwords, multi-factor sign-in or unusual logins.
  - **What to test:** the provided details work on a clean install and reach every restricted feature.
  - **Codes:** a login that needs a code sent to the developer's phone is a failure unless the instructions explain how a reviewer gets past it.
- **Account deletion.** If users can create an account, both of these must exist:
  - **In-app path:** a way inside the app to delete the account and its data.
  - **Web link:** works without reinstalling the app, names the app or developer, and explains any extra steps (such as cancelling a subscription first). Open the link and follow it.

  Data kept for security, fraud or legal reasons must be disclosed. Check that the privacy policy mentions it.
- **Privacy policy.**
  - **In the app:** a link that opens a public web page, not a PDF.
  - **On the listing:** a link too.
  - **Reachability:** works without logging in and isn't geo-blocked.
- **Data safety matches behavior.**
  - **Permissions:** compare the permissions the app requests during the walkthrough, and the data the walkthrough shows it collecting or sharing (from the network log: destinations and kinds of data, never the contents), against the Data safety answers the owner provided.
  - **Mismatches** are findings. That includes SDKs calling out before any user action.
- **Permissions in use.**
  - **Justified:** each runtime permission prompt matches a feature the user just tried to use.
  - **Denial:** the app still works without it, except for that feature.
  - **Sensitive permissions:** SMS, Call Log, all-files access, background location and similar need a Play declaration. Note each one you see and mark the declaration CHECK IN CONSOLE.
- **Ads.** If ads appear, the owner's ads declaration must say Yes. Ads mustn't be deceptive or interrupt unexpectedly (Developer Program Policy, Ads).
- **Stability.** No crashes or "app isn't responding" dialogs (ANRs) on the core flow. Include a back-button and gesture-navigation pass, rotation and process death: background the app, let the system reclaim it, then return.
- **Listing accuracy.** The description, screenshots and short description match the build. Features the listing claims are reachable. No misleading claims or other apps' names or brands (Developer Program Policy, Metadata).
- **Families.** If the target audience includes children, flag that the Families policy applies. Check that ads and data collection look appropriate, and leave the final call to the owner.
- **Content users create, and AI.**
  - **User-generated content:** reporting, blocking and moderation are visible.
  - **AI-generated content:** a way to report or flag offensive output. Re-read the current Developer Program Policy sections at run time; this snapshot doesn't quote them.

## B. Engineering readiness

- **Devices:** a small phone, a large phone and a tablet if supported, on the oldest and newest supported Android versions available on this surface.
- **System settings:** dark theme, the largest font size and display size, and a TalkBack label spot check.
- **Network:** offline and slow network show understandable errors and a retry.
- **Billing:** purchase and restore through Play Billing with a licensed test account, where the surface supports it. Otherwise mark it NOT TESTABLE HERE.

## CHECK IN CONSOLE (the app can't show these)

- **Target API level:** on 2026-11-23 the help page said new apps and updates must target Android 16 (API 36) from August 31, 2026, with extensions to November 1, 2026. Both dates have passed, so re-read the current requirement.
  - **What to compare:** the build's `targetSdkVersion`, which a reviewer also sees, can be read from the APK with `aapt dump badging` or `apkanalyzer` without touching source.
- **App content forms:** content rating questionnaire, target audience, ads declaration, Data safety form, permissions declarations.
- **Closed testing for new personal accounts:** accounts created after November 13, 2023 need a closed test with at least 12 testers opted in continuously for 14 days before applying for production. The application asks about recruiting testers, feedback and changes made. It's a process gate, not app behavior. Flag it if it applies, and note that this walkthrough doesn't count as that test.

## Draft App access instructions (fill from the walkthrough)

1. How to sign in: a credentials placeholder, how to get past any one-time code or MFA, and the login fields.
2. Where each restricted or paid feature is.
3. Anything region-specific or hardware-specific the reviewer needs.
