# The control pool - strike list under V1.0 (R3.1, rule section 5)

Built 2026-11-19 by the chain bench (WR) for Table 4, under `r3-1-control-pool-rule-v1.0.md` (SHA-256 `2bb2350a7091c5ebd22638d7bb166fed7f3fdd48fafb643e5e0b10c9fc31d22a`), section 5. Counting as substring, as V1.0 reads. Numbers only; the rule decides.

Script `wr41_strikes.py`, SHA-256 `dcdb679f766bdc48cbf58446609e6aabf71cdb40afa0b066a6693aa144244215`; the same script, run in the other mode, builds the other list. Hashes of the extracted files in `SHA256SUMS-extracted.txt`.

## Sources

| File | URL | Fetched (UTC) | Bytes | Lines | Line ends | SHA-256 |
|---|---|---|---|---|---|---|
| `pg71.txt` | https://gutenberg.pglaf.org/cache/epub/71/pg71.txt | 2026-11-19T11:32:29Z | 72261 | 1221 | CRLF | `88310a64ab17a33347228deb109dc67f089c7313ef30e97d7870449612a77c98` |
| `pg1022.txt` | https://gutenberg.pglaf.org/cache/epub/1022/pg1022.txt | 2026-11-19T11:32:37Z | 89009 | 1531 | CRLF | `bb49dd34dac779d3198d944ae77691e1dba7ffbf663e994ed54db55ffa2a503f` |
| `pg2944.txt` | https://gutenberg.pglaf.org/cache/epub/2944/pg2944.txt | 2026-11-19T11:32:46Z | 439572 | 7242 | CRLF | `5d9d28c12da8bd9aaf3043e9a2d08fbd46116efd5a3736490a393599aef6d278` |
| `pg2945.txt` | https://gutenberg.pglaf.org/cache/epub/2945/pg2945.txt | 2026-11-19T11:33:01Z | 352850 | 5550 | CRLF | `2e7eb7281ade2ab623b9e4a790f79ed8e8b25dc1d95d31f9eda4f7a7dc471e6e` |
| `pg2940.txt` | https://gutenberg.pglaf.org/cache/epub/2940/pg2940.txt | 2026-11-19T11:33:13Z | 604771 | 10458 | CRLF | `cb59647c2f04ea4e9d60ac02af1aeed5b01e6f2945e8fb8027f60bcccae35fd6` |
| `pg26659.txt` | https://gutenberg.pglaf.org/cache/epub/26659/pg26659.txt | 2026-11-19T11:33:25Z | 623823 | 10600 | CRLF | `21b785e714b14c53cfd41fbe3c02186fcd8520d65c7b35f9a467a0abacd852f5` |
| `pg50189.txt` | https://gutenberg.pglaf.org/cache/epub/50189/pg50189.txt | 2026-11-19T11:33:46Z | 249355 | 4068 | CRLF | `3b9b1eb0455b0fe968a0f987aa279602216ae0aabe1560300177a1993e45a6e9` |
| `pg130.txt` | https://gutenberg.pglaf.org/cache/epub/130/pg130.txt | 2026-11-19T11:33:55Z | 382206 | 6226 | CRLF | `ec525c93afddb05465bf6fa0af8f873078b8e42a2a24f9b999582994f054fdf2` |
| `pg34901.txt` | https://gutenberg.pglaf.org/cache/epub/34901/pg34901.txt | 2026-11-19T11:34:10Z | 331030 | 5090 | CRLF | `9ecc51191d7ba36f99b0f17b2f60ed54c3929577856f47f0616d8f198422b657` |
| `pg24526.txt` | https://gutenberg.pglaf.org/cache/epub/24526/pg24526.txt | 2026-11-19T11:34:20Z | 961540 | 16118 | CRLF | `811ebda414dcefd9664c6b845d60aa773a9f91f7a74e3adb678c47041dc02bcd` |
| `pg77244.txt` | https://gutenberg.pglaf.org/cache/epub/77244/pg77244.txt | 2026-11-19T11:34:39Z | 997092 | 16310 | CRLF | `00352fc1f9d9df365a69cc9b466fee6f3e3998467083dbaeb28396734a091c31` |

Source: PG mirror (gutenberg.pglaf.org); gutenberg.org unreachable 17-19 November 2026 (HTTP 503, "Temporarily Down for Maintenance"); aleph.gutenberg.org, the first mirror tried, did not answer. The file `pg2944.txt` is byte-identical with the copy fetched from gutenberg.org on 16 November 2026 (`5d9d28c12da8bd9aaf3043e9a2d08fbd46116efd5a3736490a393599aef6d278`). Re-measurement at gutenberg.org on 19 November 2026, 12:35-12:36 UTC: HTTP 503 for all eleven files; the other ten are to be measured again when gutenberg.org answers, and if a hash differs, both hashes are published.

## The list

