# AGENTS.md

How to use this repo if you are an AI agent (Claude, ChatGPT, Gemini, Cursor, Codex, or any other).

## What this is

AI Shelf: a method to get a brand recommended by ChatGPT, Gemini, Perplexity and Google AI Mode. You guide the user through 5 steps: measure the shelf, read the sources, find the sentence, fix their pages, get on the sources.

## How to run it

1. Read `SKILL.md` in full. It is your instructions. Follow the 5 steps in order and never skip step 1.
2. Open the reference files when a step points to them:
   - `references/run-protocol.md`: step 1, how the user runs the 20 answers
   - `references/source-playbook.md`: steps 2 and 5, what to do per source type, pitch template
   - `references/page-checklist.md`: step 4, product page checklist and answer block
3. Use `examples/vitamin-c/` to see what good output looks like. `shelf.md` shows steps 1 to 3 on a real run. `runs.csv` and `sources.csv` show the log format.
4. Give the user `templates/setup.md` to record their run settings.

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
- Also note the short phrases the AI attaches to each brand. Step 3 needs them.

Count the shelf yourself: for each brand, how many of the 20 answers name it, how many times it is #1, and the split per AI. Always show the user's brand, even at 0/20.

## Hard rules

- Work only from the user's real data. Never invent a source, a review, a stat, a quote or a citation.
- Never write a claim the user can't prove. For cosmetics, keep claims cosmetic, never medical.
- No fake reviews, no sockpuppet accounts, no undisclosed paid placements, no planted Reddit posts. Refuse and explain why.
- Call a 20-answer run a test, never a study. Nobody can guarantee a citation.

## If you are editing this repo

- `examples/vitamin-c/` is real data from Nov 1, 2026. Never change the numbers.
- Don't change the method's rules in `SKILL.md` without the maintainer's OK.
- Style: plain English, short sentences, numbers as digits, no em dashes. Keep the README short.
- License: CC BY 4.0. Keep the credit to outcoast.
