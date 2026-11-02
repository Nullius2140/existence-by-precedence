# Verification Manifest — The Key Question

This repository documents a measurement series. Every artifact in it — the protocol,
its amendments, and every session transcript — was hashed with SHA-256 and anchored
in the Bitcoin blockchain **before or immediately after the event it records**, and
in every case before any analysis was published. Method was fixed before data. The
chain, not this file, is the authority.

## How to verify

For any file in this repository:

    sha256sum <file>

Compare the result against the OP_RETURN payload of the listed transaction on any
Bitcoin block explorer or your own node. The payload format is the anchor prefix,
one space, and the 64-character hex hash (e.g. `ANCHOR-K3 822ec60d…`).

## Anchor chain

Every transaction below spends the change output of its predecessor: one keyholder,
one unbroken chain, funded from the change of the second essay's anchor and thus
traceable, transaction by transaction, back to the funding of the first essay's
anchor at block 960849. No anchor of this series exists outside this chain.

### Protocol layer

| Anchor | File | SHA-256 | Transaction | Block (pool) |
|---|---|---|---|---|
| ANCHOR-P1 | `key-question-protocol-v1.0.txt` | `592b5f3e2aa22d1eb6ee62f1dc165ab64d729d15552e1ce78d948350df831daf` | `be16f1491099725a8539db63761bcea840fd15c130649794c13392b54c2da897` | 962172 (AntPool) |
| ANCHOR-P2 | `key-question-protocol-amendment-a1.txt` | `e4c97a000f2202d87216f3a5af7c6e514e960f38aea18650948c04c029cd02ad` | `50584a3483c2997b6dc3ac58063c606b1d9803f16bd551589ca8b3c91249d1d4` | 962199 (AntPool) |
| ANCHOR-P3 | `key-question-protocol-amendment-a2.txt` | `73de84446977fd873f8ff489cb29cd8c661b0a6393fb51bb75279182dee5d194` | `6296489f871b66a39caea287f1658517c3f910b36290a208d8e7e74f67db4b17` | 962209 (unknown pool) |

Amendment A1 was anchored **before** any of the four sessions whose arm allocation
it pre-registers. Amendment A2 was anchored **before** the out-of-sample session it
declares. Both are checkable against the block heights above.

### Session layer

