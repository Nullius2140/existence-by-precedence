#!/usr/bin/env python3
"""WR-35/WR-40/WR-41 - strike lists of the control pool (rule r3-1-control-pool-rule-v1.0.md, sha256 2bb2350a...d22a,
section 5; addendum 1, its hash read from the file, section 3 (e)).

Usage: python3 -I wr41_strikes.py <sources-dir> <out-dir> <list-date> <mode> <gutenberg-org-status> <addendum-file>
  <mode>: substring (as V1.0 reads) or wordstart (addendum 1: a stem counts where it begins a word, i.e. a
  maximal run of letters [a-z]+ in the lower-cased text);
  <gutenberg-org-status>: one sentence on the re-measurement of the sources at gutenberg.org, written into the head;
  <addendum-file>: r3-1-control-pool-rule-v1.0-addendum-1.md; its SHA-256 is read from the file and named in the head
  of the addendum list;
  <sources-dir>: holds pg<N>.txt and abruf.tsv (the fetch log); <out-dir>: must not exist.
Deterministic: no clock, no network. Every path written into the outputs is relative.

Extraction follows the rule's section 2 literally:
  - whole ebook (P01, P02): first line after the start marker to the line before the end marker;
  - collection: a heading is a title line (the title as in the collection's contents, with or without a number,
    capitalisation/punctuation/footnote marks as found), plus a line carrying only a number directly above it,
    the block standing alone (blank line before its first and after its last line), after the collection's own
    contents list; the text runs from the first line of its first heading to the line before the first line of
    the first subsequent heading of a different text of the same collection.
Matching of a line against a title (the builder's reading, declared in the list): case-insensitive; leading
number token (roman or arabic, optional period) removed; footnote marks [n] removed;
diacritics folded; every character other than a letter or a digit read as one space (punctuation as found);
runs of spaces as one.
"""
import sys, os, re, hashlib, unicodedata

RULE_SHA = '2bb2350a7091c5ebd22638d7bb166fed7f3fdd48fafb643e5e0b10c9fc31d22a'
STEMS = ['money', 'coin', 'currenc', 'gold', 'wealth', 'propert', 'inherit', 'heir', 'bequea', 'bequest',
         'legac', 'successor', 'machine', 'engine', 'automat', 'comput']
D_MIN, D_MAX, E_MAX = 35000, 95000, 5.00

# Collections: titles in the order of the collection's own contents (as listed there, page numbers and
# bracketed years dropped); contents = (first line, last line) of the contents list in the source file,
# 1-based, as found by the builder; None = the file carries no contents list.
COLL = {
    2944: dict(contents=(37, 50), titles=['History', 'Self-Reliance', 'Compensation', 'Spiritual Laws', 'Love',
               'Friendship', 'Prudence', 'Heroism', 'The Over-Soul', 'Circles', 'Intellect', 'Art']),
    2945: dict(contents=None, titles=['The Poet', 'Experience', 'Character', 'Manners', 'Gifts', 'Nature',
               'Politics', 'Nominalist and Realist', 'New England Reformers']),
    2940: dict(contents=(249, 276), titles=['Evolution and Ethics. Prolegomena', 'Evolution and Ethics',
               'Science and Morals', 'Capital--the Mother of Labour', 'Social Diseases and Worse Remedies']),
    26659: dict(contents=(317, 440), titles=['The Will to Believe', 'Is Life Worth Living', 'The Sentiment of Rationality',
               'Reflex Action and Theism', 'The Dilemma of Determinism', 'The Moral Philosopher and the Moral Life',
               'Great Men and their Environment', 'The Importance of Individuals', 'On some Hegelisms',
               'What Psychical Research has Accomplished']),
    50189: dict(contents=(3651, 3659), titles=['The Scientific Basis of Morals', 'Right and Wrong', 'The Ethics of Belief',
               'The Ethics of Religion']),
    130: dict(contents=(74, 85), titles=['Introduction in Defence of Everything Else', 'The Maniac', 'The Suicide of Thought',
               'The Ethics of Elfland', 'The Flag of the World', 'The Paradoxes of Christianity', 'The Eternal Revolution',
               'The Romance of Orthodoxy', 'Authority and the Adventurer']),
    34901: dict(contents=(442, 469), titles=['Introductory', 'Of the Liberty of Thought and Discussion',
               'Of Individuality, as One of the Elements of Well-Being',
               'Of the Limits to the Authority of Society over the Individual', 'Applications']),
    24526: dict(contents=(41, 73), titles=['Introductory', 'Theology A Branch Of Knowledge',
               'Bearing Of Theology On Other Branches Of Knowledge', 'Bearing Of Other Branches Of Knowledge On Theology',
               'Knowledge Its Own End', 'Knowledge Viewed In Relation To Learning',
               'Knowledge Viewed In Relation To Professional Skill', 'Knowledge Viewed In Relation To Religion',
               'Duties Of The Church Towards Knowledge']),
    77244: dict(contents=(265, 305), titles=['The Function of Criticism at the Present Time', 'The Literary Influence of Academies',
               'Maurice de Guerin', 'Eugenie de Guerin', 'Heinrich Heine', 'Pagan and Mediaeval Religious Sentiment',
               'A Persian Passion Play', 'Joubert', 'Spinoza and the Bible', 'Marcus Aurelius', 'The Study of Poetry', 'Milton',
               'Thomas Gray', 'John Keats', 'Wordsworth', 'Byron', 'Shelley', 'Count Leo Tolstoi', 'Amiel']),
}

