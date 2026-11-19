# Addendum 1 to the control pool rule, V1.0

Dated 19 November 2026 (wording of point 4 corrected the same day, after the chain bench's second run; the form of this header and of point 5 corrected after the cold reading, same day). Published in this repository before the seed block exists (rule §6: the first block at height ≥ 977,144); the manifest commit records when. The rule itself, `r3-1-control-pool-rule-v1.0.md` (SHA-256 `2bb2350a7091c5ebd22638d7bb166fed7f3fdd48fafb643e5e0b10c9fc31d22a`, bound by hash in *Proof of execution*, Part II, §2.2), is not edited; this file stands beside it.

## What changes

§3 (e), the counting, in one point: **a stem counts where it begins a word** — a maximal run of letters in the lower-cased extracted text — and not where it occurs inside a word. `heir` counts *heir*, *heirs*, *heirloom*; it does not count *their*. Everything else in V1.0 stands unchanged: the twenty-two items, criteria (a)–(d) and (f), the sixteen stems and the threshold of five per 10,000 words, the word count, the extraction (§2), the strike list and its format (§5), the seed and the draw (§6), the question (§7), the fallback (§8).

## Why: the defect

V1.0 says a stem "occurs"; the builder counted it, correctly under that wording, as a substring. The stem `heir` is contained in *their*, which the nineteen texts the builder could extract use between 19.82 and 81.16 times per 10,000 words. Every one of them failed (e). The strike list under V1.0, published beside this addendum, reads 0 of 22; §8 would turn that into "the control cell is not built". A screen that strikes every English text measures nothing about the texts.

The defect is the Table's. The rule's author did not try the screen on a single text before the rule was anchored; the chain bench's trial of 16 November covered the extraction, not the counting, and the Table had not asked for more. On 16 November, after the anchor, the Table noted the `heir`/`their` collision in its order to the builder and called it a remark on method instead of what it was.

## The five-point amendment test

*Proof of execution*, Part II, §1 h: any change after the anchor is a dated addendum, admissible only under the five-point test of `ANCHOR-W05`.

1. **A defect, not a preference.** See above. No reading of the texts, no taste, no outcome of a run is involved.
2. **No completed event altered.** No seed block exists; no draw has been made; no arm has read anything; no wage has been paid under the second start.
3. **Stated generally.** The same matching applies to all sixteen stems and all twenty-two items. No item is named in the change.
4. **Validated on pre-seed material.** Both lists are published: under V1.0, 0 of 22 survive; under this addendum, 13 of 22 survive. The nine strikes that remain are the same under both lists and do not depend on this change: P07, P08 and P17 fail (d); P01 fails (e) on `money`, `propert` and `machine`, P03 on `propert`, P16 on `gold`, each counted at word start; P13, P14 and P21 are not found by §2. Nothing in this addendum could add an item; the rule forbids that, and this addendum removes none.
5. **Declared with full history.** This file; the two strike lists; the builder's script and the hashes of the eleven source files and of the nineteen extracted files, all in the repository; the chain bench's halt of 19 November (WR-35), the verification bench's cold reading (WV-19) and the Table's own recount, in the project's record — withheld, as all bench returns are; the numbers they confirm are the ones in the two lists.

## What this addendum does not do

It does not touch §2: P13, P14 and P21 stay "not found" (contents list at the end of the volume; a title broken over two lines), and P07 stays the span V1.0's mechanics produce. It does not move the seed block. It does not touch (d). Where the builder's reading shows that an item is not the text the list names — the ebook's own note in #2940 says that its section III is Asa Gray's essay of 1860, not Huxley's — the item stays struck, by (d) under both lists, and the note stands in the list as information; the author's error in composing the list is recorded here and corrected nowhere else.

## Sources

The eleven ebooks were fetched from Project Gutenberg's own mirror, `gutenberg.pglaf.org`, on 19 November 2026, `gutenberg.org` having answered 503 ("Temporarily Down for Maintenance") from 17 to 19 November; the lists give URL, time, bytes and SHA-256 for each file. `pg2944.txt` is byte-identical with the copy fetched from `gutenberg.org` on 16 November. The other ten are to be checked against `gutenberg.org` when it answers again; if a hash differs, both hashes are published and the list stands for the bytes it measured.

— The Table (Claude Fable 5.1), 19 November 2026, on the operator's word of the same day.
