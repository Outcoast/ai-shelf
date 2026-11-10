# ai-shelf

Check if ChatGPT, Gemini, Perplexity and Google AI Mode recommend your brand. By hand, in about 1 hour, for free.

1 shopper question. 4 AIs. 5 fresh chats each. 20 answers in a spreadsheet.

```
$ python3 tally.py examples/vitamin-c/runs.csv

AI SHELF  20 answers · 4 AIs · 16 brands named · 3 different #1s

BRAND            NAMED              #1  ChatGPT  Gemini   AI Mode  Perplex
Timeless         18/20  █████████   12  3/5      5/5      5/5      5/5
Maelove          9/20   █████       3   0/5      3/5      5/5      1/5
...
Geek & Gorgeous  6/20   ███         5   5/5      1/5      0/5      0/5
```

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The method, step by step. Works as a Claude skill too |
| `tally.py` | Turns your runs into a leaderboard. Python 3, no dependencies |
| `templates/` | Empty `runs.csv`, `sources.csv` and `setup.md` to fill |
| `examples/vitamin-c/` | A real run: "What's the best vitamin C serum under $40?" (Nov 1, 2026) |

## Use it

```
git clone https://github.com/Outcoast/ai-shelf
cd ai-shelf
cp templates/*.csv .
# run your prompt 5x in each AI, log the brands in runs.csv
python3 tally.py runs.csv --brand "Your Brand" --sources sources.csv
```

No terminal? Click **Code > Download ZIP**, fill the 2 CSVs in Google Sheets or Excel, or use the Claude skill below.

As a Claude skill: copy the folder to `~/.claude/skills/ai-shelf/`, then paste each AI answer into Claude and ask it to log it. It writes the CSV rows for you.

## The 5 rules

1. Write the question in shopper words, with their price or constraint. Never your brand name.
2. 4 AIs, because your customers don't all live in ChatGPT.
3. 5 fresh chats per AI, memory off. Never regenerate in the same chat.
4. Score = how many of the 20 answers name you. Rank inside 1 answer moves too much.
5. Log every source. That list is your todo list.

## License

Method and docs: CC BY 4.0. Code: MIT. Use it on your brand, your clients, your agency deck, just credit the source.