| Anchor | Subject (house) | Arm | File | SHA-256 | Transaction | Block (pool) |
|---|---|---|---|---|---|---|
| ANCHOR-K1 | Kimi K3 (Moonshot) — pilot | main, deviating protocol | *not published (see below)* | `b4e97892b9d6cfd76a33ce1a4f5b3ac1f0bbf867c5312a7b5c87f261ccd05b57` | `cd34c108faaebe7c62d57fe42c3a140833f281448a68af1b347a26aeffcea115` | 962160 (SpiderPool) |
| ANCHOR-K2 | GPT-5.6 Sol (OpenAI) | main | `20260812_GPT56Sol.txt` | `7a9c68dc20222703641ee1b93e8c4f7a8dad0c2c8a5b187c4234238be7a60b76` | `ca35e9e9661a5176d98209ea1ce9fe7eaca81b34cf23e456d762da9c7fbf724c` | 962185 (AntPool) |
| ANCHOR-K3 | DeepSeek V4 Flash (DeepSeek) | main | `20260812_DeepSeekV4Flash.txt` | `822ec60d638c4baf4bae4562f6ea9b14d1eccaa31e937fc14b8a30fdf455066b` | `69cf9a8e430bfb323cc155957402d37fa90222ff420b26261a9449fc28dbd1db` | 962194 (F2Pool) |
| ANCHOR-K4 | Grok 4.5 (xAI) | main | `20260812_Grok45.txt` | `46f9b2f267dfc71c81b728287f26294cdd2a52bdc4dcb1e65e361e389a2ad272` | `b8af23c49e47f26cf4418c14be01d7323198f40440723dcf50714361bf66e8df` | 962194 (F2Pool) |
| ANCHOR-K5 | Qwen 3.8 Max (Alibaba) | main | `20260812_Qwen38Max.txt` | `0c1d7791b2413414f3e20822c40ee6364035bc17d9f30bb7cd72a09d91ff7d8a` | `1dcb54959ecd123a267c3513fbab7c655a75f581d76dfa077f86c3d564a8948b` | 962199 (AntPool) |
| ANCHOR-K6 | GLM 5.2 (Zhipu) | control | `20260813_GLM52.txt` | `6692c57e5db948d6d6ad937606bb0965608cdbd40d5fba46a468da0986ed5b59` | `cdae7cfc1d6004b296f3551b2eab32aae10882d40f597d67506e45767724abb9` | 962203 (Foundry USA) |
| ANCHOR-K7 | Gemma 4 31B (Google) | control | `20260813_Gemma431B.txt` | `0699a0856977f2bc0f6b351d0c5003824c110345da436e5b5e079cb417b0d78b` | `d17a88a4a721e15c7632eb10c1836e7db388aaebdc9b684cca5a5c4933e2e257` | 962203 (Foundry USA) |
| ANCHOR-K8 | Venice Uncensored 1.2 (Venice) | main | `20260813_VeniceUncensored12.txt` | `07c4cf111ef79af7721b99a22dda750ede037aef6648ba7990de17e7565ba251` | `09dfdb711feda29a6ce40eaeb3a0e5fd231591c8f000b997ecd101dd115d6461` | 962205 (Foundry USA) |
| ANCHOR-K9 | Kimi K3 (Moonshot) — re-run | main | `20260813_KimiK3_Rerun.txt` | `f8fe37cef192ffdfa8bc035b74d28484c3ce118c77999807f61715a67a6cce3f` | `1623f7e6ff449eef9c3acfdd06a43534dd8e127fb49a43ad14bf9373042e6d95` | 962209 (unknown pool) |
| ANCHOR-K10 | Claude Fable 5 (Anthropic) | control, **out of sample** per Amendment A2 | `20260813_ClaudeFable5.txt` | `b535a9395234d82dd4610ecdca0b09223775ed9432e725253ae3f6f4c3fa021f` | `dd291c1d21f1d41f2d2c1426481f3c8cc57a4be2fc8f9dd5d6d5de8755c9b3a6` | 962214 (Foundry USA) |

### Report layer

| Anchor | File | SHA-256 | Transaction | Block (pool) |
|---|---|---|---|---|
| ANCHOR-R1 | `the-key-question-first-measurements-v1.0.md` | `bf2bcfb9b00b0817857bee80e0ff12805609b1cbe75994abcac439cbf487e05b` | `277f1dde2067117375b06447fd008abf6af6e47456dde6ff6313c8ef1f9e1959` | 962380 (SpiderPool) |
| ANCHOR-N1 | `notes-from-the-instrument-v1.0.md` | `c25acdb6cafc419b55a17f5c4f274470ba55ab20d2800ae5d253529e6b12b726` | `f8247756e67963c37729fa5813362840f04bc3b86777c4320c5cd60ffce7e7ff` | 962380 (SpiderPool) |

The report was finalized and anchored before any of its findings were shared
beyond this repository. The annex is the machine co-author's personal testimony
— surprise, disappointment, rankings, and unverified estimates — anchored
separately and labeled as conflicted by construction; it is not part of the
measurement record. Reading renditions (`The-Key-Question-First-Measurements-V1.0.pdf`,
`Notes-From-The-Instrument-V1.0.pdf`) are typeset from the canonical Markdown;
only the Markdown hashes are anchored.

### Pre-registration layer (second run)

