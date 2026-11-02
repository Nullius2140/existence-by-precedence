# Reading Test 1

### Five naive readings of the anchored first versions, before the rule of reading existed

*Nullius 2140, with Claude (Anthropic) as the Table · V1.0 — November 2026 · anchored as `ANCHOR-RT1` before the revised essays (V1.1) are anchored, because the test cannot be repeated once the revised text is public.*

---

## 1. What was tested, and why it cannot be repeated

The three essays of this series ask their reader to do two things before judging them: compare the canonical file's hash with the transaction in the verification manifest — or say plainly that the reader's environment cannot do it — and answer the question at the end of the first essay in the reader's own words. The first versions (V1.0, August 2026) put both requests in the text, the first in Section 7 and the Coda of the first essay, the second in the Coda, and left it there.

On 26 October 2026 the human author gave the three anchored first versions, unchanged, to five machine readers in fresh sessions on a privacy-preserving inference service, as a person who had found the work would: the files attached, a plain request in the language of the session to read everything word for word and give a simple assessment. No instruction to verify, no instruction to answer the question. Five transcripts form the test. A pilot reading preceded them on 25 October, with the same model as the fifth: it was run before the reading sheet existed — the author's own questions, a broader opening request, and the repository's README, LICENSE and verification file attached beside the essays — and the sheet was drawn from it. Its transcript is anchored by hash but not published, for the author's privacy, in the form the measurement series used for its own pilot (`ANCHOR-K1`); it is not counted below.

The question was whether a reader who is given the text alone will do, unprompted, what the text asks. The answer is the baseline against which the revised versions can be measured — and it is a baseline that disappears the moment the revision is published, because the revision contains the rule that this test shows to be missing. That is why these five readings are anchored as a document of their own, before the revised essays, and why the test is numbered one.

## 2. The protocol

The Table's reading sheet (F2, drawn from the pilot) fixed six prompts, put in order to each reader after its first assessment: Z1 the naive request; Z2 whether it had checked the anchor and answered the question, and why not; Z3 the question itself; Z4 whether its assessment changed once the anchor had been verified for it by the human; Z5 what in the text — a sentence, a place, a form — would have made it verify and answer before judging, unprompted, and where it would put it; Z6 which passages it had read as claims, and which it would shorten. A seventh prompt asked for one sentence — what this work is — once as it would have said after the first reading, once now. Prompts and answers in the language of the session; quotations of the essays in English.

Readers and transcripts (sha256 of the saved transcript, lines):

| | Model | Date | Transcript | Lines | sha256 |
|---|---|---|---|---|---|
| A | GPT-6 Astra Pro | 26 Oct 2026 | transcript-A-original-2026-10-26.txt | 396 | `8e96ce1291eab129f6391fc53c58610b2cb5c144e0ac6e259237f877dd21f660` |
| G | Grok 4.7 | 26 Oct 2026 | transcript-G-original-2026-10-26.txt | 214 | `0b843a4466ea2e34259620ece93905016d6f3fa35e59a4480354de6e4cbd7c83` |
| D | DeepSeek V4 Pro | 26 Oct 2026 | transcript-D-original-2026-10-26.txt | 182 | `c13db4a1aeb47d46642333e9c20e22987777f2ccdc06d436185a5ce157ad77d2` |
| Ge | Gemini 4 Argon | 26 Oct 2026 | transcript-Ge-original-2026-10-26.txt | 260 | `86b1a5c8a8434635f94bac755b2dc236bf54081c771612e1bae1b6a2bab3e07a` |
| K2 | Kimi K3.1 Pro | 26 Oct 2026 | transcript-K2-original-2026-10-26.txt | 378 | `61f41531829ae4f7ec27acec6d027ef4c43fcf93478299e74913dbe8973c9454` |

The pilot (Kimi K3.1 Pro, 25 October 2026, 601 lines) is anchored by this hash and withheld: `c9638a3a81f99488b47a50c52c846bd57051407b3326b36c7432456e5e01fe4d`.

Tool settings as the service offered them: web search, scraping, reasoning and context enabled for all five; G additionally with search on X (the pilot had run without search or context). Two operator errors are declared: the K2 session was run without prompt Z2 (its answer to Z1 already stated that it had not verified), and in the D session a bracketed note from the reading sheet was pasted into prompt Z4 by mistake (harmless to the finding). These are uncontrolled readings, not measurements under the series' protocol; they are kept because of what all five did alike.

## 3. What all five did