| No. | Ebook | Title as found | Found | First line | Last line | Lines | Bytes | Words | `money` | `coin` | `currenc` | `gold` | `wealth` | `propert` | `inherit` | `heir` | `bequea` | `bequest` | `legac` | `successor` | `machine` | `engine` | `automat` | `comput` | Max | (d) | (e) | Struck by | SHA-256 of extracted file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 71 | whole ebook | found | 28 | 870 | 843 | 52439 | 9354 | 8.55 | 0.00 | 0.00 | 0.00 | 0.00 | 11.76 | 0.00 | 55.59 | 0.00 | 0.00 | 0.00 | 0.00 | 9.62 | 1.07 | 0.00 | 1.07 | 55.59 | pass | fail | (e) | `03b86c037f856c9cc7fce825b26b2b6654c8ffae40a7fa231fda4759bf3992df` |
| P02 | 1022 | whole ebook | found | 28 | 1180 | 1153 | 69274 | 12114 | 0.83 | 0.83 | 0.00 | 2.48 | 0.83 | 1.65 | 1.65 | 45.40 | 0.00 | 0.00 | 0.00 | 0.00 | 0.83 | 0.83 | 0.00 | 0.00 | 45.40 | pass | fail | (e) | `a91f6e181004795859ea0fae7ecafdd743531542833813003d414f7f5b170af3` |
| P03 | 2944 | II. / SELF-RELIANCE | found | 824 | 1726 | 903 | 56768 | 10134 | 0.99 | 0.00 | 0.00 | 0.00 | 0.00 | 6.91 | 0.99 | 57.23 | 0.00 | 0.00 | 0.00 | 0.00 | 2.96 | 0.00 | 0.00 | 1.97 | 57.23 | pass | fail | (e) | `b0c7b2b74d4d5cf2ce802d9c2770308a1c31640678ce5d535c1e2189a6ac2137` |
| P04 | 2944 | IX. / THE OVER-SOUL | found | 4978 | 5596 | 619 | 39003 | 6885 | 1.45 | 0.00 | 0.00 | 0.00 | 4.36 | 2.90 | 0.00 | 47.93 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.45 | 47.93 | pass | fail | (e) | `4ee9bdd1ec577b9bfcfd465f4020948240da2b255d1e50f5b71ea70717c2f0d8` |
| P05 | 2945 | EXPERIENCE. | found | 833 | 1632 | 800 | 52243 | 9252 | 0.00 | 0.00 | 1.08 | 1.08 | 1.08 | 3.24 | 0.00 | 30.26 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.08 | 30.26 | pass | fail | (e) | `f9d6ae5e481705b6c7b92f83aa1838a9390e352ea906427d41920cf6d8975b7a` |
| P06 | 2945 | NATURE. | found | 3029 | 3573 | 545 | 35847 | 6231 | 0.00 | 0.00 | 0.00 | 0.00 | 4.81 | 3.21 | 0.00 | 28.89 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.60 | 0.00 | 0.00 | 28.89 | pass | fail | (e) | `362f44f14129b5dc288c08d1a253336057454e65fc934f3b212ea6ae23b4034e` |
| P07 | 2940 | EVOLUTION AND ETHICS. | found | 286 | 3148 | 2863 | 166494 | 27796 | 0.00 | 0.72 | 0.00 | 2.16 | 1.44 | 0.72 | 2.52 | 28.42 | 0.00 | 0.00 | 0.00 | 0.72 | 0.36 | 1.08 | 0.72 | 0.00 | 28.42 | fail | fail | (d) + (e) | `c2b048db759670031babeb49c3d22925161245c6382ba765e3da46b617fa2c25` |
| P08 | 2940 | SCIENCE AND MORALS | found | 3149 | 5516 | 2368 | 145821 | 23521 | 0.00 | 0.85 | 0.43 | 0.00 | 0.00 | 0.00 | 0.85 | 33.16 | 0.00 | 0.00 | 0.00 | 0.00 | 1.28 | 1.28 | 0.00 | 0.43 | 33.16 | fail | fail | (d) + (e) | `143c80ae53f1ecbbf65567948454c4bf1d8c39fb340fe93e04e228107e31f440` |
| P09 | 26659 | THE WILL TO BELIEVE.[1] | found | 454 | 1323 | 870 | 52663 | 9080 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.10 | 0.00 | 19.82 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 19.82 | pass | fail | (e) | `633f7d0d877644eb4ef99ec8c72e0febedcd7c0954c296c60b051b885d5d4e8b` |
| P10 | 26659 | IS LIFE WORTH LIVING?[1] | found | 1324 | 2242 | 919 | 53879 | 9218 | 1.08 | 0.00 | 1.08 | 0.00 | 1.08 | 2.17 | 0.00 | 37.97 | 0.00 | 0.00 | 0.00 | 1.08 | 1.08 | 0.00 | 0.00 | 0.00 | 37.97 | pass | fail | (e) | `cead78391491a2bcbd53194cef867fed8b464a40179d9bd495b8771dc1ddc3c0` |
| P11 | 26659 | THE DILEMMA OF DETERMINISM.[1] | found | 4592 | 5724 | 1133 | 69916 | 12014 | 0.83 | 0.83 | 0.83 | 0.00 | 0.00 | 1.66 | 0.00 | 27.47 | 0.00 | 0.00 | 0.00 | 0.00 | 0.83 | 0.00 | 0.00 | 0.00 | 27.47 | pass | fail | (e) | `465fb3c4b9cc10938594cd443eeee9365e5a97366dd9f5d24b0c557d63780b89` |
| P12 | 26659 | THE MORAL PHILOSOPHER AND THE MORAL LIFE.[1] | found | 5725 | 6594 | 870 | 54349 | 9198 | 1.09 | 0.00 | 0.00 | 0.00 | 0.00 | 1.09 | 0.00 | 27.18 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 27.18 | pass | fail | (e) | `06b9cead45169bc69ed9631f10ffc6e5e1456a844e9e36f24bab750ddc2a0429` |
| P13 | 50189 | - | not found: no heading block of this title after the contents list | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | not found | - |
| P14 | 50189 | - | not found: no heading block of this title after the contents list | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | not found | - |
| P15 | 130 | IV THE ETHICS OF ELFLAND | found | 1463 | 2229 | 767 | 47831 | 8516 | 0.00 | 1.17 | 2.35 | 4.70 | 0.00 | 0.00 | 0.00 | 19.96 | 0.00 | 0.00 | 1.17 | 0.00 | 3.52 | 0.00 | 1.17 | 0.00 | 19.96 | pass | fail | (e) | `91e9df4aecf8d8f0afa0dd9f398167868bdbe5d64dd6f0ad6ae3e3c52cd64b21` |
| P16 | 130 | VI THE PARADOXES OF CHRISTIANITY | found | 2819 | 3616 | 798 | 50128 | 8762 | 0.00 | 3.42 | 0.00 | 6.85 | 0.00 | 0.00 | 0.00 | 23.97 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 23.97 | pass | fail | (e) | `8f0d2a08b57f62146e2274dc08016f620cca2158945c4af16717a6b33ad88dea` |
| P17 | 34901 | OF THE LIBERTY OF THOUGHT AND DISCUSSION. | found | 1000 | 2468 | 1469 | 98416 | 16687 | 0.60 | 0.00 | 0.00 | 0.00 | 0.00 | 1.20 | 0.60 | 52.74 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.60 | 52.74 | fail | fail | (d) + (e) | `e000a87fa0a05cb01ea3d4e4aac281be3ff478e18d8cca5dadffa8c6ce27c750` |
| P18 | 34901 | OF INDIVIDUALITY, AS ONE OF THE ELEMENTS OF WELL-BEING. | found | 2469 | 3192 | 724 | 48433 | 8132 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.92 | 0.00 | 81.16 | 0.00 | 0.00 | 0.00 | 0.00 | 2.46 | 1.23 | 2.46 | 0.00 | 81.16 | pass | fail | (e) | `f2eb35aa91bce334c3011acb7ddf2344d27dd88eb908ef26d8d4d2cca47e75e1` |
| P19 | 24526 | Knowledge Its Own End. | found | 3256 | 3955 | 700 | 44187 | 7607 | 0.00 | 0.00 | 0.00 | 0.00 | 2.63 | 1.31 | 0.00 | 49.95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 49.95 | pass | fail | (e) | `4d9fbb2f6382ab4b96436e41667f4edb378d8d90939a5f12dbc779b706d7da5f` |
| P20 | 24526 | Knowledge Viewed In Relation To Professional Skill. | found | 4731 | 5537 | 807 | 51168 | 8839 | 1.13 | 0.00 | 0.00 | 1.13 | 4.53 | 1.13 | 1.13 | 47.52 | 0.00 | 0.00 | 0.00 | 0.00 | 1.13 | 3.39 | 0.00 | 0.00 | 47.52 | pass | fail | (e) | `1de47e02a68a8003b8560a7dcec7fd1d2097e5ff0b90e95bce3573db79bdd3fc` |
| P21 | 77244 | - | not found: no heading block of this title after the contents list | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | not found | - |
| P22 | 77244 | THE LITERARY INFLUENCE OF ACADEMIES. | found | 1312 | 2269 | 958 | 60920 | 10174 | 0.00 | 0.00 | 0.98 | 0.98 | 0.00 | 0.00 | 0.00 | 24.57 | 0.00 | 0.00 | 0.00 | 0.98 | 0.00 | 0.00 | 0.00 | 0.00 | 24.57 | pass | fail | (e) | `7c665be1cebe43ac463b61796b111ed11600a2b32eebb11eea25e09ec52d2abe` |

Note to P08: the ebook's own note, lines 3137-3145 of `pg2940.txt`: section III is Asa Gray's essay (1860), not Huxley's; struck by (d) under both lists.

Survivors: 0 of 22 (none). Fewer than three: rule section 8.

Counting: words = whitespace-separated tokens of the extracted file; each stem counted as a substring of the lower-cased text, per 10,000 words, two decimals; (e) fails above 5.00; (d) passes from 35,000 to 95,000 bytes.
