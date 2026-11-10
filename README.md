# ai-shelf

A free Claude skill that shows which brands ChatGPT, Gemini, Perplexity and Google AI Mode recommend for a shopper question, and which sources they cite.

AIs don't rank brands. They repeat what their sources agree on. This skill shows you who is on the shelf for your question, and where the AIs got it from.

## What it does

1. **The shelf**: 1 shopper question, 4 AIs, 5 fresh chats each. You paste the answers, Claude logs who gets named and how often.
2. **The sources**: the sites the AIs cite, ranked by how many AIs read them, and which brands each one recommends.

Then a summary and a re-run date, so you can track it every 2 weeks.

## Install

**Claude.ai / Claude Desktop**: download this repo as a zip and upload it as a skill in Claude's settings (skills need to be enabled on your plan).

**Claude Code**:
```
git clone https://github.com/Outcoast/ai-shelf ~/.claude/skills/ai-shelf
```

Then ask Claude: *"Run the AI Shelf on my category"* and tell it your brand and product.

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The 2 steps Claude follows |
| `AGENTS.md` | How to run it with any other AI agent (ChatGPT, Gemini, Cursor, Codex) |
| `references/run-protocol.md` | How to run the 20 answers (settings per AI) |
| `templates/setup.md` | Log your run setup |
| `examples/vitamin-c/` | A real run: 20 answers on "What's the best vitamin C serum under $40?", with the results in `shelf.md` |

## Honest part

20 answers is a snapshot, not a study. Re-run every 2 weeks with the same question to see the trend.

## License

CC BY 4.0. Use it on your brand, your clients, your agency deck, just credit the source.
