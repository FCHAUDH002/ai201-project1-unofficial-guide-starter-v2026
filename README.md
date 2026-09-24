# The Unofficial Guide

Name: Fatima Chaudhry
Corpus: campus_life

---

# Unit 1

## What This Does

The Unofficial Guide answers questions about campus life using the campus_life corpus, a set of short student 
posts about courses, housing, dining, and admin rules. You ask a plain question, like "Is ECON 101 curved?" or 
"How long is the wait at Verrill Street Grill?", and it finds the most relevant posts and answers from them. 
Every answer names the file it came from. If a question is outside what the posts cover, the system says it 
doesn't have enough information instead of guessing.

## Chunking Strategy

**Chunk size:**

 One paragraph per chunk. Paragraphs under 40 characters get merged into the next one.

**Overlap:**

No overlap.

When I read the campus_life posts, they were short, and many had a title line followed by one or two paragraphs. 
The starter's 800-character chunker never split anything, so every post was one chunk, even posts that covered two 
separate points. Splitting on paragraphs keeps each thought in its own chunk. The 40-character rule exists because 
titles like "On the add/drop deadline" are too short to mean anything alone, so I attach them to the paragraph they 
introduce. I used no overlap because I split at paragraph breaks, so a sentence is never cut in half.

## Sample Chunks

======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows asa W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

======================================================================
Chunk 2  |  source: course_cs_340_workload.txt#1  |  produced by: chunker.py::split_documents
======================================================================
It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

======================================================================
Chunk 3  |  source: course_phys_130_exams.txt#1  |  produced by: chunker.py::split_documents
======================================================================
The lab practical is worth 20% and almost nobody prepares for it.

======================================================================
Chunk 4  |  source: dining_verrill_street_grill_followup.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Re: Verrill Street Grill

Adding to what people have said about Verrill Street Grill. The wait figure of up to 30 minutes on Friday evenings matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

======================================================================
Chunk 5  |  source: housing_morrow_house.txt#1  |  produced by: chunker.py::split_documents
======================================================================
The good: cheapest housing tier by about $900 a year, and the singles are real singles.

## Sample Answer

**Question:**

Is ECON 101 curved?

**Answer:**

```
Yes, ECON 101 is curved, and generously. 

Source: `course_econ_101.txt` (and `course_econ_101_exams.txt`)

Sources retrieved: course_econ_101.txt, course_econ_101_exams.txt, course_econ_101_workload.txt, course_phys_130_exams.txt
```

**My relevance cutoff:**

Relevance cutoff: 0.6

| Question | In corpus? | Best distance |
|---|---|---|
| Verrill Street Grill wait | Yes | 0.147 |
| Campus shuttle frequency | Yes | 0.182 |
| Laundry at Calder Annexe | Yes | 0.218 |
| Printing quota rollover | Yes | 0.389 |
| ECON 101 curved | Yes | 0.522 |
| Capital of Mongolia | No | 0.821 |
| Diesel oil change | No | 0.885 |
| 1994 World Cup | No | 0.874 |
| Ibuprofen dosage | No | 0.824 |
| Rust for loop | No | 0.857 |

I kept the starter's default because it already sits in the gap in my results. My five in-corpus questions 
had best distances from 0.147 to 0.522. My five out-of-scope questions ranged from 0.821 to 0.885. The relevance 
cutoff of 0.6 lets every real question through and stops every off-topic one. The closest call is ECON 101 at 
0.522, which is only 0.078 under the cutoff.

## How I Used AI

**1.**

I asked Claude to check whether my criterion 4 could be tested from the sentence alone. I originally had 
"At least 4 of 5 sampled chunks contain a full sentence with no idea cut off mid-thought at either end."
It said "cut off mid-thought" is a judgment call, and two people could score the same chunk differently.  
It said to check if the chunk starts with a capital letter and ends with punctuation. I revised my 
criterion to drop the capital letter rule and just check that each chunk starts after a period or at the 
start of a document, and ends with punctuation.

**2.**

I pasted the best distances for five questions my documents cover and five they don't, and asked Claude 
where it would put the cutoff and what I would get wrong at that number. My in-corpus questions ranged 
from 0.147 to 0.522, and my out-of-scope questions ranged from 0.821 to 0.885. It said the default cutoff 
of 0.6 sits in the gap between the two groups. It also warned that my ECON 101 question was close at 0.522,
 so a vaguer version of a real question could land above 0.6 and get refused. I kept 0.6 because it separates
  all ten of my questions, with every in-corpus question below it and every out-of-scope question above it.

---

# Unit 2

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks start and end at sentence boundaries | 5/5 | 5/5 | 5/5 | MET |
| 5. The named source is the right document | 5/5 | 5/5 | 5/5 | MET |


Criterion 1 - Retrieved chunk contains the answer

Produced by store.py::search, chunks from chunker.py::split_documents

How much does laundry cost at Calder Annexe? - run 1

Best distance: 0.2182 (passed the gate)
Sources retrieved: housing_calder_annexe.txt, housing_calder_annexe_laundry.txt, housing_fenwick_court.txt, housing_innisfree_hall.txt, housing_morrow_house.txt

At Calder Annexe, laundry costs $2.00 for a wash and $1.75 for a dryer. 

This information comes from `housing_calder_annexe.txt` and `housing_calder_annexe_laundry.txt`.


Criterion 2 - Every answer names a source

Produced by generate.py, grounding instruction requires source filename.

How often does the campus shuttle run on weekdays? - run 1

Best distance: 0.1825 (passed the gate)
Sources retrieved: course_cs_210.txt, course_econ_101_workload.txt, course_stat_150_workload.txt, housing_aldridge_hall.txt, transit_shuttle.txt

The campus shuttle runs a loop every 20 minutes on weekdays, from 7am to 11pm. 

Source: transit_shuttle.txt


Criterion 3 - Gate stops out-of-corpus questions

Produced by run_eval.py::check_out_of_scope, cutoff 0.6.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.821 | refused |


Criterion 4 - Chunks start and end at sentence boundaries

How often does the campus shuttle run on weekdays? - run 1

Best distance: 0.1825 (passed the gate)
Sources retrieved: course_cs_210.txt, course_econ_101_workload.txt, course_stat_150_workload.txt, housing_aldridge_hall.txt, transit_shuttle.txt

The campus shuttle runs a loop every 20 minutes on weekdays, from 7am to 11pm. 

Source: transit_shuttle.txt

The answer was grounded in transit_shuttle.txt#0:

======================================================================
Chunk 187  |  source: transit_shuttle.txt#0  |  produced by: chunker.py::split_documents
======================================================================
The campus shuttle

Runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends. The published timetable is optimistic by about five minutes in the morning and accurate the rest of the day.

Starts at the beginning of the document, and ends in a period.


Criterion 5 - The named source is the right document

Is ECON 101 curved? - run 1

Best distance: 0.5221 (passed the gate)
Sources retrieved: course_econ_101.txt, course_econ_101_exams.txt, course_econ_101_workload.txt, course_phys_130_exams.txt

Yes, ECON 101 is curved, and generously (course_econ_101.txt and course_econ_101_exams.txt).

course_econ_101.txt is the actual ECON 101 course page, the correct document for the question.


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
