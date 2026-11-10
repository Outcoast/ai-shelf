---
name: ai-shelf
description: See which brands ChatGPT, Gemini, Perplexity and Google AI Mode recommend for a real shopper question, and which sources they cite. Use when someone wants to check their AI visibility, asks why a competitor gets recommended instead of them, wants to know which sites the AIs read for their category, or pastes AI answers about their category. Runs the AI Shelf test (1 question, 4 AIs, 5 fresh chats each) and returns a brand leaderboard and a ranked list of the sources the AIs cite.
---

# AI Shelf

AIs don't rank brands. They repeat what their sources agree on.

In a 20-answer test on "What's the best vitamin C serum under $40?", Timeless was named in 18 answers across all 4 AIs. TODAY and Allure were each cited by 3 of the 4 AIs, Wirecutter by 2.

This skill shows the user who owns the shelf for their question today, and which sources the AIs read to decide it. It runs in 2 steps. Do them in order.

Always work from the user's real data (pasted answers and screenshots). Never invent a brand, a source, a quote or a citation.

## Step 1: the shelf

Goal: know who the AIs recommend today.

1. Ask the user for their brand, their product category, its price range, and who buys it.
2. Write 3 shopper questions with them, in the words a real customer types. Rules:
   - casual, with the constraint a shopper includes (a price, a skin type, a use case): `What's the best vitamin C serum under $40?`
   - never the brand name or a competitor's name in the prompt
   - English if the market is the US
   - pick 1 as the main question; the other 2 are for later runs
3. Give them the run protocol (see `references/run-protocol.md`): ChatGPT and Gemini in temporary chats, Perplexity logged in, Google AI Mode with `udm=50&hl=en&gl=us`. 5 fresh chats per AI on the main question = 20 answers. New chat every run, never "regenerate".
4. As they paste each answer (text or screenshot), log it yourself in 2 tables:
   - **Brands**: AI, run, position, brand (normalize spellings, 1 row per brand, skip brands only mentioned as a comparison)
   - **Sources**: AI, run, source, type (media, retailer, brand site, blog, reddit, youtube, instagram, tiktok, review site, other)
5. When the 20 answers are in, show the shelf:
   - each brand: named X/20, times #1, per-AI split (e.g. ChatGPT 5/5, Google 0/5)
   - the user's brand, even at 0/20
   - 1 line on what surprised you

If the user can't run all 20, work with what they have and say the result is a snapshot.

## Step 2: the sources

Goal: the list of sites the AIs read for this question.

1. Rank sources by how many of the 4 AIs cite them, then by how many answers.
2. For the top 10, note which brands each one recommends (if the user shares the page or you can open it) and whether the user's brand is on it.
3. Flag the sources cited by 2+ AIs. Those weigh on several AIs at once.

Output a table: source, type, cited by which AIs, in X answers, brands it recommends, user's brand present (yes/no).

## Then: the summary and the re-run

Close with:
1. the shelf today (score per AI, the user's brand included)
2. the top 3 competitors, and on which AIs each one is strongest
3. the top 10 sources, with the ones cited by 2+ AIs flagged
4. re-run date: same question, same settings, 2 weeks later. Compare scores and sources.

20 answers is a snapshot. Call it a test, never a study, and always show the setup (date, location, login, model) next to the numbers.
