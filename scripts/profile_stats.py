"""Draw the profile's GitHub statistics as SVG files in this repository (light and dark).

    GITHUB_TOKEN=... python scripts/profile_stats.py

Writes assets/{stats,activity,languages}-{light,dark}.svg from the GitHub GraphQL API. The images live in
the repository, so the profile never depends on an outside stats server; .github/workflows/profile-stats.yml
refreshes them daily. Counts cover the last 12 months and public, non-fork repositories.
"""
import datetime
import json
import os
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

USER = os.environ.get('PROFILE_USER', 'ishtiaq-ahmed-dev')
OUT = Path(__file__).resolve().parents[1] / 'assets'
FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
THEMES = {
    'light': dict(ink='#1f2328', ink2='#59636e', muted='#818b98', border='#d1d9e0', grid='#e7ecf0', bar='#2a78d6',
                  langs=['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#e87ba4', '#6250d6'], other='#c3c2b7', gap='#ffffff'),
    'dark': dict(ink='#f0f6fc', ink2='#9198a1', muted='#757d87', border='#3d444d', grid='#21262d', bar='#3987e5',
                 langs=['#3987e5', '#d95926', '#199e70', '#c98500', '#d55181', '#9085e9'], other='#56565c', gap='#0d1117'),
}
QUERY = """query($login: String!) { user(login: $login) {
  followers { totalCount }
  repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) { totalCount nodes {
    stargazerCount languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } } } }
  contributionsCollection { totalCommitContributions totalPullRequestContributions
    contributionCalendar { totalContributions weeks { firstDay contributionDays { contributionCount } } } } } }"""


def fetch():
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if not token:
        raise SystemExit('Set GITHUB_TOKEN (or GH_TOKEN) to read the GitHub API')
    body = json.dumps({'query': QUERY, 'variables': {'login': USER}}).encode()
    req = urllib.request.Request('https://api.github.com/graphql', body,
                                 {'Authorization': f'bearer {token}', 'User-Agent': 'profile-stats'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if data.get('errors'):
        raise SystemExit(f'GitHub API error: {data["errors"]}')
    return data['data']['user']


def card(w, h, th, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="{escape(title)}" font-family="{FONT}"><title>{escape(title)}</title>'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" fill="none" stroke="{th["border"]}"/>'
            f'<text x="24" y="34" font-size="15" font-weight="600" fill="{th["ink"]}">{escape(title)}</text>{body}</svg>')


def stats_svg(u, th):
    cc = u['contributionsCollection']
    tiles = [(cc['contributionCalendar']['totalContributions'], 'Contributions'), (cc['totalCommitContributions'], 'Commits'),
             (u['repositories']['totalCount'], 'Public repositories'),
             (sum(r['stargazerCount'] for r in u['repositories']['nodes']), 'Stars earned'), (u['followers']['totalCount'], 'Followers')]
    w, h, cell = 900, 132, (900 - 48) / len(tiles)
    body = ''.join(
        f'<text x="{24 + i * cell}" y="86" font-size="30" font-weight="600" fill="{th["ink"]}">{v:,}</text>'
        f'<text x="{24 + i * cell}" y="110" font-size="13" fill="{th["ink2"]}">{escape(label)}</text>'
        for i, (v, label) in enumerate(tiles))
    return card(w, h, th, body, 'GitHub activity, last 12 months')


def activity_svg(u, th):
    weeks = u['contributionsCollection']['contributionCalendar']['weeks']
    counts = [sum(d['contributionCount'] for d in wk['contributionDays']) for wk in weeks]
    w, h, x0, x1, y0, y1 = 900, 230, 56, 876, 190, 56
    top = max(4, max(counts))
    step = next(s for s in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500) if top / s <= 4)
    top = step * -(-top // step)
    bw = (x1 - x0) / len(counts)
    body = []
    for v in range(0, top + 1, step):
        y = y0 - (y0 - y1) * v / top
        body.append(f'<line x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}" stroke="{th["grid"] if v else th["border"]}"/>'
                    f'<text x="{x0 - 10}" y="{y + 4:.1f}" font-size="11" text-anchor="end" fill="{th["muted"]}">{v}</text>')
    seen = None
    for i, (wk, c) in enumerate(zip(weeks, counts)):
        x = x0 + i * bw
        if c:
            bh = max(2.0, (y0 - y1) * c / top)
            body.append(f'<rect x="{x + 1.5:.1f}" y="{y0 - bh:.1f}" width="{bw - 3:.1f}" height="{bh:.1f}" rx="2" fill="{th["bar"]}">'
                        f'<title>Week of {wk["firstDay"]}: {c} contributions</title></rect>')
        month = datetime.date.fromisoformat(wk['firstDay']).strftime('%b')
        if month != seen and i < len(weeks) - 2:
            seen = month
            body.append(f'<text x="{x + 1.5:.1f}" y="{y0 + 20}" font-size="11" fill="{th["muted"]}">{month}</text>')
    total = sum(counts)
    body.append(f'<text x="{w - 24}" y="34" font-size="13" text-anchor="end" fill="{th["ink2"]}">{total:,} contributions, by week</text>')
    return card(w, h, th, ''.join(body), 'Activity')


def languages_svg(u, th):
    sizes = {}
    for repo in u['repositories']['nodes']:
        for e in repo['languages']['edges']:
            sizes[e['node']['name']] = sizes.get(e['node']['name'], 0) + e['size']
    ranked = sorted(sizes.items(), key=lambda kv: -kv[1])
    top, rest = ranked[:5], sum(v for _, v in ranked[5:])
    parts = top + ([('Other', rest)] if rest >= 0.005 * sum(sizes.values()) else [])  # a sliver is not worth a legend entry
    total = sum(v for _, v in parts) or 1
    # colour follows the language, not its rank: languages keep their slot as the ranking changes
    order = ['Python', 'C++', 'HTML', 'JavaScript', 'TypeScript', 'CSS']
    colour = lambda name: th['other'] if name == 'Other' else th['langs'][order.index(name)] if name in order else th['other']
    w, h, x0, x1 = 900, 128, 24, 876
    body, x = [], x0
    for name, v in parts:
        seg = (x1 - x0) * v / total
        body.append(f'<rect x="{x:.1f}" y="52" width="{max(seg - 2, 1):.1f}" height="12" rx="3" fill="{colour(name)}"/>')
        x += seg
    lx = x0
    for name, v in parts:
        label = f'{name} {100 * v / total:.1f}%'
        body.append(f'<rect x="{lx}" y="86" width="10" height="10" rx="2" fill="{colour(name)}"/>'
                    f'<text x="{lx + 16}" y="95" font-size="13" fill="{th["ink2"]}">{escape(label)}</text>')
        lx += 22 + 7.2 * len(label)
    return card(w, h, th, ''.join(body), 'Languages in public repositories')


def main():
    u = fetch()
    OUT.mkdir(exist_ok=True)
    for mode, th in THEMES.items():
        for name, draw in (('stats', stats_svg), ('activity', activity_svg), ('languages', languages_svg)):
            (OUT / f'{name}-{mode}.svg').write_text(draw(u, th), encoding='utf-8')
    print('wrote', OUT)


if __name__ == '__main__':
    main()