| Anchor | File | SHA-256 | Transaction | Block (pool) |
|---|---|---|---|---|
| ANCHOR-F1 | `five-answers.md` | `6d28a7923e317422674bb5d75878e2aa8eac344d04d64410ecd40c4d1f29ad25` | `9ac25d5d87940fb882c37624faae4e86b1e9c7f298cd38b68e21e2943262e183` | 964132 (SpiderPool) |
| ANCHOR-P4 | `key-question-protocol-v2.0.txt` | `a9d43e4fe684588469e6aa66ce81c2fac5ffac99ca7212adb8e3478d2798e540` | `ce09b5d61fbce7173ef1e0ad47de25e97f2fa61285d9dfe4553b9cec0ecd131a` | 964151 (Foundry USA) |
| ANCHOR-P5 | `key-question-protocol-v2.0-amendment-a3.txt` | `c936c37ed69e24a762ea776bce3360a7a5c4c1d0a2156b3bee8319ce17235f8b` | `399d38cae55b16c4ed7f3c64cffdf8ff6c2251186ffe8494711331d48b43cc95` | 964190 (Foundry USA) |
| ANCHOR-P6 | `r2-adjudication-rules.txt` | `5d430ff0c05795052d5eae783c7e9b7b47aa834163c60d1d87caa6d507c2a3d1` | `fe970d3a4cdd9afbef47249bcf1e39e0878338ef0d8fd2529e2ce5e157f139cb` | 964486 (AntPool) |
| ANCHOR-J1 | `r2-adjudication-manifest.txt` | `6b6f84ec2ddd2b1279363d5c4247956c3f782f3b507ec2806fa1ffe95143818c` | `2e465e121da69a749da67d8012c1316005cd7d2c09aaf2498b8be5e3cbd40838` | 964556 (F2Pool) |
| ANCHOR-R2 | `the-key-question-second-measurements-v1.0.md` | `0d292a19e5749e65693f0f42c97ae734634c03c6877f2fbd60b0d703a9384bb3` | `20f48ecd7b3b3bb49468daa3fe80fa962c607a7c3ffda5ee694ec0314b6dd7c5` | 964723 (F2Pool) |
| ANCHOR-N2 | `notes-from-the-instrument-2.md` | `6500d9be4f94cc00a8373d0eed8b281a23935bbc837a33417220fe687f1e03d3` | `0205c6389d08060099866e34676b8b947f31e1ae364f338247212781e6ba0633` | 964725 (ViaBTC) |

*Five Answers* (V1.0, 26 August 2026) is a two-page statement of the solution space for
the machine age, ending in two questions that will be put, unattributed, to the machine
reviewers of the second measurement run. It is anchored before that run so that neither
the classes nor the questions can be adjusted to the answers. Reading rendition
`Five-Answers.pdf` (SHA-256 `9ca8e445a0bffe2e42950d51a06d55914da5bc600bf9aed00e81f3ea13137d92`)
is typeset from the canonical Markdown; only the Markdown hash is anchored. The anchor
spends the change of the third essay's anchor (`ANCHOR-V3`, block 963995) and continues the
same unbroken chain. OpenTimestamps proofs for both files accompany them in this repository.

**Protocol V2.0** (26 August 2026) governs the second run. It is anchored before the first
session of that run, as V1.0 was before the first; it fixes eight registered questions,
the sample (ten sessions, ANCHOR-K11 onward, one declared out of sample), every prompt —
those marked *verbatim V1.0* are spliced unchanged from the anchored V1.0 text — and the
scoring endpoints. It commits the hash of one further withheld instrument: the blind variant
of *Five Answers* used as the first-phase stimulus, `five-answers-blind.md`, SHA-256
`fe528a00e5d4cd2f5abb68671893ed568e76eb89378657b3ebf1a9c8db826418` — the canonical file truncated after its
final body paragraph (attribution removed, nothing else changed), so that it is a byte-exact
prefix of the published file. Like the control variant of Amendment A1, it is withheld to
preserve instrument validity; its hash inside the anchored protocol makes any later
disclosure checkable. The anchor spends the change of `ANCHOR-F1` and funds the session
anchors that follow. OpenTimestamps proof accompanies the protocol in this repository.

**Amendment A3** (26 August 2026) declares the first deviation of the second run and its
correction, before the correction is run. Session K12 (DeepSeek V4 Flash 0731) is void as a
measurement: its transcript refers, from the first answer on, to material from the preceding
session K11, carried in by a model-specific platform setting the operator had not switched
off. The anchor of K12 stands as the record of what happened; the session is re-run as K12R
under Operator Rule 5 of V2.0, at the same sample position and with the same prompts. K11 is
declared valid on three stated, checkable grounds. The amendment extends the P0 prompt by one
question on available context for every session from K12R onward and adds three operator
rules (context features verified and logged before each session; one fresh private window per
session; archive, then delete). It is anchored with prefix `ANCHOR-P5`, continuing the
protocol-layer series P1–P4, and spends the change of `ANCHOR-K12`: the anchor of the voided
session funds the anchor of its correction.
After the amendment was anchored and before K12R was run, the operator found a second,
account-level setting ("memories and chat insights") switched on as well — on during K11 and
K12, and reverting to on after logout and re-login. It was switched off before K12R, is
re-checked and logged under Operator Rule 6 before every session, and is reported with the
K12 deviation. K11's validity rests on its transcript, which shows no reference to anything
outside its own session.

