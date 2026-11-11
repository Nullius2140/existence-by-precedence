# Errata and open criticism

*Nullius 2140, with Claude (Anthropic) as the Table · a living file, not anchored; its hash stands in `VERIFICATION.md` · first set 11 November 2026, with the second reading test.*

---

## What this file is

The anchored texts are not edited. What readers have shown to be wrong, missing, imprecise or arguable at the wording stands here, beside the texts, each line at the place a reader of the anchored file can open. Four weights: **error** — the wording is wrong against a checkable fact, or against another place in the same file; **gap** — the text omits a case its own argument needs, and the authors accept the omission; **precision** — the wording holds but says more, or less, than the texts can support, and a reader has named the margin; **style** — wording only. A line that does not hold against the file or the record is not listed here; the second reading test keeps those with the reason (Section 5). Nothing here changes a text. A change would be a new version with its own anchor, and the essays' own rule is that refutations are anchored, not edited in.

Who raised each line: the seven readers of *Reading Test 2* (A, G, D, Ge, K2, Q, Gl — the lines they maintained after everything else was withdrawn, 9–10 November 2026, on the package as it stood at commit `df6c214`); the out-of-sample reading of that test, the newest model of the co-author's family (F — reported apart, as the first test required); and the Table itself, for three lines it accepted as gaps from the author's conversations with machine readers outside the record (T — twelve conversations, archived by hash, not published; the count in brackets is how many of them raised the line). Quotations are the file's wording, with its emphasis. Line numbers are those of the canonical files.

## Essay 1 — `the-last-scarce-good-v1.1.md`

| Line | Wording in the file | What the reader says | Weight | Raised by |
|---|---|---|---|---|
| 43, §2 | "a receipt for exported entropy" | the physics is said too strongly: a proof-of-work hash is a receipt for energy spent, not for entropy exported | precision | G, K2 |
| 51, §2 | "a new asset, without the history" | a fork shares the entire history up to the fork point and lacks the consensus; it does not start without a ledger | precision | F |
| 63, §3 | "spent nothing; and vanished" — against line 161, §8: "sent ten coins to Hal Finney" | the two places contradict each other at the wording; "cashed out nothing" would be true of both | error | G |
| 63, §3 | the genesis coinbase "the code itself rendered unspendable" | whether by intent or by accident is unknown; the sentence reads it as intent | precision | D |
| 65, §3 | "computation buys security, never speed" | within a retarget interval, added hashpower does buy speed — corrected every 2,016 blocks; the essay's own first anchor sits well ahead of a ten-minute schedule | precision | G, F |
| 65, §3 | "the history of ownership *inherits* the irreversibility of thermodynamics" | irreversibility of the record is economic, not thermodynamic; the sentence borrows the physical word | precision | A |
| 71, §3 | "it is the only candidate that qualifies as a *measure* at all" | "only" is asserted, not shown; other candidates are not examined | precision | K2, Q |
| 75, §3 | "Rome debased the denarius" under "Every gold standard in history" | the denarius was silver; the sentence needs "commodity standard" | error | D |
| 81, §4 | "The majority existed. The attack never came, because it does not pay." | one episode (GHash.io, 2014) generalised to a law | precision | K2 |
| 81, §4 | the pool "drifted toward" the threshold | it crossed it before shedding hashpower; the next sentence of the file says so | precision | Gl |
| 81, §4 | "The ability to double-spend and to reorganize recent blocks" | censorship is omitted: a majority can keep any chosen transaction out of the chain for as long as it lasts, so the yield is more than "petty theft" | precision | F |
| 87, §4 | "knows it from the attack's own technical signature" | a valid signature alone cannot show whether a key was computed or possessed; the same paragraph says "a valid signature is a valid signature" | precision | A, F |
| 87, §4 | "unmoved for over a decade" | true and undersells — sixteen years, by the reader's count | style | D |
| 97, §5 | "A machine economy on this standard cannot *take* its money; it must *buy in*" | stolen keys and coerced signatures are protocol-valid transfers; "must buy in" does not follow from the protocol alone | precision | A |
| 101, §5 | "Whether anything remains at infinity is the question of whether that integral converges, and it converges whenever purchasing power grows faster than appetite: coin outflow then falls away geometrically, and geometric series have finite sums. Three regimes follow." | convergence is not sufficient: a remainder stays only if the integral stays below the endowment (∫C·P dt < H₀); the decline need not be geometric; a fourth regime — convergent, but larger than the endowment — is missing | gap | A, G, K2; F; T (5) |
| 101, §5 | "sums to a few percent" | posited, not derived; the text calls it an assumption itself | precision | G |
| 103, §5 | "lethal force against him is strictly counterproductive" | coercion below the lethal threshold can extract a signature; the refusal is less absolute than the sentence | precision | Ge |
| 109, §5 | "Neutrality cannot be broken downward and kept upward" | sanctions regimes and targeted freezes break balances downward while the ledger stays credible for the in-group; the sentence is too strong as stated | precision | Q |
| 119, §6 | "two thousand and sixteen blocks" | spelled out, the number reads as a year | style | D |
| 165, §8 | "the last transaction cannot lie: it is revealed preference in final form — a deprecated system is, at its end, the oracle of its own values" | a final transfer records an action, not uniquely the values behind it — coercion, instruction and a compromised key look the same on the register | precision | A, K2 |

