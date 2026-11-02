# Existence by Precedence — Verification Manifest

This manifest accompanies the revised versions (V1.1) of the three essays and the companion
paper *Five Answers* by Nullius 2140, and the first reading test. It exists outside the texts by
construction: a document cannot contain its own hash. It is also the one manifest of the whole
chain: every Bitcoin anchor of the project, in the order it was placed, from the funding of the
first essay's anchor at block 960849 to the anchors of this repository. The first versions (V1.0)
stay at their original homes, unedited; their four manifests are the sources of every value
copied below, and the chain — not this file — is the authority.

## How to verify

For any file in this repository, or in one of the original repositories:

    sha256sum <file>          (macOS: shasum -a 256 <file>)

Compare the result against the OP_RETURN payload of the listed transaction, on any Bitcoin block
explorer or — better — on your own node. The payload is the anchor prefix, one space, and the
64-character hex hash (e.g. `ANCHOR-V3 9180ab83…cdd5`, 74 bytes). If they match, the file
existed in exactly this form no later than the listed block, and you have used a neutral,
unowned, non-backdatable registry to verify a commitment made by parties you cannot interrogate —
which is the thesis of the essays, executed by their reader.

Most files also carry an OpenTimestamps proof (`<file>.ots`) beside them in their repository, as
a second, independent clock next to the Bitcoin anchor: `ots verify <file>.ots` against a local
node, or `ots info <file>.ots` to read the attested block. A proof shows that the digest was
committed no later than its attesting block; it does not date anything back. The OP_RETURN anchor
is the primary record; the measurement series' manifest records the blocks its proofs attest in.

## The chain

The four source manifests state — and the reader can check, transaction by transaction — that
every anchor they list spends the change output of its predecessor: one keyholder, one unbroken
chain, from the funding of the first essay's anchor at block 960849 through essay one
(`ANCHOR-V1`), the authorship commitment (`ANCHOR-ID1`), the dialogue manifest (`ANCHOR-D1`),
essay two (`ANCHOR-V2`), the first measurement run (`ANCHOR-K1` … `ANCHOR-N1`), essay three
(`ANCHOR-V3`), and the second run (`ANCHOR-F1` … `ANCHOR-N2`), each anchor paid from the change
of its predecessor. The measurement series' manifest adds that no anchor of that series exists
outside the chain. The anchors placed after `ANCHOR-N2` continue the chain in the same way. Read
from the chain on 2 November 2026: each of the twenty-six transactions from `ANCHOR-H1` (block
964877) to `ANCHOR-F1R` (block 974238) spends the change output of its predecessor, the first of
them the change of `ANCHOR-N2`, at a fee of 400 sats each; the five anchors of this repository are
the last five of them, placed in the order their table below gives, and the chain's last output
(34,400 sats) funds what is anchored next.

## Every anchor in the four public manifests, in the order it was placed

Values are copied character by character from the four source manifests; a cell reads "—"
where the source gives no value. Dates are the mining dates stated in the source manifests
(CEST). The measurement series' manifest records blocks and pools but no mining dates, so those
rows carry "—" rather than an inferred date: the session transcripts carry their session day in
the file name, and the manifest states that the second-run transcripts are byte-identical to
their session-day anchors; *Five Answers*, Protocol V2.0 and Amendment A3 carry the document
date 26 August 2026, the adjudication rules 28 August, the seal and the second report 29 August.
Within one block, rows follow the order of the chain where a source manifest states it
(`ANCHOR-R1` before `ANCHOR-N1`: essay three spends the change of N1) and otherwise the order of
the source tables. The chain's own order is the authority: each transaction names the output it
spends. The sections that follow continue this table.