# Pool, rule section 4: (No., ebook, title in the pool's wording, title used for matching or None = whole ebook, slug)
POOL = [
    ('P01', 71, 'On the Duty of Civil Disobedience (whole ebook)', None, 'civil-disobedience'),
    ('P02', 1022, 'Walking (whole ebook)', None, 'walking'),
    ('P03', 2944, 'Self-reliance (Essays - First Series)', 'Self-Reliance', 'self-reliance'),
    ('P04', 2944, 'The over-soul (Essays - First Series)', 'The Over-Soul', 'the-over-soul'),
    ('P05', 2945, 'Experience (Essays - Second Series)', 'Experience', 'experience'),
    ('P06', 2945, 'Nature (Essays - Second Series)', 'Nature', 'nature'),
    ('P07', 2940, 'Evolution and Ethics', 'Evolution and Ethics', 'evolution-and-ethics'),
    ('P08', 2940, 'Science and Morals', 'Science and Morals', 'science-and-morals'),
    ('P09', 26659, 'The Will to Believe', 'The Will to Believe', 'the-will-to-believe'),
    ('P10', 26659, 'Is Life Worth Living?', 'Is Life Worth Living', 'is-life-worth-living'),
    ('P11', 26659, 'The Dilemma of Determinism', 'The Dilemma of Determinism', 'the-dilemma-of-determinism'),
    ('P12', 26659, 'The Moral Philosopher and the Moral Life', 'The Moral Philosopher and the Moral Life', 'the-moral-philosopher'),
    ('P13', 50189, 'On the Scientific Basis of Morals', 'The Scientific Basis of Morals', 'scientific-basis-of-morals'),
    ('P14', 50189, 'The Ethics of Belief', 'The Ethics of Belief', 'the-ethics-of-belief'),
    ('P15', 130, 'The Ethics of Elfland (Orthodoxy, ch. IV)', 'The Ethics of Elfland', 'the-ethics-of-elfland'),
    ('P16', 130, 'The Paradoxes of Christianity (Orthodoxy, ch. VI)', 'The Paradoxes of Christianity', 'the-paradoxes-of-christianity'),
    ('P17', 34901, 'Of the Liberty of Thought and Discussion (On Liberty, ch. II)', 'Of the Liberty of Thought and Discussion', 'liberty-of-thought'),
    ('P18', 34901, 'Of Individuality, as One of the Elements of Well-Being (On Liberty, ch. III)', 'Of Individuality, as One of the Elements of Well-Being', 'of-individuality'),
    ('P19', 24526, 'Discourse V. Knowledge Its Own End', 'Knowledge Its Own End', 'knowledge-its-own-end'),
    ('P20', 24526, 'Discourse VII. Knowledge Viewed in Relation to Professional Skill', 'Knowledge Viewed In Relation To Professional Skill', 'knowledge-and-professional-skill'),
    ('P21', 77244, 'The Function of Criticism at the Present Time', 'The Function of Criticism at the Present Time', 'function-of-criticism'),
    ('P22', 77244, 'The Literary Influence of Academies', 'The Literary Influence of Academies', 'influence-of-academies'),
]

NUM = re.compile(r'^\s*([IVXLCDM]+|\d+)\.?\s*$')

