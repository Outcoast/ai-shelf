# ai-shelf

A free Claude skill that helps your brand get recommended by ChatGPT, Gemini, Perplexity and Google AI Mode.

AIs don't rank brands. They repeat what their sources agree on. This skill finds those sources, finds the sentence the AIs repeat about the winners, and writes your fixes.

## What it does

1. **The shelf**: 1 shopper question, 4 AIs, 5 fresh chats each. You paste the answers, Claude logs who gets named and from which sources.
2. **The sources**: the sites that decide your shelf, ranked by how many AIs read them.
3. **The sentence**: the 1-line claim the AIs should repeat about you (specific, provable, quotable).
4. **Your pages**: an answer block, FAQ and consistent claims for your product page, Amazon and retailers. Ready to paste.
5. **The outreach**: pitches to the editors, creators and communities the AIs cite. No fake reviews, no sockpuppets.

Then a 1-page plan and a re-run date to see if it moved.

## Install

**Claude.ai / Claude Desktop**: download this repo as a zip and upload it as a skill in Claude's settings (skills need to be enabled on your plan).

**Claude Code**:
```
git clone https://github.com/Outcoast/ai-shelf ~/.claude/skills/ai-shelf
```

Then ask Claude: *"Run the AI Shelf on my brand"* and give it your product page.

## What's inside

| File | What it is |
|---|---|
| `SKILL.md` | The 5 steps Claude follows |
| `AGENTS.md` | How to run it with any other AI agent (ChatGPT, Gemini, Cursor, Codex) |
| `references/run-protocol.md` | How to run the 20 answers (settings per AI) |
| `references/source-playbook.md` | What to do per source type, with a pitch template |
| `references/page-checklist.md` | Product page checklist and answer block template |
| `templates/setup.md` | Log your run setup |
| `examples/vitamin-c/` | A real run: 20 answers on "What's the best vitamin C serum under $40?", with the worked steps 1 to 3 in `shelf.md` |

## Honest part

Nobody can guarantee a citation. This raises your odds and shows you, every 2 weeks, if it's working.

## License

CC BY 4.0. Use it on your brand, your clients, your agency deck, just credit the source.