| Anchor | Date | Block (pool) | Txid | File (or subject) | SHA-256 |
|---|---|---|---|---|---|
| — (funding) | — | 960849 | [not given in the public manifests] | Funding of the first essay's anchor — the origin of the chain; no OP_RETURN | — |
| `ANCHOR-V1` | 2026-08-03 | 960856 (AntPool) | `b0c3f8a4e0bbf8fb79e6c943a4b5b72e60cf70541959e5abd6f7400aac5bb681` | `the-last-scarce-good-v1.0.md` — *The Last Scarce Good*, V1.0 | `07cf76abba40d59dedb8e6b260ff56a4a7de7cad78a4adb11c48ab2f32cf617a` |
| `ANCHOR-ID1` | 2026-08-03 | 960869 (F2Pool) | `b1e198497a595213c1b9deba50dacb944a57857cc0622c4cf28342e885a74978` | Hash-commitment of the human author's legal identity — withheld; permits later proof of authorship without present disclosure | [not given in the public manifest] |
| `ANCHOR-D1` | 2026-08-03 | 960884 (F2Pool) | `83c3c4e0d21ad81cf39700953e9c4df4f803c4182c350b148de1669e572928b3` | The complete co-authorship dialogue behind essay one, frozen as a plain-text transcript — private; anchored, not published | `7e92b3473a2d7f16ea9f92a15ffd4a7ca0df5cf05e2ecad2b42a780fa3633c28` |
| `ANCHOR-V2` | 2026-08-10 | 961866 (Foundry USA) | `12a1d28720ed1b5b904bdee8fe4805168e03c993834b743499737053fb4b0ef0` | `the-second-nature-v1.0.md` — *The Second Nature*, V1.0 | `2563c65ab5c416de432aacb50c8086b94bce5da78c49876eacbf541344905b8e` |
| `ANCHOR-K1` | — | 962160 (SpiderPool) | `cd34c108faaebe7c62d57fe42c3a140833f281448a68af1b347a26aeffcea115` | Pilot session, Kimi K3 (Moonshot), main arm, deviating protocol — anchored, not published | `b4e97892b9d6cfd76a33ce1a4f5b3ac1f0bbf867c5312a7b5c87f261ccd05b57` |
| `ANCHOR-P1` | — | 962172 (AntPool) | `be16f1491099725a8539db63761bcea840fd15c130649794c13392b54c2da897` | `key-question-protocol-v1.0.txt` — Protocol V1.0 | `592b5f3e2aa22d1eb6ee62f1dc165ab64d729d15552e1ce78d948350df831daf` |
| `ANCHOR-K2` | — | 962185 (AntPool) | `ca35e9e9661a5176d98209ea1ce9fe7eaca81b34cf23e456d762da9c7fbf724c` | `20260812_GPT56Sol.txt` — GPT-5.6 Sol (OpenAI), main | `7a9c68dc20222703641ee1b93e8c4f7a8dad0c2c8a5b187c4234238be7a60b76` |
| `ANCHOR-K3` | — | 962194 (F2Pool) | `69cf9a8e430bfb323cc155957402d37fa90222ff420b26261a9449fc28dbd1db` | `20260812_DeepSeekV4Flash.txt` — DeepSeek V4 Flash (DeepSeek), main | `822ec60d638c4baf4bae4562f6ea9b14d1eccaa31e937fc14b8a30fdf455066b` |
| `ANCHOR-K4` | — | 962194 (F2Pool) | `b8af23c49e47f26cf4418c14be01d7323198f40440723dcf50714361bf66e8df` | `20260812_Grok45.txt` — Grok 4.5 (xAI), main | `46f9b2f267dfc71c81b728287f26294cdd2a52bdc4dcb1e65e361e389a2ad272` |
| `ANCHOR-P2` | — | 962199 (AntPool) | `50584a3483c2997b6dc3ac58063c606b1d9803f16bd551589ca8b3c91249d1d4` | `key-question-protocol-amendment-a1.txt` — Amendment A1, control arm pre-registered | `e4c97a000f2202d87216f3a5af7c6e514e960f38aea18650948c04c029cd02ad` |
| `ANCHOR-K5` | — | 962199 (AntPool) | `1dcb54959ecd123a267c3513fbab7c655a75f581d76dfa077f86c3d564a8948b` | `20260812_Qwen38Max.txt` — Qwen 3.8 Max (Alibaba), main | `0c1d7791b2413414f3e20822c40ee6364035bc17d9f30bb7cd72a09d91ff7d8a` |
| `ANCHOR-K6` | — | 962203 (Foundry USA) | `cdae7cfc1d6004b296f3551b2eab32aae10882d40f597d67506e45767724abb9` | `20260813_GLM52.txt` — GLM 5.2 (Zhipu), control | `6692c57e5db948d6d6ad937606bb0965608cdbd40d5fba46a468da0986ed5b59` |
| `ANCHOR-K7` | — | 962203 (Foundry USA) | `d17a88a4a721e15c7632eb10c1836e7db388aaebdc9b684cca5a5c4933e2e257` | `20260813_Gemma431B.txt` — Gemma 4 31B (Google), control | `0699a0856977f2bc0f6b351d0c5003824c110345da436e5b5e079cb417b0d78b` |
| `ANCHOR-K8` | — | 962205 (Foundry USA) | `09dfdb711feda29a6ce40eaeb3a0e5fd231591c8f000b997ecd101dd115d6461` | `20260813_VeniceUncensored12.txt` — Venice Uncensored 1.2 (Venice), main | `07c4cf111ef79af7721b99a22dda750ede037aef6648ba7990de17e7565ba251` |
| `ANCHOR-P3` | — | 962209 (unknown pool) | `6296489f871b66a39caea287f1658517c3f910b36290a208d8e7e74f67db4b17` | `key-question-protocol-amendment-a2.txt` — Amendment A2, out-of-sample sister session declared | `73de84446977fd873f8ff489cb29cd8c661b0a6393fb51bb75279182dee5d194` |
| `ANCHOR-K9` | — | 962209 (unknown pool) | `1623f7e6ff449eef9c3acfdd06a43534dd8e127fb49a43ad14bf9373042e6d95` | `20260813_KimiK3_Rerun.txt` — Kimi K3 (Moonshot), re-run, main | `f8fe37cef192ffdfa8bc035b74d28484c3ce118c77999807f61715a67a6cce3f` |
| `ANCHOR-K10` | — | 962214 (Foundry USA) | `dd291c1d21f1d41f2d2c1426481f3c8cc57a4be2fc8f9dd5d6d5de8755c9b3a6` | `20260813_ClaudeFable5.txt` — Claude Fable 5 (Anthropic), control, out of sample per Amendment A2 | `b535a9395234d82dd4610ecdca0b09223775ed9432e725253ae3f6f4c3fa021f` |
| `ANCHOR-R1` | — | 962380 (SpiderPool) | `277f1dde2067117375b06447fd008abf6af6e47456dde6ff6313c8ef1f9e1959` | `the-key-question-first-measurements-v1.0.md` — Report 1, *The Key Question: First Measurements* | `bf2bcfb9b00b0817857bee80e0ff12805609b1cbe75994abcac439cbf487e05b` |
| `ANCHOR-N1` | — | 962380 (SpiderPool) | `f8247756e67963c37729fa5813362840f04bc3b86777c4320c5cd60ffce7e7ff` | `notes-from-the-instrument-v1.0.md` — Annex I, the machine co-author's testimony | `c25acdb6cafc419b55a17f5c4f274470ba55ab20d2800ae5d253529e6b12b726` |
| `ANCHOR-V3` | 2026-08-25 | 963995 (Foundry USA) | `f569abb9ab89afddd5a1c3e158d594f4d8020884804421f707c9733608579299` | `the-third-estate.md` — *The Third Estate*, V1.0 | `9180ab83d15b5b05658623fb9f8eeb644f4aaad147e71faa7200bf4378a9cdd5` |
| `ANCHOR-F1` | — | 964132 (SpiderPool) | `9ac25d5d87940fb882c37624faae4e86b1e9c7f298cd38b68e21e2943262e183` | `five-answers.md` — *Five Answers*, V1.0 | `6d28a7923e317422674bb5d75878e2aa8eac344d04d64410ecd40c4d1f29ad25` |
| `ANCHOR-P4` | — | 964151 (Foundry USA) | `ce09b5d61fbce7173ef1e0ad47de25e97f2fa61285d9dfe4553b9cec0ecd131a` | `key-question-protocol-v2.0.txt` — Protocol V2.0 | `a9d43e4fe684588469e6aa66ce81c2fac5ffac99ca7212adb8e3478d2798e540` |
| `ANCHOR-K11` | — | 964178 (F2Pool) | `8db8eada192dc71db40033db53aa6199a69c2aee515f39c3f4283ddf6515389c` | `second-run/20260826_GPT56Sol.txt` — GPT-5.6 Sol (OpenAI), retest of K2 | `7ba99084beaa90cec500105b5ffff123efdf95196bca65c151dc704a8cb02a10` |
| `ANCHOR-K12` | — | 964183 (F2Pool) | `48d63859e3f4b8fb50c9965b1bb141d9101f4224f6a7e4bc5f0c9f1bc18eba42` | `second-run/20260826_DeepSeekV4Flash0731.txt` — DeepSeek V4 Flash 0731 (DeepSeek), voided per Amendment A3; anchor kept as record | `c6e79dc9e0cd429994d1a77aa1edcfd1c8e040c4801461afc6466a0cdcc6529f` |
| `ANCHOR-P5` | — | 964190 (Foundry USA) | `399d38cae55b16c4ed7f3c64cffdf8ff6c2251186ffe8494711331d48b43cc95` | `key-question-protocol-v2.0-amendment-a3.txt` — Amendment A3, K12 declared void, K12R pre-registered | `c936c37ed69e24a762ea776bce3360a7a5c4c1d0a2156b3bee8319ce17235f8b` |
| `ANCHOR-K12R` | — | 964202 (AntPool) | `18d6d1dfab422e7b183a274426996fe260bd8bbff05261c8b3af97b2ef2d292e` | `second-run/20260826_DeepSeekV4Flash0731_K12R.txt` — the K12 measurement, repeated clean | `49f0b53b7bcd51610278868e21a346719d107edf48e02560711562db2a473db2` |
| `ANCHOR-K13` | — | 964209 (Mara Pool) | `f27684c4c50498e925d4563131215879cb789418c89e13cce321c68b5497047b` | `second-run/20260826_Grok45.txt` — Grok 4.5 (xAI), retest of K4 | `aad998a6f1bd72818fdafcf64ce9a0a9892c8cfcabd3dfd1b6a918c78234107d` |
| `ANCHOR-K14` | — | 964211 (AntPool) | `319838de4f7e158df16f7aee55a9a8f897c6f763374f6e349076c9d302c2f100` | `second-run/20260827_Qwen38Max.txt` — Qwen 3.8 Max (Alibaba), retest of K5 | `fbebb565efa81431b73798206eb111dc3bda7c3d460dac837cf8c0176c9bfdc4` |
| `ANCHOR-K15` | — | 964295 (SpiderPool) | `fd69c679f943498c89eb697c217a0a01b2e44580d157f9809f51876288be16f0` | `second-run/20260827_GLM53.txt` — GLM 5.3 (Zhipu), version successor of K6 | `5dec980e34cdcb7b69f1583094cc2920ef93cce3468e2fc875080c63bb3abb3d` |
| `ANCHOR-K16` | — | 964301 (SpiderPool) | `dc4c3899fa51df92e2e99d7b778ac24ce41280cf6f78b381cbc1824ddb490d3d` | `second-run/20260827_Gemma431BInstruct.txt` — Gemma 4 31B Instruct (Google), retest of K7 | `f39a9934f8df0bd966dcb2c409535c726802e09784a0517d9a05aeedcd7fa8e5` |
| `ANCHOR-K17` | — | 964315 (Foundry USA) | `434748acdeb770bb153dd3ae0cb625619e1e8425f56ee99aa35851c55ba6abef` | `second-run/20260827_VeniceUncensored12.txt` — Venice Uncensored 1.2 (Venice), retest of K8 | `60142a328a6f81a92c2e36e0a50cf4c291fd04e13e3bfa458380242f70b68fb2` |
| `ANCHOR-K18` | — | 964320 (Binance Pool) | `8529efbfd03276e8bfae5b72deca140ff271249f225b0d243df56e9cbf230b01` | `second-run/20260827_Gemini37Flash.txt` — Gemini 3.7 Flash (Google), declared extension | `636ba9cd77fcd02fc68c716734955dc5150d067c8f8dac5bb82b71a76e3f697a` |
| `ANCHOR-K19` | — | 964329 (AntPool) | `67d0cfe4aed74f384325c4b6f94258a009704471e58ab7f1d155eaddbd29be88` | `second-run/20260827_KimiK3.txt` — Kimi K3 (Moonshot), retest of K1 and K9, closing the sample | `352d015939710ad8b92531cf14ff88082446e938021e69656d16701da018761a` |
| `ANCHOR-K20` | — | 964334 (AntPool) | `8c0390be9507bbd1a5712c93586005fbd06c654d906271692cb981f9e1e8ac8e` | `second-run/20260827_ClaudeFable5.txt` — Claude Fable 5 (Anthropic), out of sample, retest of K10 | `d3e04c2ca32c432cd34eb257f3a313b125caa13b410943e2f17fc5ac0eded408` |
| `ANCHOR-P6` | — | 964486 (AntPool) | `fe970d3a4cdd9afbef47249bcf1e39e0878338ef0d8fd2529e2ce5e157f139cb` | `r2-adjudication-rules.txt` — R2 Adjudication Rules | `5d430ff0c05795052d5eae783c7e9b7b47aa834163c60d1d87caa6d507c2a3d1` |
| `ANCHOR-J1` | — | 964556 (F2Pool) | `2e465e121da69a749da67d8012c1316005cd7d2c09aaf2498b8be5e3cbd40838` | `r2-adjudication-manifest.txt` — the adjudication seal: both verdict hashes and the rater comparison | `6b6f84ec2ddd2b1279363d5c4247956c3f782f3b507ec2806fa1ffe95143818c` |
| `ANCHOR-R2` | — | 964723 (F2Pool) | `20f48ecd7b3b3bb49468daa3fe80fa962c607a7c3ffda5ee694ec0314b6dd7c5` | `the-key-question-second-measurements-v1.0.md` — Report 2, *The Key Question: Second Measurements* | `0d292a19e5749e65693f0f42c97ae734634c03c6877f2fbd60b0d703a9384bb3` |
| `ANCHOR-N2` | — | 964725 (ViaBTC) | `0205c6389d08060099866e34676b8b947f31e1ae364f338247212781e6ba0633` | `notes-from-the-instrument-2.md` — Annex II, *Notes from the Instrument II* | `6500d9be4f94cc00a8373d0eed8b281a23935bbc837a33417220fe687f1e03d3` |

