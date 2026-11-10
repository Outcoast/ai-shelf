---
name: ai-shelf
description: Run an AI Shelf test, the manual method for measuring whether ChatGPT, Gemini, Perplexity and Google AI Mode recommend a brand for a real shopper question. Use when someone wants to check their AI visibility, write the shopper prompt, log AI answers into runs.csv and sources.csv, tally the results, or turn the cited sources into a todo list.
---

# AI Shelf

1 shopper question. 4 AIs. 5 fresh chats each. 20 answers in a spreadsheet.

The point: 1 screenshot tells you what 1 AI said in 1 chat on 1 afternoon. 20 answers tell you who actually owns the shelf, and the sources tell you why.

## Step 1: write the prompt (shopper words)

Write the question the way a real customer types it. Rules:

- 1 question, typed casually, in the shopper's words (not your marketing words)
- include the constraint they'd include: a price, a skin type, a use case ("under $40", "for dry skin")
- never put your brand name or a competitor's name in the prompt
- no "act as an expert", no system-style instructions
- in English if your market is the US, even if you're not

Good: `What's the best vitamin C serum under $40?`
Bad: `List the top 10 vitamin C serum brands with their market positioning`

If the user gives a brand-centric prompt, rewrite it into shopper words and explain the change in 1 line.

## Step 2: set up the 4 AIs

| AI | Setting |
|---|---|
| ChatGPT | Temporary chat (memory off), default model |
| Gemini | Temporary chat, default model |
| Perplexity | Logged in (logged-out answers get blocked), default model |
| Google AI Mode | `https://www.google.com/search?udm=50&hl=en&gl=us&q=<prompt>` |

Write down: date, city you ran it from, logged in or not, model names. Location changes the sources.

## Step 3: run it 5 times per AI

- New chat for every run (never regenerate inside the same chat)
- Paste the exact same prompt
- Screenshot or copy every answer before closing it

## Step 4: log every answer

`runs.csv` = 1 row per brand named, in the order the AI listed it:

```
engine,run,position,brand
ChatGPT,1,1,Geek & Gorgeous
ChatGPT,1,2,Timeless
```

`sources.csv` = 1 row per source the AI cited:

```
engine,run,source,type
ChatGPT,1,NBC News,media
```

Use `type` from: media, retailer, brand site, blog, reddit, youtube, instagram, tiktok, review site, other.

When the user pastes an AI answer, extract both tables for them. Rules:
- normalize brand names (same spelling every time: "e.l.f." not "elf" and "e.l.f. SKIN")
- 1 brand per row even if the AI names 2 products from it (keep the first position)
- a brand mentioned only as a comparison ("a dupe for SkinCeuticals") is not named, skip it
- if the AI picks no winner, position = the order it listed them
- if an answer names no brand at all, log 1 row with brand `-` so it still counts in the 20

## Step 5: tally

```
python3 tally.py runs.csv --brand "Your Brand" --sources sources.csv
```

Read it like this:
- NAMED out of 20 is the score. Position inside 1 answer moves too much to mean anything.
- #1 shows who each AI crowns.
- The per-AI columns show where you're missing. 5/5 on one AI and 0/5 on another is common.

## Step 6: read the sources

Sort `sources.csv` by how often each source appears. The sources cited across several AIs are the ones that decide the shelf. That list is the todo list: get reviewed there, get listed there, fix the claims there.

## Step 7: repeat

Same prompt, same settings, every 2 weeks. Keep every CSV with the date in the filename (`2026-11-01-runs.csv`). The trend is what you report, never 1 run.

## Honesty rules

- 20 runs is a snapshot. Call it a test, never a study.
- Always publish the setup (date, location, login, model) next to the numbers.
- If an AI was blocked or swapped, say so.