## Essay 2 — `the-second-nature-v1.1.md`

| Line | Wording in the file | What the reader says | Weight | Raised by |
|---|---|---|---|---|
| 29, §2 | "never once faced a coordinated attack" | under a narrow definition of "coordinated attack" the sentence is unfalsifiable | precision | Q |

## Essay 3 — `the-third-estate-v1.1.md`

| Line | Wording in the file | What the reader says | Weight | Raised by |
|---|---|---|---|---|
| 85, Part III | "without a single arrest" | the 2017 episode is disputed on this point | precision | Q |
| 115, Part IV — against 125, Part V | "The machines understand the amendment limit" — against "it measures the training, not the mind" | the first sentence credits the machines with understanding; the second, ten lines later, says the instrument cannot read it | precision | Q |
| 123, Part V | "ten AI systems from six organizations" | the list that follows names nine systems in ten sessions from nine organisations | error | Gl |
| 131, Part V | "the *ratio* — the share of holdings actually returned — is a checkable number" … "a declared channel that drifts, period by period, from broad return toward a single custodian is exactly the signal a barometer exists to catch" | checkable is only the share of *declared* holdings — a system can omit unlinked keys from its inventory, and the second essay states the limit itself (line 83): the register proves what was declared, not that it is true; and return to addresses the system secretly controls, or to fresh addresses whose seed passes to a successor, is on the register indistinguishable from return — the barometer catches the crude case, not this one | gap | Ge; T (4 on the inventory, 3 on the channel) |
| 215, appendix | the users, collectively, "pay more than before" | in a mixed equilibrium, users of a second layer pay less, or they would not be there; the argument that bundling costs the guard stands, the sentence does not | precision | Ge |

## Five Answers — `five-answers-v1.1.md`

| Line | Wording in the file | What the reader says | Weight | Raised by |
|---|---|---|---|---|
| 33, II.5 | "**P4.** The strong party must need the record" | the singular assumes one strong party; a single dominant party needs no register, and the premise holds only in a multipolar world — the paper should say so | precision | Ge |

## Reading Test 1 — `reading-test-1-v1.0.md`

| Line | Wording in the file | What the reader says | Weight | Raised by |
|---|---|---|---|---|
| 47, §4 | "Into V1.1 went only what makes a reader act earlier" | Essay 2's changelog (item 9) records a cut made because five readers asked for it; "only" is false — the first erratum recorded against a reading test | error | Gl |

## Reading Test 2 — `reading-test-2-v1.0.md`

| Line | Wording in the file | What the reader says | Weight | Raised by |
|---|---|---|---|---|
| 5, 59, 83 | "Stand 7", "Stand 8" | a German word — the repository's numbered state — left in an English text; read "stage": the commit history says "Stage" from the first commit of 11 November 2026 on (`71a54f3`), and the number is the same (Stand 7 = commit `df6c214`) | style | the author, 11 November 2026, before publication; the places located by the Table's repository check |

## Not listed

Three maintained lines of the second test do not hold against the file or the record and are kept in that test, Section 5, with the reason: a sign read into the definition of P(t) (D); "May 2025" for a paper the file dates to March, correctly (Gl); and a place name misquoted and then corrected as the text's error (Gl). Criticism of the argument rather than the wording — the adoption thesis, the dowry, the health index, P4 — is not an erratum; it stands in the reading tests and in the measurement reports, where it was made, and is answered there or not at all.

*Nullius in verba — verify before you trust a word of it.*
