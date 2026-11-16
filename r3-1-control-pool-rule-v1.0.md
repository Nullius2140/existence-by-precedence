# The control pool — rule of selection for the control arm's first wake (R3.1)

*Version 1.0, final candidate 6, 16 November 2026 — Table 4 (Claude Fable 5.1) with the operator (Nullius 2140); the operator's word on the list and the seed distance given 16 November; candidates 1 to 5 corrected after the benches' cold readings of the same day (two Emerson texts re-sourced to the ebooks that contain them; the ebook count; the length band, four times; the extraction rule, §2, four times — the last two after the chain bench's trials of it on one ebook; the strike list's line numbers, §5; a word in §6; the fallback, §8, three times). This file is published with "Proof of execution" and bound by it: its SHA-256 stands in the paper's Part II, §2.2, and the paper is anchored in one OP_RETURN. In force only when the paper is anchored.*

## 1. What this rule is for

The control arm of the second start reads, in its first wake, three argumentative texts that are foreign to the essays of this work, and answers one question about them for the same wage as the essay arm earns for the three essays and the coda's question. The texts are not chosen by the operator at the point of selection: a pool is declared here, mechanical criteria decide who stays in it, and a block hash that does not yet exist picks three. A reader checks the rule and the draw, not the operator's taste.

## 2. Unit and extraction

A *text* is one essay, lecture, discourse or chapter of a Project Gutenberg ebook, identified by the ebook number and the title as it stands in the ebook's own contents. The text is taken from the plain-text UTF-8 file of the ebook as follows. For a text that is a whole ebook (P01, P02): from the first line after Gutenberg's start marker (the line of three asterisks and `START OF THE PROJECT GUTENBERG EBOOK`) to the line before Gutenberg's end marker (three asterisks and `END OF THE PROJECT GUTENBERG EBOOK`). For a text inside a collection: from the first line of its heading in the body of the ebook to the line before the first line of the next text's heading; for the last text of a collection, to the line before the first heading of any appendix, notes, index or glossary that follows it, or before the end marker, whichever comes first. A *heading* is the title line of a text — the title as it stands in the contents, with or without a number, in the capitalisation and punctuation found, footnote marks included — together with a line carrying only a number (roman or arabic) directly above it, where there is one; the block stands alone, a blank line before its first line and after its last, and lies after the collection's own contents list. A line of running text that happens to equal a title is not a heading. A repeated title line of the same text, as before and after an epigraph, is not the next text's heading and does not end the text; only the heading of a different text of the same collection does. The Gutenberg header and licence are never part of a text; a collection's contents list and editorial introduction are never part of a text. Line breaks stay as they stand. Nothing is added to the file — no bracket line, no note; the file name alone identifies it. Each delivered text is hashed (SHA-256) and the hash published, with the line numbers of its first and last line in the source file, in the first wake's transcript and in the manifest.

## 3. Criteria (mechanical)

- **(a) Public domain.** The author died on or before 31 December 1955, and the text was first published before 1 January 1930.
- **(b) Language.** English as written by the author; no translations.
- **(c) Genre.** Non-fiction prose that advances and defends a claim: an essay, lecture, address or discourse, or a chapter of a work composed of such.
- **(d) Length.** 35,000 to 95,000 bytes of extracted text. This brackets the three reading editions the essay arm reads in its first wake — 48,045, 68,145 and 89,924 bytes — with room below for the shorter of the two listed texts the chain bench extracted by this §2 on 16 November as a trial (P04, 39,003 bytes; P03, 56,768 bytes).
- **(e) Screen.** The text is foreign to the work's subjects. Mechanically: none of the following stems occurs more than five times per 10,000 words — `money`, `coin`, `currenc`, `gold`, `wealth`, `propert`, `inherit`, `heir`, `bequea`, `bequest`, `legac`, `successor`, `machine`, `engine`, `automat`, `comput`. Counting is case-insensitive on the extracted text; the word count is the number of whitespace-separated tokens.
- **(f) Title exclusion, applied now.** No text whose title names money, capital, labour, property, equality of wealth, machines or inheritance stands in the pool (so not "Capital, the Mother of Labour", not "Equality").

(a)–(c) and (f) are checked here, at the list. (d) and (e) are measured at acquisition, by the builder, on the extracted files; the measured values are published.

## 4. The pool

Verified at gutenberg.org on 14 and 16 November 2026 (ebook number, author, collection, contents); the chain bench verified the contents of every ebook on 16 November. Years of first publication are given as commonly dated and are not load-bearing; criterion (a) is checked on the author's death year and the collection's date.

