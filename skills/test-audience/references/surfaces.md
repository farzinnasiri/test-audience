# Surfaces: how to touch the app, and what each can't test

Pick the surface **after** checking which tools are installed in this runtime. Names below are examples, not requirements. Use whatever user-like driver is available and record its name and version in the report.

## Detecting tools (read-only checks)

- **Web:** a browser automation CLI or MCP server, such as `agent-browser`, Playwright MCP or a built-in browser tool.
- **iOS Simulator:** `xcrun simctl list devices booted`, plus a UI driver such as mobile-mcp, Maestro (it has a built-in MCP server), Callstack's agent-device or AXe.
- **Android emulator or device:** `adb devices` and `emulator -list-avds`, plus a UI driver such as mobile-mcp, Maestro or agent-device.
- **Cloud device:** only when the owner already has an account with a service such as BrowserStack, Firebase Test Lab, AWS Device Farm or Appetize. Uploading a build there is an external action and needs explicit approval.
- **Computer use:** a desktop-control tool that sees the screen and moves the pointer. It's the fallback for anything with a window, including a mirrored phone screen.

If nothing fits the app, stop and name what to install. Never pretend a run happened.

## Surface matrix

| Surface | Good for | NOT TESTABLE HERE (report it, never pass it) |
|---|---|---|
| Desktop browser, desktop viewport | Web apps, marketing site, pricing, web checkout in test mode | Mobile layout and touch, anything native |
| Desktop browser at a phone viewport (375×812, touch emulation) | Responsive web, mobile web onboarding | Real touch physics, native gestures (edge swipe-back, long-press menus, pinch fidelity), the on-screen keyboard covering inputs, real-device performance, OS permission sheets, push, in-app purchase, biometrics, deep or universal links, app lifecycle (background, kill, restore) |
| Expo or React Native **web build** in a browser | Quick look at flows and copy | All of the row above, **and** it uses a different renderer (react-native-web), so layout, fonts, scrolling and native modules can behave differently from the iOS and Android apps. Never treat it as evidence about the native apps. |
| iOS Simulator | Native flows, layout across device sizes, Dynamic Type, dark mode, locale, permission dialogs, deep links, simulated push, StoreKit testing with a local config | Real camera, the real App Store purchase flow, TestFlight builds (the simulator needs a simulator build), real performance and thermals, some hardware (NFC, Bluetooth), true VoiceOver use. Face ID and location are simulated only. |
| Android emulator | Native flows, screen sizes, permissions, back button and gesture navigation, locale, process death | Real camera and sensors, Play Billing without a Play image and a licensed tester, real performance, OEM skins |
| Real device over a cable, or a cloud real device | Closest to users: performance, keyboard, real touch, the TestFlight or internal-track build | Some cloud services restrict purchases, push or biometrics. Check the service and list what's blocked. |
| Computer use (screen and pointer) | Anything with a window, including apps with no automation hooks | Slower and less precise. Gestures are limited to what the pointer can do. Never drive the owner's personal phone or accounts without a separate explicit yes. |

## Lab controls (allowed, they aren't "using the app")

Viewport and orientation, network throttling (slow 3G or offline), locale and language, light or dark mode, text size, resetting or revoking permissions, clearing app data or reinstalling, simulated location, simulated push, and the clock or time zone.

If a control is unavailable on this surface (for example, no network throttling), the persona that needs it reports that part as `NOT TESTABLE HERE`.

## Observation (allowed, read-only)

Screenshots, screen recording, the accessibility tree or snapshot, console errors, the network log (status codes and timing, never response bodies containing personal data), and read-only checks such as `document.documentElement.scrollWidth > window.innerWidth`.

Observation never changes app state.

## Parallelism

- **Web:** personas may run in parallel only with separate browser profiles or sessions and separate test accounts.
- **One simulator or emulator:** run personas one at a time, clearing app data in between.
- **Several devices:** booting several simulators or emulators allows parallel runs, but each needs its own test account. Machines run out of memory quickly, so prefer sequential runs when in doubt.
