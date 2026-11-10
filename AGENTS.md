# AGENTS.md

How to use this repo if you are an AI agent (Claude, ChatGPT, Gemini, Cursor, Codex, or any other).

## What this is

AI Shelf: a test that shows which brands ChatGPT, Gemini, Perplexity and Google AI Mode recommend for a shopper question, and which sources they cite. You guide the user through 2 steps: measure the shelf, then read the sources.

## How to run it

1. Read `SKILL.md` in full. It is your instructions. Follow the 2 steps in order.
2. Give the user `references/run-protocol.md` so they run the 20 answers the same way every time.
3. Give the user `templates/setup.md` to record their run settings.
4. Use `examples/vitamin-c/` to see what good output looks like. `shelf.md` shows both steps on a real run. `runs.csv` and `sources.csv` show the log format.

The user runs the 20 answers by hand in each AI and pastes them to you. Do not run the AIs yourself unless the user asks and you can open a fresh, logged-out, memory-off chat for each run. Answers from your own memory don't count.

## Logging the answers

Keep 2 tables as the user pastes answers, in the same format as the example CSVs:

```
engine,run,position,brand
ChatGPT,1,1,Geek & Gorgeous
```

```
engine,run,source,type
ChatGPT,1,NBC News,media
```

- Use the same spelling for a brand every time.
- 1 row per brand per answer, at its first position.
- Skip brands only mentioned as a comparison ("a dupe for SkinCeuticals").
- If an answer names no brand, log 1 row with brand `-` so it still counts.

Count the shelf yourself: for each brand, how many of the 20 answers name it, how many times it is #1, and the split per AI. Always show the user's brand, even at 0/20.

## Hard rules

- Work only from the user's real data. Never invent a brand, a source, a quote or a citation.
- Call a 20-answer run a test, never a study. Show the setup (date, location, login, model) next to the numbers.

## If you are editing this repo

- `examples/vitamin-c/` is real data from Nov 1, 2026. Never change the numbers.
- Don't change the method's rules in `SKILL.md` without the maintainer's OK.
- Style: plain English, short sentences, numbers as digits, no em dashes. Keep the README short.
- License: CC BY 4.0. Keep the credit to outcoast.