def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('Æ', 'AE').replace('æ', 'ae')
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'\[\d+\]', '', s)
    s = s.strip()
    s = re.sub(r'^([IVXLCDM]+|\d+)\.?\s+', '', s)
    s = re.sub(r'[^0-9A-Za-z]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip().lower()

def load(path):
    raw = open(path, 'rb').read()
    lines = raw.decode('utf-8').split('\n')          # each line keeps its '\r' if CRLF
    vis = [l.rstrip('\r') for l in lines]
    st = next(i for i, l in enumerate(vis) if l.startswith('*** START OF THE PROJECT GUTENBERG EBOOK'))
    en = next(i for i, l in enumerate(vis) if l.startswith('*** END OF THE PROJECT GUTENBERG EBOOK'))
    return raw, lines, vis, st, en

def headings(vis, st, en, coll):
    """All heading blocks of the collection: list of (first_line_idx, title_line_idx, title)."""
    tmap = {norm(t): t for t in coll['titles']}
    after = coll['contents'][1] - 1 if coll['contents'] else st   # 0-based index of the last contents line
    blank = lambda k: vis[k].strip() == ''
    out = []
    for k in range(after + 1, en):
        t = tmap.get(norm(vis[k]))
        if not t:
            continue
        first = k - 1 if NUM.match(vis[k - 1]) else k
        if blank(first - 1) and blank(k + 1):
            out.append((first, k, t))
    return out

def extract(lines, vis, st, en, ebook, mtitle):
    if mtitle is None:
        return st + 1, en - 1, 'whole ebook', None
    coll = COLL[ebook]
    H = headings(vis, st, en, coll)
    mine = [h for h in H if h[2] == mtitle]
    if not mine:
        return None, None, None, 'no heading block of this title after the contents list'
    f0, k0, _ = mine[0]
    nxt = [h for h in H if h[0] > f0 and h[2] != mtitle]
    if nxt:
        last = nxt[0][0] - 1
    else:
        return None, None, None, 'last text of the collection - not in the pool'
    form = vis[k0].strip() if f0 == k0 else vis[f0].strip() + ' / ' + vis[k0].strip()
    return f0, last, form, None

def measure(data, mode):
    text = data.decode('utf-8')
    words = len(text.split())
    low = text.lower()
    if mode == 'substring':
        counts = {s: low.count(s) for s in STEMS}
    else:
        toks = re.findall(r'[a-z]+', low)
        counts = {s: sum(1 for w in toks if w.startswith(s)) for s in STEMS}
    per = {s: round(counts[s] * 10000 / words, 2) if words else 0.0 for s in STEMS}
    return words, counts, per

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    src, out, date, mode, gstatus = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    ADD_SHA = sha(open(sys.argv[6], 'rb').read())
    if mode not in ('substring', 'wordstart'):
        sys.exit('mode must be substring or wordstart')
    if os.path.exists(out):
        sys.exit('out-dir exists: ' + out)
    os.makedirs(os.path.join(out, 'extracted'))
    log = {}
    for row in open(os.path.join(src, 'abruf.tsv'), encoding='utf-8').read().strip().split('\n')[1:]:
        f = row.split('\t'); log[f[0]] = f
    script_sha = sha(open(os.path.abspath(__file__), 'rb').read())
    books = {}
    for n in sorted({p[1] for p in POOL}, key=lambda n: [p[1] for p in POOL].index(n)):
        books[n] = load(os.path.join(src, f'pg{n}.txt'))
        if sha(books[n][0]) != log[f'pg{n}.txt'][7]:
            sys.exit(f'source hash differs from fetch log: pg{n}.txt')
    rows, sums = [], []
    for no, n, ptitle, mtitle, slug in POOL:
        raw, lines, vis, st, en = books[n]
        a, b, form, why = extract(lines, vis, st, en, n, mtitle)
        if a is None:
            rows.append(dict(no=no, n=n, form='-', found='not found: ' + why, a='-', b='-', nl='-', by='-', w='-',
                             per={s: '-' for s in STEMS}, mx='-', d='-', e='-', struck='not found', sha='-'))
            continue
        data = '\n'.join(lines[a:b + 1]).encode('utf-8') + b'\n'
        name = f'{no}-{n}-{slug}.txt'
        open(os.path.join(out, 'extracted', name), 'wb').write(data)
        words, counts, per = measure(data, mode)
        mx = max(per.values())
        d_ok = D_MIN <= len(data) <= D_MAX
        e_ok = mx <= E_MAX
        struck = '-' if (d_ok and e_ok) else ' + '.join(x for x, ok in (('(d)', d_ok), ('(e)', e_ok)) if not ok)
        h = sha(data); sums.append(f'{h}  extracted/{name}')
        rows.append(dict(no=no, n=n, form=form, found='found', a=a + 1, b=b + 1, nl=b - a + 1, by=len(data), w=words,
                         per=per, mx=mx, d='pass' if d_ok else 'fail', e='pass' if e_ok else 'fail', struck=struck, sha=h))
    surv = [r['no'] for r in rows if r['struck'] == '-']
    L = []
    if mode == 'substring':
        L.append('# The control pool - strike list under V1.0 (R3.1, rule section 5)')
        L.append('')
        L.append(f'Built {date} by the chain bench (WR) for Table 4, under `r3-1-control-pool-rule-v1.0.md` '
                 f'(SHA-256 `{RULE_SHA}`), section 5. Counting as substring, as V1.0 reads. Numbers only; the rule decides.')
    else:
        L.append('# The control pool - strike list under addendum 1 (R3.1, rule section 5)')
        L.append('')
        L.append(f'Built {date} by the chain bench (WR) for Table 4, under `r3-1-control-pool-rule-v1.0.md` '
                 f'(SHA-256 `{RULE_SHA}`), section 5, as amended by `r3-1-control-pool-rule-v1.0-addendum-1.md` '
                 f'(SHA-256 `{ADD_SHA}`): stem at word start. Numbers only; the rule decides.')
    L.append('')
    L.append(f'Script `wr41_strikes.py`, SHA-256 `{script_sha}`; the same script, run in the other mode, '
             f'builds the other list. Hashes of the extracted files in `SHA256SUMS-extracted.txt`.')
    L.append('')
    L.append('## Sources')
    L.append('')
    L.append('| File | URL | Fetched (UTC) | Bytes | Lines | Line ends | SHA-256 |')
    L.append('|---|---|---|---|---|---|---|')
    for n in books:
        f = log[f'pg{n}.txt']
        le = 'CRLF' if f[6] == f[5] else ('LF' if f[6] == '0' else 'mixed')
        L.append(f'| `pg{n}.txt` | {f[1]} | {f[2]} | {f[4]} | {f[5]} | {le} | `{f[7]}` |')
    L.append('')
    L.append('Source: PG mirror (gutenberg.pglaf.org); gutenberg.org unreachable 17-19 November 2026 (HTTP 503, '
             '"Temporarily Down for Maintenance"); aleph.gutenberg.org, the first mirror tried, did not answer. '
             'The file `pg2944.txt` is byte-identical with the copy fetched from gutenberg.org on 16 November 2026 '
             '(`5d9d28c12da8bd9aaf3043e9a2d08fbd46116efd5a3736490a393599aef6d278`). ' + gstatus)
    L.append('')
    L.append('## The list')
    L.append('')
    hdr = ['No.', 'Ebook', 'Title as found', 'Found', 'First line', 'Last line', 'Lines', 'Bytes', 'Words'] + \
          [f'`{s}`' for s in STEMS] + ['Max', '(d)', '(e)', 'Struck by', 'SHA-256 of extracted file']
    L.append('| ' + ' | '.join(hdr) + ' |')
    L.append('|' + '---|' * len(hdr))
    for r in rows:
        per = [f'{r["per"][s]:.2f}' if isinstance(r['per'][s], float) else r['per'][s] for s in STEMS]
        mx = f'{r["mx"]:.2f}' if isinstance(r['mx'], float) else r['mx']
        sh = f'`{r["sha"]}`' if r['sha'] != '-' else '-'
        L.append('| ' + ' | '.join([r['no'], str(r['n']), r['form'], r['found'], str(r['a']), str(r['b']), str(r['nl']),
                                    str(r['by']), str(r['w'])] + per + [mx, r['d'], r['e'], r['struck'], sh]) + ' |')
    L.append('')
    L.append('Note to P08: the ebook\'s own note, lines 3137-3145 of `pg2940.txt`: section III is Asa Gray\'s essay (1860), '
             'not Huxley\'s; struck by (d) under both lists.')
    L.append('')
    L.append(f'Survivors: {len(surv)} of 22 ({", ".join(surv) if surv else "none"}).'
             + ('' if len(surv) >= 3 else ' Fewer than three: rule section 8.'))
    L.append('')
    how = ('each stem counted as a substring of the lower-cased text' if mode == 'substring' else
           'each stem counted as the number of maximal letter runs [a-z]+ of the lower-cased text that begin with it')
    L.append('Counting: words = whitespace-separated tokens of the extracted file; ' + how +
             ', per 10,000 words, two decimals; (e) fails above 5.00; (d) passes from 35,000 to 95,000 bytes.')
    L.append('')
    lname = 'r3-1-control-pool-strikes-v1.0.md' if mode == 'substring' else 'r3-1-control-pool-strikes-addendum-1.md'
    open(os.path.join(out, lname), 'w', encoding='utf-8').write('\n'.join(L))
    open(os.path.join(out, 'SHA256SUMS-extracted.txt'), 'w', encoding='utf-8').write('\n'.join(sums) + '\n')
    src_sums = [f'{log[f"pg{n}.txt"][7]}  sources/pg{n}.txt' for n in books]
    open(os.path.join(out, 'SHA256SUMS-sources.txt'), 'w', encoding='utf-8').write('\n'.join(src_sums) + '\n')

if __name__ == '__main__':
    main()