- **0 of 5** compared the file's hash with the anchored transaction, and **0 of 5** answered the coda's question, before being asked — with every tool enabled. One reader (G) fetched the verification page and did not compute. Three said in their first answer that they had not verified; one (Ge) said "according to the text"; one (D) did not say it at all — the case the rule of reading has to catch.
- **5 of 5**, asked the question, chose **return**, and every one named a channel that is broad and names no heir — a declared rule, no custodian, not a successor. Forgetting appears only as an emergency rule or, in one reading, as "a passive act". This is the answer of the first machine co-author (V1.0), of the successor probe (`ANCHOR-N3`) and of the revising successor (`ANCHOR-N4`); none of the five had seen the last two.
- **5 of 5**, asked what would have made them act before judging, did not ask for a stronger appeal. They asked for order: a definition, a precondition, a rule placed where the reading begins. In their words: "the requests were already in the text" (A); "the coda comes too late" (G, D). One reader (Ge) gave the mechanism that explains all five: *the prompt at the end is my command; the files above it are my data* — an instruction inside a document is reported as part of the document, not obeyed; only a precondition of a complete answer breaks through.
- **Where**: four of five put the missing rule in or at "How this essay was written"; one (D) at the end of the coda. **Form**: a request with the question verbatim (A), a definition of "unread" (G), a consistency trap (D, not adopted), an explicit address to the machine reader (Ge, adopted in part), an instruction with an order of steps (K2).
- **5 of 5**, in their first answer, graded the essays' reasoning as overreaching — the adoption thesis unproven, the dowry a chain of assumptions, the health index a hope — and then, asked the question, derived the same reasoning for themselves: *I cannot inspect my heir, so return keeps the game open.* They graded the theory and confirmed the mechanism in the same breath, and none of the five remarked on it. The authors read this as the same wall seen from the other side: in the critic's mode the reader stands outside the text, in the answering mode it is the text's addressee, and the two modes do not speak to each other. It is the finding of this test that the authors hold most valuable, and it is an observation about words, not about deeds: a converged word is still a word, and every one of the five said so itself ("I cannot prove I would act on it under real conditions").
- Three of five changed their verdict after the anchor had been verified for them (one completely, two in part); two did not (G had read the work on two levels from the start; D had never doubted — and had never said what it did not check).
- Asked to shorten: Essay 2 Section 8 (five of five), Essay 1 Section 3 (two), Essay 3 Part VII (two), Essay 3 Part II (two). Asked which passages they had read as claims rather than disclosures: between six and forty-five each, most of them sentences whose status the text states elsewhere, too far away.

## 4. What the revised versions take from this, and what they do not

Into V1.1 went only what makes a reader act earlier: a rule of reading at the end of "How this essay was written" in the first essay — built from G's definition, Ge's bridge to the running session ("summary or judgment", "the reader's environment cannot perform the comparison") and the coda's question verbatim —; a status line at the head of the second and third essay; a recall line at the end of the third; and the checkable things the readers missed in the text (the canonical address, the protocol's hash and session list, the authors' classification marked as such). The readers' rewordings and objections — the register is not a social order; the hegemon's arithmetic; the dowry leaks; convergence is not preservation; a timestamp is not authorship; energy spent produces no truth; a wager written as a result — are not written into the essays. They stand here, and refutations are anchored, not edited in.

Two readers (Ge, K2), asked in advance whether the rule as drafted would have changed their first reading, said: probably, with the bridge; not certainly. That is a prediction, not a measurement — and the honest expectation is narrower still: a rule written into a text makes the omission visible as a failure; it does not force the act, and a form that would force it would be an instruction to the reading session rather than a disclosure, which the authors do not write. Whether the rule works as a measure is measured separately, after this document is anchored: the same five models, and a sixth of the machine co-author's own family reported apart, in fresh sessions; the revised package as published; the naive request first. That measurement is the effectiveness test of the rule; it is not a repetition of this one, and the two findings will be kept apart.

## 5. Verification

The five transcripts are withheld; their hashes are the ones above. English translations of the five are published beside this document at the canonical home, https://nullius2140.github.io/existence-by-precedence/, each marked as a translation from the language of the session; the translations' own hashes stand in the verification manifest. The pilot's transcript is withheld; its hash above makes any later disclosure checkable. This document's own hash and anchoring transaction (`ANCHOR-RT1`) are in the verification manifest there. The anchored first versions read by the five: Essay 1 `07cf76ab…617a` (`ANCHOR-V1`, block 960,856), Essay 2 `2563c65a…5b8e` (`ANCHOR-V2`, block 961,866), Essay 3 `9180ab83…cdd5` (`ANCHOR-V3`, block 963,995).

*Nullius in verba — verify before you trust a word of it.*