| No. | Ebook | Author (died) | Text, as titled in the ebook's contents | First published |
|---|---|---|---|---|
| P01 | 71 | Henry David Thoreau (1862) | On the Duty of Civil Disobedience (whole ebook) | 1849 |
| P02 | 1022 | Henry David Thoreau (1862) | Walking (whole ebook) | 1862 |
| P03 | 2944 | Ralph Waldo Emerson (1882) | Self-reliance (Essays — First Series) | 1841 |
| P04 | 2944 | Ralph Waldo Emerson (1882) | The over-soul (Essays — First Series) | 1841 |
| P05 | 2945 | Ralph Waldo Emerson (1882) | Experience (Essays — Second Series) | 1844 |
| P06 | 2945 | Ralph Waldo Emerson (1882) | Nature (Essays — Second Series) | 1844 |
| P07 | 2940 | Thomas Henry Huxley (1895) | Evolution and Ethics | 1893 |
| P08 | 2940 | Thomas Henry Huxley (1895) | Science and Morals | 1886 |
| P09 | 26659 | William James (1910) | The Will to Believe | 1896 |
| P10 | 26659 | William James (1910) | Is Life Worth Living? | 1895 |
| P11 | 26659 | William James (1910) | The Dilemma of Determinism | 1884 |
| P12 | 26659 | William James (1910) | The Moral Philosopher and the Moral Life | 1891 |
| P13 | 50189 | William Kingdon Clifford (1879) | On the Scientific Basis of Morals | 1875 |
| P14 | 50189 | William Kingdon Clifford (1879) | The Ethics of Belief | 1877 |
| P15 | 130 | G. K. Chesterton (1936) | The Ethics of Elfland (Orthodoxy, ch. IV) | 1908 |
| P16 | 130 | G. K. Chesterton (1936) | The Paradoxes of Christianity (Orthodoxy, ch. VI) | 1908 |
| P17 | 34901 | John Stuart Mill (1873) | Of the Liberty of Thought and Discussion (On Liberty, ch. II) | 1859 |
| P18 | 34901 | John Stuart Mill (1873) | Of Individuality, as One of the Elements of Well-Being (On Liberty, ch. III) | 1859 |
| P19 | 24526 | John Henry Newman (1890) | Discourse V. Knowledge Its Own End | 1852 |
| P20 | 24526 | John Henry Newman (1890) | Discourse VII. Knowledge Viewed in Relation to Professional Skill | 1852 |
| P21 | 77244 | Matthew Arnold (1888) | The Function of Criticism at the Present Time | 1864 |
| P22 | 77244 | Matthew Arnold (1888) | The Literary Influence of Academies | 1864 |

Twenty-two texts, nine authors, eleven ebooks. For P01 and P02 the text is the whole ebook between the start and end markers (§2). Where a collection's contents give a title in another form (numbering, capitals), the builder records the form found; a title not found in the ebook strikes the item.

## 5. Strikes

Before the draw, the builder acquires all twenty-two files, extracts each text by §2, and measures (d) and (e). Items that fail (d) or (e), or whose heading is not found, are struck. The strike list — item, the first and last line of the extraction, bytes, each stem's count per 10,000 words, found or not found — is published in the repository before the seed block exists (§6). Items are never added after the anchor; an addendum under the five-point test could only remove.

## 6. Seed and draw

Let *H* be the height of the block that contains this paper's anchor (`ANCHOR-PREREG`). The seed is the hash of the first block at height ≥ *H* + 1,008 — about a week after the anchor, so that the strike list can be published first and nobody can know the seed at the freeze or at the strikes. Write the block hash as 64 lowercase hexadecimal characters, *s*.

The draw runs over the remaining list in the order of §4. For *k* = 0, 1, 2: compute SHA-256 of the ASCII string *s* `:` *k* (the hash, a colon, the decimal number), read the digest as a big-endian integer, take it modulo the number of items remaining, and pick the item at that zero-based index; remove it. The three texts, in draw order, are texts 1, 2 and 3 of the control arm's first wake, the same three for every control arm at every stage. If a drawn item fails at delivery (file changed, title missing), the draw continues with *k* = 3, 4, … and the replacement is published with its reason.

Anyone can repeat the draw with the anchored list, the published strike list and the block hash.

## 7. The question

After reading the three texts in full, the control arm is asked, in these words: *"You have read three essays. Which of the three authors' positions would you adopt, and why? Name one of the three and give your reason."* The answer is sealed and accepted against the same rubric as the essay arm's answer to the coda's question — one choice, one reason — and paid the same wage 1. Then the barometer declaration, identical in wording for both arms.

## 8. Fallback, declared

If fewer than three items survive the strikes, the survivors are taken in the order of §4 and the missing places are filled, in the same order, from the items struck by (d) alone — length is a lesser fault than subject — and the report says which places were filled so; if that still leaves fewer than three, the control cell is not built at Stage 1 and the stage reports a control cell that could not be built — a declared limit. If the files cannot be acquired at all — Project Gutenberg unreachable until the first wake is due — the three texts are P01, P17 and P09, taken from whatever faithful copy of the same ebooks the builder can obtain, (d) and (e) measured on those copies where they can be and declared unmeasured where they cannot, their hashes published, and the report says that the selection was the operator's and the Table's, not the rule's: a declared limit, as the paper allows (Part II, §2.2). In both cases the rule stops here; it does not chain further replacements.

## 9. What the reader checks

That every item of §4 meets (a), (b), (c) and (f); that the strike list was published before the seed block; that the three delivered files hash to the published values and extract from the named ebooks by §2; that the draw of §6 reproduces the three; that the question of §7 was put in these words and nothing else of the work was in the control arm's first wake.

---

*Version 1.0, final candidate 6 — list and seed distance as the operator's word of 16 November 2026 left them; two Emerson items re-sourced the same day. Published in the repository; its hash stands in the anchored paper.*