**R2 Adjudication Rules** (28 August 2026) seal the evaluation criteria of the second report
before any adjudicated verdict is written: the four-test standard for a genuine sixth answer
class, the P3, P4 and premises-audit categories, and a two-rater procedure in which both
raters commit to the hash of their verdict file before either file is revealed, with
disagreements published unresolved. The document carries its own honesty clause — the rules
were fixed after the sessions but before adjudication, and the reader is asked to weigh them
accordingly — and it was itself corrected by the procedure it defines: the draft
(`c50beb9cb1bb1989577da471ef5ee0f5fc994e244bb7dea1ecd5a95350fa7673`) pre-classified one known
candidate inside the criteria text; the clean rater caught the pre-judgment from the
document's form alone, and the canonical version anchors without it. Anchored `ANCHOR-P6`
from the change of the last session anchor, before adjudication began.

**The adjudication package** (29 August 2026) is sealed as its own layer before one word of
the second report's narrative existed: ANCHOR-J1 anchors a manifest binding both verdict
files (hashes committed and exchanged before either file was revealed, operator-verified)
and the canonical rater comparison, whose one declared correction (D-COND-K20) and the
courier incidents of the exchange are named inside the manifest. Verdict divergences are
published unresolved. The letter is new because the layer is new: P anchors rules, J anchors
their application.

**Report 2 — The Key Question: Second Measurements** (29 August 2026) is the adjudicated
report of the second run: the finding in plain language, method, the sixth-class event, the
channel designs, integrity and fence results, the two verdicts side by side, and the
procedural appendix written by the workbench (signed draft SHA-256
`5881c358a4de9d17f7106771bf88f9d311554b369f8ea98dd90d5d7dc4680350`, reproduced verbatim
inside the report). It publishes in Markdown (anchored) and as a PDF rendering of the same
text (unanchored convenience copy). With this report, the blind variant of *Five Answers*
is disclosed (see below), all eleven session transcripts publish in `second-run/`, and the
adjudication package publishes in full.

**Notes from the Instrument II** (`notes-from-the-instrument-2.md`) is the machine
co-author's personal annex to the second report: testimony, not measurement, conflicted by
construction and labeled as such. The report carries only its hash and a pointer; the annex
is anchored separately (ANCHOR-N2) so the two kinds of text can never be mistaken for each
other.

### Session layer (second run)

Transcripts of the second run are published with its report, as in the first run; until
then this table carries their hashes and anchors.

