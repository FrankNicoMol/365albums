from collections import Counter
from pathlib import Path


def _top_genres(df, n=5):
    counts = Counter()
    for g in df['genres'].dropna():
        for tag in g.split(','):
            tag = tag.strip()
            if tag and tag != 'unknown':
                counts[tag] += 1
    return [genre.title() for genre, _ in counts.most_common(n)]


def build_page(df, img_path: Path, output_path: Path):
    albums = len(df)
    total_min = int(df['duration_min'].sum())
    remaining = max(0, 365 - albums)
    progress_pct = round(albums / 365 * 100, 1)
    genres = _top_genres(df)

    img_rel = img_path.relative_to(output_path.parent)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>365 Albums — 2026</title>
  <style>
    *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      background: #08080f;
      color: #ddddf0;
      font-family: system-ui, -apple-system, sans-serif;
      font-weight: 300;
    }}

    .hero {{
      width: 100%;
      max-height: 75vh;
      object-fit: cover;
      display: block;
    }}

    .content {{
      max-width: 600px;
      margin: 0 auto;
      padding: 4rem 2rem 6rem;
    }}

    .eyebrow {{
      font-size: 0.7rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: #6b6b88;
      margin-bottom: 1rem;
    }}

    .mission {{
      font-size: 2.4rem;
      font-weight: 200;
      line-height: 1.25;
      margin-bottom: 3.5rem;
      color: #f0f0ff;
    }}

    .divider {{
      border: none;
      border-top: 1px solid #1a1a2e;
      margin: 2.5rem 0;
    }}

    .stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }}

    .stat-value {{
      font-size: 2.6rem;
      font-weight: 200;
      color: #b47fe8;
      line-height: 1;
    }}

    .stat-label {{
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #55556a;
      margin-top: 0.4rem;
    }}

    .section-label {{
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #55556a;
      margin-bottom: 1rem;
    }}

    .tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .tag {{
      padding: 0.3rem 0.8rem;
      border: 1px solid #2a1a4a;
      font-size: 0.8rem;
      color: #9d6ed6;
      letter-spacing: 0.05em;
    }}

    .progress-row {{
      display: flex;
      justify-content: space-between;
      font-size: 0.65rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #55556a;
      margin-bottom: 0.75rem;
    }}

    .bar-track {{
      height: 1px;
      background: #1a1a2e;
    }}

    .bar-fill {{
      height: 1px;
      background: linear-gradient(90deg, #7c3aed, #d4622a);
      width: {progress_pct}%;
    }}
  </style>
</head>
<body>

  <img class="hero" src="{img_rel}" alt="365 Albums 2026">

  <div class="content">

    <p class="eyebrow">New Year's Resolution — 2026</p>
    <p class="mission">Listen to<br>365 albums.</p>

    <div class="stats">
      <div>
        <div class="stat-value">{albums}</div>
        <div class="stat-label">Albums listened</div>
      </div>
      <div>
        <div class="stat-value">{total_min:,}</div>
        <div class="stat-label">Minutes</div>
      </div>
      <div>
        <div class="stat-value">{remaining}</div>
        <div class="stat-label">To go</div>
      </div>
    </div>

    <hr class="divider">

    <p class="section-label">Top genres</p>
    <div class="tags">
      {"".join(f'<span class="tag">{g}</span>' for g in genres)}
    </div>

    <hr class="divider">

    <div class="progress-row">
      <span>Progress</span>
      <span>{albums} / 365</span>
    </div>
    <div class="bar-track">
      <div class="bar-fill"></div>
    </div>

  </div>
</body>
</html>"""

    output_path.write_text(html, encoding='utf-8')
