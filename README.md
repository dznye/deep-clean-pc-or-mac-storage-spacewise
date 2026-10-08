# Deep Clean PC or Mac Storage - SpaceWise

**Find what is taking up space on your PC, find hidden files and caches, and clean them safely.**
Everything you remove goes to the Recycle Bin first, so nothing is gone for good.

> Searching for *"what to delete when C drive is full"*, *"C drive full for no reason"*, *"how to find hidden files taking up space"* or *"how to clean my PC storage"*? This is built for exactly that.

**Website and download page:** https://fuidzy.com/deep-clean-pc-or-mac-storage

## Download

Get **SpaceWise.exe** from the [Releases page](../../releases/latest) and double-click it. Your browser opens the app: click **Scan my profile**.

| Platform | Status |
|---|---|
| Windows 10 / 11 | Available |
| macOS | Experimental build coming (not tested on a real Mac yet) |

**"Windows protected your PC"?** The app is new and not code-signed yet. Click **More info -> Run anyway**. To verify your download, compare its SHA-256 hash with the one listed on the release:

```
certutil -hashfile SpaceWise.exe SHA256
```

## Pricing

- **7-day free trial**, everything unlocked.
- After that, scanning, the bubble map and the hidden-files finder stay **free**. Cleaning needs a license: **$12.99 one-time**, works on 2 devices, 30-day refund.
- Your license code is **emailed to you right after you buy** (check spam). In the app click *Enter license code*, paste it, done.

[Buy SpaceWise - $12.99](https://checkout.dodopayments.com/buy/pdt_0NpJ6SuSJI4BY5AYVFPb0?quantity=1)

## What it does

- **Linked bubble map** - a floating, draggable map of what is using space. Big folders link to what is inside them. Colors show file type.
- **Quick clean** - labeled groups (temp files, crash dumps, shader and browser caches, package-manager caches, Gradle, AI model caches, Android emulator images). Each is tagged **Safe**, **Check first** or **Slower next build**.
- **Hidden files finder** - the biggest hidden files and folders on your drive.
- **Old and big files** - files over 50 MB you have not touched in 6+ months.
- **Chain-reaction cleanup** - select a big bubble and everything linked to it goes; select a small one to remove just that item.

## Safe by design

- Runs **only on your computer**. Nothing is uploaded.
- Deletes **only by moving to the Recycle Bin** (Windows will warn you if something is too big for it).
- Only touches paths it showed you, and **blocks** Windows, Program Files, ProgramData, your Documents / Desktop / Pictures / Music / Videos / Downloads folders themselves, and `.ssh`, `.gnupg`, `.aws`.
- Never follows junctions or symlinks.
- If some folders cannot be read, it tells you how many and offers a **Run as administrator** button. System folders stay protected even then.

## Support

Open an [issue](../../issues) or see the website for contact details.

## Terms

See [EULA.md](EULA.md). This repository contains the website and release downloads; the application source code is not published.