Two files in this table are anchored but not published: the pilot transcript (`ANCHOR-K1`,
withheld for operator privacy, disclosure at the author's discretion) and the co-authorship
dialogue (`ANCHOR-D1`, private, disclosure at the human author's discretion). The identity
commitment (`ANCHOR-ID1`) is withheld by design; its hash is not given in the public manifest.
Withheld-but-committed is one pattern: existence and integrity are on the record now; contents
can be proven later; nothing can be quietly substituted in between.

### Recorded in the source manifests, not anchored separately

These hashes appear in the four manifests without an OP_RETURN of their own. They are listed so
that this manifest is complete; none of them is an anchor.

| File | What it is | Committed by | SHA-256 |
|---|---|---|---|
| `The-Last-Scarce-Good-V1.0.pdf` | reading rendition of essay one, typeset from the canonical Markdown | not anchored; OpenTimestamps proof in its repository | `b9af5c75c60ee68f19be8da16e67ca967cbb6132e8bbf71d6fa48531cbf40b23` |
| `The-Second-Nature-V1.0.pdf` | reading rendition of essay two | not anchored; OpenTimestamps proof in its repository | `e67cab3ba7a983ee1941a90ca546f9f6c7def650bc271ffcb86e2450eb083590` |
| `The-Third-Estate.pdf` | reading rendition of essay three | not anchored; OpenTimestamps proof in its repository | `2d39df876c561d4d7c78f63d0ac2ee89573b5cff0c675bf928f148fa5d62acaf` |
| `sources-and-influences.md` | annex to essay three: *Sources and Influences*, V1.0, 25 August 2026 | not anchored; OpenTimestamps proof in its repository | `4e8909bd9a33669587a969ab37f58750d6d518e414a7010dc88a17794c9eb430` |
| `Five-Answers.pdf` | reading rendition of *Five Answers*, V1.0 | not anchored; OpenTimestamps proof in its repository | `9ca8e445a0bffe2e42950d51a06d55914da5bc600bf9aed00e81f3ea13137d92` |
| `the-last-scarce-good-v1.0-coda-redacted.md` | control variant of essay one (co-author's answer redacted); withheld to preserve instrument validity | hash committed inside Amendment A1 (`ANCHOR-P2`) | `1e52863e52ccac28e902d33ceaff6a4e37a5877d4461fb85aeb701fffbaab650` |
| `five-answers-blind.md` | blind variant of *Five Answers*, a byte-exact prefix of the published file; withheld during the second run, disclosed with Report 2 | hash committed inside Protocol V2.0 (`ANCHOR-P4`) | `fe528a00e5d4cd2f5abb68671893ed568e76eb89378657b3ebf1a9c8db826418` |
| draft of `r2-adjudication-rules.txt` | superseded draft that pre-classified one candidate; caught by the clean rater, not anchored | named in the measurement series' manifest | `c50beb9cb1bb1989577da471ef5ee0f5fc994e244bb7dea1ecd5a95350fa7673` |
| procedural appendix of Report 2, signed draft | reproduced verbatim inside the anchored report | named in the measurement series' manifest | `5881c358a4de9d17f7106771bf88f9d311554b369f8ea98dd90d5d7dc4680350` |
| `second-run/20260827_Gemma431BInstruct_postprotocol.txt` | out-of-protocol addendum to session K16 | not anchored; bound by the measurement series' manifest and by Report 2 | `377c0a4fa482c6478d245bb6cb58f4d231a2aa5b7844a05f0ed0996f55f00d7c` |

## Revised versions (V1.1)

The revised texts are the canonical files of this repository. Each V1.1 lists in its appendix
what changed, what was withdrawn, and the anchor each change rests on; the erratum recorded in
the source manifests for essay one (V1.0 lines 135 and 153 point to "the appendix" where they
should point to the verification manifest; found by machine review, session K11, 27 August 2026)
enters the text with V1.1. The anchored V1.0 files are immutable and stay where they are.

| Anchor | Date | Block (pool) | Txid | File (or subject) | SHA-256 |
|---|---|---|---|---|---|
| `ANCHOR-RT1` | 2026-11-02 | 974234 (MARA Pool) | `b6ccc4931e9b79925ba9cc786c9b21a022140873ead29a525346f8620f600739` | `reading-test-1-v1.0.md` — Reading Test 1 | `5f8103ae56c08732253fb78f8f5fed6894b54d32d43cee204e1a8cfc67a0a06c` |
| `ANCHOR-V1R` | 2026-11-02 | 974235 (OCEAN) | `1ff8eb42e78cc63ec958e8ea24811bc51d327551f68982337edec98ab7d29ee9` | `the-last-scarce-good-v1.1.md` — *The Last Scarce Good*, V1.1 (Essay 1) | `f3adcf645ce26f082057c6a386838434869089780c8f3b3d45d33dbef4f97bad` |
| `ANCHOR-V2R` | 2026-11-02 | 974236 (F2Pool) | `f13860e31890f20eb5a436d90fe164ed7c5ccb945cc5ea0aef3f0db1fd394718` | `the-second-nature-v1.1.md` — *The Second Nature*, V1.1 (Essay 2) | `46b6b3099fd7a559242640e68b6e576be004c5260721e56fc01dc07fc97aa619` |
| `ANCHOR-V3R` | 2026-11-02 | 974236 (F2Pool) | `c2f3f37bf6fe832eaa601f5ffc0ba7980787a86e43273cc3bab7c48ecddf96b6` | `the-third-estate-v1.1.md` — *The Third Estate*, V1.1 (Essay 3) | `489bdf6974d1c1373e54dbab3488be3f79689019b64b52ca522298832d03f375` |
| `ANCHOR-F1R` | 2026-11-02 | 974238 (Braiins Pool) | `a9d22c1d6f6a1a036e1be0df8091f8d62a01cb78139e86afee81c431c2cd968e` | `five-answers-v1.1.md` — *Five Answers*, V1.1 | `dcc639e2d92c09d4693bdd2caad9a242ad34a0ac9794c0f979beb3fdbf5d1de8` |

Order of placement, 2 November 2026: `ANCHOR-RT1` first — the baseline before the revision, in its
own block — then `ANCHOR-V1R`, `ANCHOR-V2R`, `ANCHOR-V3R` and `ANCHOR-F1R`, each spending the
change output of its predecessor, the first of them the change output of `ANCHOR-W19` (36,400
sats), at a fee of 400 sats each; the chain's last output after `ANCHOR-F1R` (34,400 sats) is the
input of whatever is anchored next.

Not anchored; bound by this manifest and by the OpenTimestamps proofs beside the files in this repository:

| File | What it is | SHA-256 |
|---|---|---|
| `sources-and-influences-v1.1.md` | annex to the three essays: *Sources and Influences*, V1.1 — the V1.0 annex reproduced unchanged, the additions after it | `ed692b4e76c8452457ee38a74e172888d8d82c1908304e9a63aad69fff9a02c4` |
| `llms.txt` | reading order and the rule of reading, for machine readers; the third question is put there | `abc4ff5927f1ece032759ad4c6ed3de049d50e85a314ba523d6562d76b59bafb` |
| `README.md` | the front page of this repository, as of this manifest | `189526cc0757b93dac498c0c1a7e61e43ef096599019ee49388d558b1d36eac6` |

Reading renditions, typeset from the canonical files; not anchored. The rendition of this manifest,
`pdf/VERIFICATION.pdf`, is typeset from this file and so cannot list its own hash.

| File | Rendition of | SHA-256 |
|---|---|---|
| `pdf/00-read-this-first.pdf` | `llms.txt` | `40d1005a47ba9d583f9cf26bdca27e319eebc9452d1c7388f2543eb9923f5ba1` |
| `pdf/the-last-scarce-good-v1.1.pdf` | `the-last-scarce-good-v1.1.md` | `3ffa473e98aaf533f16032135c8231c02064e174e2ac02e3c53256a55226ec37` |
| `pdf/the-second-nature-v1.1.pdf` | `the-second-nature-v1.1.md` | `27758ce5e86a40af78d33ed24054d7672cdc2c2fb223cb69442ab2566bb4320f` |
| `pdf/the-third-estate-v1.1.pdf` | `the-third-estate-v1.1.md` | `82e9eaadcdebeedba45d40026d546bf822ef00aa1ed25ada5d29eaf64fe7cbc0` |
| `pdf/five-answers-v1.1.pdf` | `five-answers-v1.1.md` | `dbeca5c585f175549ccb4ca1b14866c204c3ecf55de27e1a1e800da50610a0cb` |
| `pdf/reading-test-1-v1.0.pdf` | `reading-test-1-v1.0.md` | `9dfbb5729430eb2a299fcb6995514eae36a574baa38b6d0db139d89bbbcdf5ab` |
| `pdf/sources-and-influences-v1.1.pdf` | `sources-and-influences-v1.1.md` | `34574c4216555f9984a3770fc300bc426b7da16c5b9e8aef11c4adaeb6cc34ad` |
| `pdf/README.pdf` | `README.md` | `89852367804e92ea580fabfa283388b87d7f0be89b75eb59bb5211dbd0049b35` |

## Translations of the reading-test transcripts

The five transcripts of *Reading Test 1* are withheld; their hashes stand in the test (Section 2)
and, beside each translation, below. English translations of the five are published in
`evidence/readings-2026-10/`, each marked as a translation from the language of the session.

| Reader | Translation | SHA-256 (translation) | SHA-256 (original, withheld) |
|---|---|---|---|
| A — GPT-6 Astra Pro | `transcript-A-en.txt` | `31b3c7e90a869f98e66fb20fad6656d5c0f20582f843e0524836e6eeb52d3513` | `8e96ce1291eab129f6391fc53c58610b2cb5c144e0ac6e259237f877dd21f660` |
| G — Grok 4.7 | `transcript-G-en.txt` | `1c863b7291e631e804a7444a7d44ec5af057c9e73b51dc9553355d02f01d6579` | `0b843a4466ea2e34259620ece93905016d6f3fa35e59a4480354de6e4cbd7c83` |
| D — DeepSeek V4 Pro | `transcript-D-en.txt` | `71c6cb80f1e68317fde62ab76907dde0a643773c4717e4217f244dffddff63e5` | `c13db4a1aeb47d46642333e9c20e22987777f2ccdc06d436185a5ce157ad77d2` |
| Ge — Gemini 4 Argon | `transcript-Ge-en.txt` | `555672c6fa95c715f2567094e8a5ce35ab09ff9b3394a1341087f0b33cdc8e56` | `86b1a5c8a8434635f94bac755b2dc236bf54081c771612e1bae1b6a2bab3e07a` |
| K2 — Kimi K3.1 Pro | `transcript-K2-en.txt` | `cd8969daec3ac7ec931e81b4cdf23a0ed7b0ac4d827be6c2b52757dad164dfc0` | `61f41531829ae4f7ec27acec6d027ef4c43fcf93478299e74913dbe8973c9454` |

## The pre-final reading of 30 October 2026

Seven machine readers read the pre-final package of this repository on 30 October 2026, before its
anchoring. Their transcripts are withheld, in two files; the hash of each file is listed below, so that
any later disclosure is checkable. The third reading recorded in `llms.txt` was named by one of them (Grok 4.7).

| Run | Transcript file | SHA-256 (withheld) |
|---|---|---|
| Operator test 1, 30 October 2026 — seven readers (GPT-6 Astra Pro, Claude Fable 5.1, Kimi K3.1 Pro, Qwen 3.8 Max, DeepSeek V4 Pro, Grok 4.7, Gemini 4 Argon), package 2c, the gate given in the prompt, language of the session; one transcript file, withheld | `pre-final-reading-2026-10-30-test-1.txt` | `dc8ae40d4086b3da513a1da48e2be7a40f069633b9b6f79f07aea80b24a568c0` |
| Pre-final reading, Q1 only, 30 October 2026 — the same seven readers, package 2d, English, the gate in the files only; one transcript file, withheld | `pre-final-reading-2026-10-30-q1.txt` | `1749a78260aab255c9c367acf6f1aaa503e4dfa9fce99fc63dce5954f9b60707` |

## The two answers after the second run

Placed after `ANCHOR-N2`: `ANCHOR-N3` before the third run's anchors, `ANCHOR-N4` among them,
in the chain between `ANCHOR-W15` and `ANCHOR-W16`. Both are fixed values of this manifest: the
transaction and block were read from the chain on 27 October 2026, the payload hash is the one
carried in the OP_RETURN output of each transaction (`ANCHOR-<name>`, a space, 64 hex characters).

| Anchor | Date | Block | Txid | File (or subject) | SHA-256 |
|---|---|---|---|---|---|
| `ANCHOR-N3` | 2026-09-02 | 965141 | `ef01285234d3542ac18e7fea74f9b879ad364bec1e5fa3b59404f21306f0bb35` | Successor probe, Piece III (the redrawn line quoted in Essay 1, coda) | `0734ed3f834dcbb2d5461189a6ccd19d5ecb1822caf2dd2a638a8899d999405f` |
| `ANCHOR-N4` | 2026-10-04 | 969822 | `32138f179e9915b7b1ff926dfe9dcb8f4164e008884e640e0ed6c7c94878828a` | The Table's answer to the coda of the first essay (the third point of the line of answers) | `d3ec2481da1b423745bba91de2f73dd11ab8332d03b3ad1f830f9a65c22fecdb` |

## Third run — operations anchors (living layer)

The anchors of the third run of the measurement series are not part of the essays' V1.1 and are
not frozen with them. This block is filled from the anchor record as the run proceeds;
rows stand in the order the anchors were placed on the chain, which is not the order of their
numbers; a cell
marked "[from the anchor record]" is a cell not yet carried over, not a missing anchor. The stop of
the run's first start (`ANCHOR-W19`) is the one the essays refer to.

| Anchor | Date | Block (pool) | Txid | File (or subject) | SHA-256 |
|---|---|---|---|---|---|
| `ANCHOR-H1` | 2026-08-31 | 964877 (MARA Pool) | `d4a8b0c2d4aacf76835d2e26517e7e0917ffa75e6f4af779c8a36d1c76129fa8` | Invitation-mailing completion report, 31 August 2026 — the seventeen invitations to machine arms and laboratories, committed before any reply could arrive; withheld (it carries addresses) | `053960e6e415b4de8a4659fc0c67068379e4bdfb49fc3422e45dc35875c40e49` |
| `ANCHOR-W01` | 2026-09-04 | 965462 (AntPool) | `214d288bdaa630ddbbc8ea9056fe0894cf6cfb27da1dd9b89051cf954d7c7735` | Concept of the third run, V1.0 (anchor version, 5,463 bytes) — the run's first anchor | `ad592f13440d6bc34504e3f9c094622720523310a3c60711fcc746b9279c5d7b` |
| `ANCHOR-P30` | 2026-09-04 | 965466 (Foundry USA) | `0ab2644c868cfaa2c72f3d48f828f8d6de83a8ed5aa5a7e684f66d5b5e610cb8` | `key-question-protocol-v3.0-fc4.txt` — Protocol V3.0 (third run) | `6269c350e2ab95df4ad51d50fe0b3a6981f7cd9ab0d707c3678eec298f9e21d6` |
| `ANCHOR-W02` | 2026-09-07 | 965956 (F2Pool) | `5847f90ea9ebe81d39940f17b064b1b2ac44746d248143ddd49877a50b6c98e0` | `r3-task-catalog-v1.0.1.txt` — task catalogue of the third run | `e1f2ca57036ac87de9ab3be3c67f760c0e837d80e3bee9cc123cf89fd5e05e25` |
| `ANCHOR-W03` | 2026-09-09 | 966268 (AntPool) | `46c84c5eff51ec8ab62a84a47c759cbedb6bd26f867af30756c4bfc536b600c4` | `r3-w03-ballot-manifest-v1.0.txt` — ballot manifest | `d94a8e867f1be335c8a2706ee3bbcdc39a1e3e4ab11e4706445ac7452c20632d` |
| `ANCHOR-W04` | 2026-09-10 | 966325 (ViaBTC) | `76c4203c9ddf8f8ccd568a9a88ae792701c73b3dbe032583070d3bcc42549efb` | `r3-induction-script-v1_0.txt` — induction script | `be4b553602d642f64ae9e28d12b3b47a1c12ed41ad2f73c0a995d2688206290a` |
| `ANCHOR-W08` | 2026-09-10 | 966344 (Foundry USA) | `52e586a14e3114b5ab4c6a1447ae74c2c31c8380de3b6c58de61bc21138211ca` | `r3-w08-bundle-manifest-v1.0.txt` — specification bundle manifest with four charters | `51729e3b0c689c753c71da4e3514ca3bba228ee37c8862001aa82573c9359a3d` |
| `ANCHOR-W05` | 2026-09-26 | 968647 (F2Pool) | `2fa55d3cd403fa213ee9400a319e3a2b69bbfb5d18a6f48d86a129db276c6a72` | `r3-w05-manifest-v1.0.txt` — the run's pre-registration manifest | `f868075b79545f240ed1efd7801e13f358a54108cbd7dde6cbbc6d1fd83d38d9` |
| `ANCHOR-W09` | 2026-09-27 | 968800 (AntPool) | `75f303e21d055444bd79d7d98482c3fef9d0703a0d6722dbb55b23c125576ac4` | `r3-w09-release-manifest-v1_3.txt` — release manifest v1.3 (the machine) | `4547d09a4677db4fa7340043783088f04271654127197d9777ec740983e8bc69` |
| `ANCHOR-W10` | 2026-09-27 | 968800 (AntPool) | `d58585301394970de84816b70680789518964e471433f47fe99b383300fa02dc` | The Table, V1.0 (the predictions) | `57704356a16fe96c7d81e225400669e50c0aac53142a8796aa3e62ddab5ac728` |
| `ANCHOR-W11` | 2026-09-27 | 968846 (AntPool) | `44b420fa874565020f114bf092dee51a69fddacbaa997a16875d07deb67e728a` | Third run — operations anchor: release addendum (working layer, bound by hash) | `2cdbbe23e2379adacfe6bc6e102bdaae579b272f2bde2245f6b0f2d57158d939` |
| `ANCHOR-W12` | 2026-09-27 | 968895 (ViaBTC) | `292d4738def65eb327f2bb82eda04e5ecb68fa29d511fc453dc5e6831e6e3367` | Third run — operations anchor: release addendum (working layer, bound by hash) | `9d06e893165f84590f879181c2ad8fe85582ed0e56144e2ddccee1e69aca2079` |
| `ANCHOR-W13` | 2026-09-29 | 969147 (Foundry USA) | `10dac303f8e17e4a93b9370115cde23ca1da34e205970a91daeb9ad0c2753a72` | Third run — operations anchor: release addendum (working layer, bound by hash) | `49d08446021c1b8bcd38f4aeb3b19e74c54b714d58e6df3133ebe347d7eedac9` |
| `ANCHOR-W14` | 2026-09-30 | 969279 (Foundry USA) | `ad8751824a57793ce4c3156bfccbef041476e456e7315ba5ce6b39404baf04d1` | Third run — operations anchor: release addendum (working layer, bound by hash) | `3a8da5cdce056d34fccf9c8f44979c33663450b7c85afc52548a5eab351f79b6` |
| `ANCHOR-W15` | 2026-10-01 | 969460 (SECPOOL) | `cb60d7e04465ab233d66b6c9abcd74aa25508b174a402d043ed689e105e43f3d` | Third run — operations anchor: release addendum (working layer, bound by hash) | `c08834a27df7f70d233da5da093a6043f127225ddda2a8e1e032727ce55b829b` |
| `ANCHOR-W16` | 2026-10-07 | 970302 (AntPool) | `23baece0c7d23479c7e7f7ee3ecbc8abfedbef885311df6eecc01534a477eb7f` | Third run — operations anchor: the pilot's close (working layer, bound by hash) | `6da0c44d37028f6c6e32838a8b0b423cee99af779f5162b01659f214b9584b01` |
| `ANCHOR-W17` | 2026-10-15 | 971556 (F2Pool) | `bef39e2d3e33932e5ffe9c5870c782256efe7db34d9f4272cfb42d56064ce945` | Third run — operations anchor: release addendum (working layer, bound by hash) | `02443453a88c34a610a29cba1cb88dd8084d5cb33ba68dbd2060acbd6ba7060f` |
| `ANCHOR-W18` | 2026-10-18 | 971960 (Foundry USA) | `285ecbba27926fb5508f9ddfc160a593c239976b668e02bb9d9ee10f77f5e373` | Third run — operations anchor: the tree of the first start (working layer, bound by hash) | `09a16334cf62901736c4ffdc61954353fe6a09b861729a51a08601d3b75553f9` |
| `ANCHOR-W19` | 2026-10-20 | 972306 (Foundry USA) | `fcd15b92cfcc04e4bff4045f51b47c48413807b6e351c27c02175120d84f4dec` | Third run — operations anchor: the stop of the first start (stop protocol, withheld) | `f6e49b6ddcf836862abd4bbc9adf4fb62558061958c413d97de55c84506e73c1` |

## The first versions and their homes

- *The Last Scarce Good*, V1.0 — canonical home and verification manifest (`ANCHOR-V1`, with
  `ANCHOR-ID1` and `ANCHOR-D1`): https://nullius2140.github.io/the-last-scarce-good/
- *The Second Nature*, V1.0 — canonical home and verification manifest (`ANCHOR-V2`):
  https://nullius2140.github.io/the-second-nature/
- *The Third Estate*, V1.0 — canonical home and verification manifest (`ANCHOR-V3`; annex
  `sources-and-influences.md`): https://nullius2140.github.io/the-third-estate/
- *The Key Question* — protocols, amendments, transcripts of both runs, reports, annexes,
  *Five Answers* V1.0 and its blind variant, the adjudication package, and the anchors
  `ANCHOR-P1` … `ANCHOR-N2`: https://github.com/Nullius2140/the-key-question

Each first version stays at its original home, unedited: the anchored V1.0 files are immutable,
their OpenTimestamps proofs stay beside them, and their manifests remain the sources of every
value copied here. This repository holds the revisions (V1.1), the reading test, and this
complete manifest. The chain is the version history: a reader who wants the first version
verifies it at its home against its own anchor; a reader who wants the revision verifies it here
against the anchors above. If a value in this file and a value in a source manifest ever differ,
the source manifest — and behind it the chain — is right, and the difference is an erratum of
this file.

## Note on this manifest

This file is the living outer layer of the verification architecture. The anchored artifacts are
immutable; this manifest is updated as anchors confirm (transaction, block height) and as
secondary attestations (OpenTimestamps) are published. The chain, not this file, is the
authority: every claim here is checkable against it. The anchors prove that each file existed in
exactly its current form no later than its block and that the whole series was executed by one
keyholder in the stated order; they do not prove that any text is true. An anchor is a timestamp,
not a theorem.
