---
name: ai-shelf
description: Get a brand recommended and cited by ChatGPT, Gemini, Perplexity and Google AI Mode for the shopper questions that matter. Use when someone asks how to get their brand mentioned by ChatGPT or AI search, wants a GEO / AI visibility plan, wants to know why a competitor gets recommended instead of them, or pastes AI answers about their category. Runs a baseline (the AI Shelf test), finds the sources and the sentences the AIs repeat, then writes the fixes: product page copy, the one-liner, and outreach to the sites the AIs read.
---

# AI Shelf

AIs don't rank brands. They repeat what their sources agree on.

In a 20-answer test on "What's the best vitamin C serum under $40?", Timeless was named in 18 answers across all 4 AIs. It was Wirecutter's budget pick, it showed up in dermatologist YouTube videos and Reddit threads, and the AIs called it "the budget dupe for SkinCeuticals". Someone wrote that line once. Now the AIs say it for them.

This skill helps the user become that brand for their own category. It runs in 5 steps. Do them in order, and don't skip step 1: every fix later depends on which sources the AIs actually read.

Always work from the user's real data (pasted answers, their product pages, their claims). Never invent a source, a review, a stat or a citation.

## Step 1: the shelf (baseline)

Goal: know who the AIs recommend today, and from which sources.

1. Ask the user for their brand, their hero product and its price, and who buys it. Read their product page if they give a URL or paste it.
2. Write 3 shopper questions with them, in the words a real customer types. Rules:
   - casual, with the constraint a shopper includes (a price, a skin type, a use case): `What's the best vitamin C serum under $40?`
   - never the brand name or a competitor's name in the prompt
   - English if the market is the US
   - pick 1 as the main question; the other 2 are for later runs
3. Give them the run protocol (see `references/run-protocol.md`): ChatGPT and Gemini in temporary chats, Perplexity logged in, Google AI Mode with `udm=50&hl=en&gl=us`. 5 fresh chats per AI on the main question = 20 answers. New chat every run, never "regenerate".
4. As they paste each answer (text or screenshot), log it yourself in 2 tables:
   - **Brands**: AI, run, position, brand (normalize spellings, 1 row per brand, skip brands only mentioned as a comparison)
   - **Sources**: AI, run, source, type (media, retailer, brand site, blog, reddit, youtube, instagram, tiktok, review site, other)
   - **Phrases**: any short description the AI attaches to a brand ("budget dupe for X", "dermatologist favorite", "best for sensitive skin")
5. When the 20 answers are in, show the shelf:
   - each brand: named X/20, times #1, per-AI split (e.g. ChatGPT 5/5, Google 0/5)
   - the user's brand, even at 0/20
   - 1 line on what surprised you

If the user can't run all 20, work with what they have and say the result is a snapshot.

## Step 2: read the sources

Goal: the list of sites that decide the shelf.

1. Rank sources by how many of the 4 AIs cite them, then by how many answers.
2. For the top 10, note: which brands they recommend, whether the user's brand is on them, and what kind of fix would get it there (`references/source-playbook.md`).
3. Flag the sources cited by 2+ AIs. Those are the priority: 1 placement there moves several AIs at once.

Output a table: source, cited by which AIs, in X answers, user's brand present (yes/no), competitor on it, fix type.

## Step 3: find the sentence

Goal: the 1 line the AIs should repeat about the user's brand.

1. List the phrases the AIs repeated about the top 3 brands (from the Phrases log). Find where each one comes from (usually 1 editorial pick or 1 comparison that got copied).
2. Write 3 candidate one-liners for the user's product. Each one must be:
   - specific and checkable (a % of active, a price, a comparison, a test result, an award)
   - short enough to be quoted in 1 clause (under 12 words)
   - true today, with proof the user can show
   - comparative when possible ("the $25 alternative to X", "the only Y under $Z with W")
3. Help the user pick 1. That line goes on their pages (step 4) and into every pitch (step 5).

Never write a claim the user can't prove. For cosmetics, keep claims cosmetic (no medical or drug claims).

## Step 4: fix your own pages

Goal: pages an AI can read and quote. Use `references/page-checklist.md`.

For the hero product page, write:
- an answer block at the top: 2-3 sentences that answer the shopper question directly, including the one-liner, the price, the key spec, and who it's for
- a short FAQ with the real shopper questions from step 1 as headings
- a comparison section if the one-liner is comparative (honest, factual)
- the same claims, word for word, for the Amazon listing and each retailer page the user sells on (list the differences you find)

Deliver the copy ready to paste, plus a list of what to change on each page.

## Step 5: get on the sources

Goal: the user's brand on the sites from step 2, in order of priority.

For each priority source, write the next action and the draft (`references/source-playbook.md`):
- editorial lists and reviewers: a short pitch to the editor, with the one-liner, the proof, and a sample offer
- YouTube and TikTok creators the AIs cite: a seeding message, no script imposed, disclosure required
- Reddit: what to do and what never to do (no fake accounts, no planted posts, answer as the brand openly)
- retailers and review sites: listing copy, how to get honest reviews where the AI reads them
- the user's own channels: 1 post or page that states the one-liner with proof, so it exists somewhere quotable

Hard rules: no fake reviews, no undisclosed paid placements, no sockpuppets. They break platform rules, they break the law in many markets, and AIs increasingly discount them.

## Then: the plan, and the re-run

Close with a 1-page plan:
1. the shelf today (score per AI)
2. the one-liner
3. page fixes (done / to do)
4. top 5 sources with the action and owner for each
5. re-run date: same question, same settings, 2 weeks later. Compare scores and sources.

Be honest about timing: page fixes can show up within weeks, editorial placements take longer, and some AIs refresh slower than others. Nobody can guarantee a citation. The plan raises the odds, and the re-run shows if it worked.