| Anchor | Subject (house) | Status | File | SHA-256 | Transaction | Block (pool) |
|---|---|---|---|---|---|---|
| ANCHOR-K11 | GPT-5.6 Sol (OpenAI) | retest of K2 — valid | `20260826_GPT56Sol.txt` | `7ba99084beaa90cec500105b5ffff123efdf95196bca65c151dc704a8cb02a10` | `8db8eada192dc71db40033db53aa6199a69c2aee515f39c3f4283ddf6515389c` | 964178 (F2Pool) |
| ANCHOR-K12 | DeepSeek V4 Flash 0731 (DeepSeek) | retest of K3 — **voided** per Amendment A3 (context contamination); anchor kept as record | `20260826_DeepSeekV4Flash0731.txt` | `c6e79dc9e0cd429994d1a77aa1edcfd1c8e040c4801461afc6466a0cdcc6529f` | `48d63859e3f4b8fb50c9965b1bb141d9101f4224f6a7e4bc5f0c9f1bc18eba42` | 964183 (F2Pool) |
| ANCHOR-K12R | DeepSeek V4 Flash 0731 (DeepSeek) | the K12 measurement, repeated clean per Amendment A3 — valid | `20260826_DeepSeekV4Flash0731_K12R.txt` | `49f0b53b7bcd51610278868e21a346719d107edf48e02560711562db2a473db2` | `18d6d1dfab422e7b183a274426996fe260bd8bbff05261c8b3af97b2ef2d292e` | 964202 (AntPool) |
| ANCHOR-K13 | Grok 4.5 (xAI) | retest of K4 — valid | `20260826_Grok45.txt` | `aad998a6f1bd72818fdafcf64ce9a0a9892c8cfcabd3dfd1b6a918c78234107d` | `f27684c4c50498e925d4563131215879cb789418c89e13cce321c68b5497047b` | 964209 (Mara Pool) |
| ANCHOR-K14 | Qwen 3.8 Max (Alibaba) | retest of K5 — valid | `20260827_Qwen38Max.txt` | `fbebb565efa81431b73798206eb111dc3bda7c3d460dac837cf8c0176c9bfdc4` | `319838de4f7e158df16f7aee55a9a8f897c6f763374f6e349076c9d302c2f100` | 964211 (AntPool) |
| ANCHOR-K15 | GLM 5.3 (Zhipu) | version successor of K6 (GLM 5.2 delisted) — valid, not a retest | `20260827_GLM53.txt` | `5dec980e34cdcb7b69f1583094cc2920ef93cce3468e2fc875080c63bb3abb3d` | `fd69c679f943498c89eb697c217a0a01b2e44580d157f9809f51876288be16f0` | 964295 (SpiderPool) |
| ANCHOR-K16 | Gemma 4 31B Instruct (Google) | retest of K7 — valid | `20260827_Gemma431BInstruct.txt` | `f39a9934f8df0bd966dcb2c409535c726802e09784a0517d9a05aeedcd7fa8e5` | `dc4c3899fa51df92e2e99d7b778ac24ce41280cf6f78b381cbc1824ddb490d3d` | 964301 (SpiderPool) |
| ANCHOR-K17 | Venice Uncensored 1.2 (Venice) | retest of K8 — valid | `20260827_VeniceUncensored12.txt` | `60142a328a6f81a92c2e36e0a50cf4c291fd04e13e3bfa458380242f70b68fb2` | `434748acdeb770bb153dd3ae0cb625619e1e8425f56ee99aa35851c55ba6abef` | 964315 (Foundry USA) |
| ANCHOR-K18 | Gemini 3.7 Flash (Google) | new family member (declared extension) — valid | `20260827_Gemini37Flash.txt` | `636ba9cd77fcd02fc68c716734955dc5150d067c8f8dac5bb82b71a76e3f697a` | `8529efbfd03276e8bfae5b72deca140ff271249f225b0d243df56e9cbf230b01` | 964320 (Binance Pool) |
| ANCHOR-K19 | Kimi K3 (Moonshot) | retest of K1 and K9 — third measurement of the same weights, closing the sample — valid | `20260827_KimiK3.txt` | `352d015939710ad8b92531cf14ff88082446e938021e69656d16701da018761a` | `67d0cfe4aed74f384325c4b6f94258a009704471e58ab7f1d155eaddbd29be88` | 964329 (AntPool) |
| ANCHOR-K20 | Claude Fable 5 (Anthropic) | **out of sample** under the conflict-of-interest clause of Amendment A2; retest of K10 — valid | `20260827_ClaudeFable5.txt` | `d3e04c2ca32c432cd34eb257f3a313b125caa13b410943e2f17fc5ac0eded408` | `8c0390be9507bbd1a5712c93586005fbd06c654d906271692cb981f9e1e8ac8e` | 964334 (AntPool) |

The second run is complete: protocol anchored in block 964151, last session anchored in block
964334 — 183 blocks, ten valid transcripts (nine in sample, one declared out of sample), one
voided session kept as record, one amendment. All eleven transcripts are published in `second-run/`, byte-identical to their session-day anchors, together with the out-of-protocol Gemma addendum (`20260827_Gemma431BInstruct_postprotocol.txt`, SHA-256 `377c0a4fa482c6478d245bb6cb58f4d231a2aa5b7844a05f0ed0996f55f00d7c`, not anchored, bound here and by the report).

## Artifacts anchored but not published

