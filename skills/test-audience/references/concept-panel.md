# Mode: concept-panel

Answer: among a few concepts, landing pages, paywalls, prices or positioning lines, which ones should go in front of real people first, and what objections should we expect?

Every output carries the label **SYNTHETIC HYPOTHESIS: not user validation**.

## What the evidence supports, and what it doesn't

- **The method.** Semantic Similarity Rating (SSR) comes from [Maier et al., 2025 (arXiv:2510.08338)](https://arxiv.org/abs/2510.08338), PyMC Labs with Colgate-Palmolive. An LLM conditioned on a consumer persona reads a product concept and writes a free-text purchase-intent statement. That text is then mapped to a 1–5 distribution by embedding similarity to anchor statements.
- **The reported result.**
  - **Data:** 57 personal-care product concept surveys with about 9,300 human responses.
  - **Ranking:** SSR reached about 90% of human test-retest reliability in ranking concepts.
  - **Distributions:** its response distributions were realistic (KS similarity above 0.85).
  - **Direct ratings:** asking the model for a number directly gave narrow, unrealistic distributions.
- **What that doesn't cover.**
  - **Panel level only:** it's agreement at the level of the whole panel, on hypothetical concepts in one consumer category, against stated intent.
  - **Untested territory:** it isn't individual prediction, real purchasing, software or app experience, B2B, or your audience.
  - **No calibration here:** the paper calibrated against real survey data, and you don't have that here.
- **The counter-evidence.** Independent 2026 studies found synthetic respondents flatter than people, less likely to say "not sure", and prone to inventing relationships in the data:
  - Pew Research Center, "Can AI stand in for human survey-takers?";
  - ["Plausible but Not Valid", arXiv:2608.14606](https://arxiv.org/abs/2608.14606).

So use the panel for **relative screening and finding objections**. Never use it for absolute demand, conversion rates, market size, or claims about how a real demographic behaves.

## Inputs (part of the run plan)

- **Variants.** Two to five, each shown as the user would see it: a concept card, a landing page or paywall screenshot captured through the browser, or a positioning line. Capturing from the live app follows the same outside-only rules as every mode.
- **The question.** For example "How likely are you to try this?", or "…to pay <price> per month for this?". Pick one per run; trying and paying are different questions.
- **Segments.** One to four, defined by the owner from their real target audience, such as "freelance designers who invoice monthly". Each segment is described by its situation and current alternative, not by a demographic stereotype.
- **Sample size.** At least 30 respondents per variant per segment, so the spread is visible. More respondents reduce noise, but they don't reduce model bias.

## Running the panel

1. **One variant per respondent.** Each respondent sees only one variant, so respondents never compare.
2. **Persona conditioning.** Write each respondent as an individual inside the segment: a name-free profile with their situation, the current way they solve the problem, budget sensitivity, and one or two specifics that vary between respondents.
3. **Ask for words, not numbers.** The prompt shows the variant, asks the question, and asks for a short honest reaction in their own words, including what would stop them. Never ask for a rating, because direct numbers are exactly what the paper found unreliable.
4. **Generate in independent batches.** Use separate subagents or calls per batch (for example 10 respondents for one variant and segment), with instructions to vary the reactions. Responses from one context are correlated; disclose how the batches were made.
5. **Score with SSR.**
   - **With Python:** run the bundled script:
     ```
     uv run --python 3.12 --with "semantic_similarity_rating @ git+https://github.com/pymc-labs/semantic-similarity-rating.git" <this skill's directory>/scripts/ssr_rate.py panel.json
     ```
   - **Input:** `panel.json` holds `responses` (variant, segment, text) and optional `anchor_sets`.
   - **What it does:** the script uses PyMC Labs' reference package. It embeds locally with sentence-transformers (the default model is `all-MiniLM-L6-v2`; the first run downloads it) and averages over the anchor sets.
   - **Anchors:** the bundled anchor sets are authored defaults for "try or get this". They're not the paper's sets. Write new ones when the question is about paying a specific price, and report which anchors were used.
   - **If Python or the model can't run:** skip the numbers entirely and deliver only the qualitative objection analysis. Never estimate scores by eye.
6. **Code the objections.** Cluster the "what would stop me" statements per variant into themes. Count how many respondents raised each one and quote two or three verbatim.

## Reading the result

- **Rank variants by expected score**, but call a winner only when its 90% interval doesn't overlap the next variant's. Otherwise say "no clear difference" and lean on the objections.
- **Segment differences** are hypotheses about who to recruit for real tests, not facts about those people.
- **Watch for the known failure modes:**
  - every variant scoring the same;
  - suspiciously polite, uniformly positive text;
  - objections that are generic ("too expensive") rather than specific to the variant.

  If you see any of these, say the panel didn't separate the variants.

## Output

- The label, the question, the variants, segments, sample sizes, the batch method, the embedding model and the anchor sets.
- The score table from the script, or "qualitative only" with the reason.
- The top objections per variant, with counts and quotes.
- A recommendation: which one or two variants to put in front of real users, and the smallest real test that would confirm or kill the leader. That could be five target-user interviews, a landing page split test with a real call to action, or a priced pre-order where it's lawful and the owner approves.
- The limits: one paragraph pointing back to "What the evidence supports" above.

No outreach, posting, ad spend or real-user contact happens in this mode.
