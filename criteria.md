# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

My questions target single, specific facts, like a dollar amount, a time interval, 
or a yes/no answer. Since my chunks are short and topic-focused, I expect this to 
hold for most questions, but I am not expecting 5 of 5 because a few of my documents, 
like the course pages, are similar enough that retrieval could pull the wrong one.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

This should hold 5 of 5 since the grounding prompt requires the source filename every 
time, and it costs nothing extra for the model to include it.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**

I expect the system to correctly refuse most of these questions, since they are about 
completely different topics than campus documents, and should not come back looking anything alike.

---

## 4. Something about your chunks

For at least 4 of 5 sampled chunks, each one starts right after a period or is the very 
beginning of a document, and ends with a period, question mark, or exclamation point.

**Why this target:**

My documents average 317 characters, and the fallback chunker almost never reaches its 
800 character cutoff, so most chunks are already whole documents. I expect this to hold 
most of the time, but I am not setting it at 5 of 5 in case my chunker introduces an edge 
case with a document that covers two separate topics.

---

## 5. Your choice

For at least 4 of my 5 test questions, the source named in the answer is the actual 
document that contains the answer, not just any document that got retrieved.

**Why this target:**

Some of the documents are similar in structure but different in content, which makes it easy 
for the system to retrieve the right topic but name the wrong document. A confidently wrong 
source is worse than the system simply admitting it does not know.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
