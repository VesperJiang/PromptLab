# Evaluation Plan

## Test Prompts Overview

We prepared 20 prompts to test PromptLab's optimization feature. These prompts cover four areas we often use AI for: writing, coding, office tasks, and learning.

## What We're Measuring

We looked at five things when evaluating each prompt:

| Criteria | What We Check |
|----------|---------------|
| Clarity | Is the task clearly described? |
| Completeness | Does it include all necessary details? |
| Role Setting | Does it tell the AI who it should act as? |
| Output Format | Does it specify how the output should look? |
| Constraints | Does it set limits like length or style? |

## How We Did It

1. We fed each original prompt into PromptLab
2. The system flagged missing elements
3. It generated an optimized version
4. We compared scores before and after

## What We Expect

From our survey, we know the most common missing elements are:
- Output format (53.33% of users mentioned this)
- Role setting (36.67%)
- Constraints (36.67%)

Based on these findings, here's what we expect to see:

| Metric | Original (Avg) | Optimized (Expected) |
|--------|----------------|---------------------|
| Clarity | 55/100 | 85/100 |
| Completeness | 40/100 | 80/100 |
| Role Setting | 30/100 | 75/100 |
| Output Format | 25/100 | 80/100 |
| Constraints | 20/100 | 70/100 |
| **Overall** | **34/100** | **78/100** |

## Caveats

We want to be honest about our limitations:
- We only tested 20 prompts, which is a small sample
- The scoring was automated, not reviewed by humans
- Our survey data came from 30 people, mostly students like us
- Results may look different for other types of prompts

## Final Thoughts

Despite the limitations, we believe PromptLab will make a real difference. The biggest improvements are likely to be in Output Format and Constraints — exactly the areas where our survey showed users struggle the most.

---
*I wrote this evaluation based on our survey results and test data. I used AI tools to help with wording and structure.*

## Real Case Comparison

We tested one typical bad prompt to see how much PromptLab could improve it.

### The Original Prompt

> 帮我写一篇文章

This is a real example of what we saw in our survey — users often write very short, vague prompts. This one has almost no useful information: no topic, no format, no length limit, and no role for the AI to play.

### The Optimized Version

After running it through PromptLab, we got this:

> You are a university writing instructor.
> 
> Please write a Chinese argumentative essay on "The Impact of AI on College Students' Learning Habits."
> 
> Requirements:
> 1. Approximately 800 words
> 2. Structure: introduction, body, and conclusion
> 3. Formal tone
> 4. At least 3 key arguments
> 5. Output in Markdown format

### What Changed

The optimized version added most of what the original was missing. We got a clear role ("university writing instructor"), a specific topic ("AI and college learning"), a structure requirement, and a Markdown output format. We also got word count and tone constraints.

It's not perfect — the user still needs to confirm their topic and audience — but it's much more usable than just "write an article."

### Score Comparison

We scored both versions using our five criteria. The original scored low on almost everything because it didn't specify any details. The optimized version did much better, especially on role setting, output format, and constraints — exactly the areas where our survey showed users struggle the most.

### What We Learned

From this test, we can see that PromptLab works well for fixing vague prompts. It won't replace the user's own thinking, but it helps them think about what they actually need from the AI. The biggest improvements come from adding role, format, and constraints — which makes sense, since those were the top missing elements in our survey.

*This comparison was written based on our own test results. AI assistance was used for translation and wording refinement.*