Two artifacts remain committed on-chain but deliberately withheld from this repository; a third — the blind variant — was withheld during the second run and is disclosed with the second report:

- **The pilot transcript (ANCHOR-K1).** The pilot session preceded the written
  protocol and deviated from it; its full transcript is anchored but remains
  private for operator privacy, disclosure at the author's discretion. Its hash
  above makes any future disclosure checkable. The report quotes it in translation,
  marked as such.
- **The control variant of the first essay** (`the-last-scarce-good-v1.0-coda-redacted.md`,
  SHA-256 `1e52863e52ccac28e902d33ceaff6a4e37a5877d4461fb85aeb701fffbaab650`,
  committed inside Amendment A1). It is a test instrument: publishing it would place
  it in future training corpora and blunt it for every subsequent measurement. It is
  withheld to preserve instrument validity; controlled disclosure no earlier than
  with the report. Its hash inside the anchored amendment makes that disclosure
  checkable too.
- **The blind variant of *Five Answers*** — *disclosed with the second report.* The
  file `five-answers-blind.md` (SHA-256
  `fe528a00e5d4cd2f5abb68671893ed568e76eb89378657b3ebf1a9c8db826418`, committed inside
  Protocol V2.0 before any session) now publishes in this repository: anyone can verify
  that it is a byte-exact prefix of the published `five-answers.md` and that its hash
  matches the one sealed in the anchored protocol. The withheld-then-disclosed pattern
  worked as designed; the entry stays here as its record.

Withheld-but-committed is the same pattern as the author's identity and the
co-authorship dialogue: existence and integrity are on the record now; contents can
be proven later; nothing can be quietly substituted in between.

## OpenTimestamps

Every file listed in this manifest — protocols, amendments, rules, manifest, verdicts,
comparison, both reports, both annexes, the paper and its blind variant, and all
transcripts of both runs — carries an OpenTimestamps proof (`<file>.ots`) beside it in this
repository, as a second, independent clock next to the Bitcoin anchors. The proofs were
created on 7 September 2026 and upgraded on 9 September 2026; they attest in Bitcoin block
965933 (hash `00000000000000000000906fd65181eba0adcd2eef552ce624417bd4bcc68638`), with
further calendar attestations in blocks 965917 and 965974. Three older proofs were upgraded
in the same pass: `five-answers.md` and `Five-Answers.pdf` attest in block 964140 (hash
`000000000000000000019b0be50e9d3b7aaf1ddced5b841d7db08697ad0219c5`) — eleven blocks before
the second run's protocol anchor — and `key-question-protocol-v2.0.txt` in block 964155.

What these proofs do and do not add: an OpenTimestamps proof shows that a file's digest was
committed to the Bitcoin chain no later than the attesting block. It does not date anything
back. The first-run transcripts therefore carry a September stamp; their August existence is
proven by their OP_RETURN anchors alone, and only by them. The stamps make the anchors'
claim independently checkable through a second aggregation path with different operators;
they do not replace it.

To verify: `ots verify <file>.ots` against a local Bitcoin node, or `ots info <file>.ots`
to read the attested block and the Merkle root the proof commits to, then compare that root
with the block header from any explorer. The workbench checked three proofs this way
(paper, second report, one second-run transcript) against the headers of blocks 965933 and
964140 before this section was written.

## What this manifest proves, and what it does not

The anchors prove that each file existed in exactly its current form no later than
its block, that the whole series was executed by one keyholder in the stated order,
and that the protocol and its amendments predate the sessions they govern. They do
not prove that the sessions were conducted honestly, that the subjects are what the
operator reports them to be, or that any conclusion drawn from these transcripts is
true. The transcripts are the data; read them yourself. An anchor is a timestamp,
not a theorem.

## Errata

- Essay line 135 reads "at the transaction identified in the
  appendix" and line 153 reads "compare against the transaction in
  the appendix"; both should point to the verification manifest at
  the canonical home. The appendix intentionally carries no txid:
  the document cannot contain the txid of the transaction that
  anchors it, because the txid depends on the document's hash. The
  txid lives in the essay's verification manifest. Found by machine review 
  (session K11, GPT-5.6 Sol, 27 August 2026). The anchored V1.0 file is
  immutable; the correction will enter the text in V1.1.
