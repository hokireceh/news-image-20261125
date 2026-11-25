# THE WORLD — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/hokireceh/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/hokireceh/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-image newspaper front page summing up 25 November 2026 in seven
stories: the war in Ukraine leads — 700,000 Russian troops killed — with
Iran's winter energy crisis, Iraq's move on Kurdish oilfields,
Indonesia's vice-president resigning, Real Madrid's 5–1 Champions League
rout of PSV, and a car bomb in Colombia below it.

## The image

`entry.png` is a 1024×1024 PNG drawn in pure typography — white paper,
black ink, dark-red accents — with a big serif masthead, a full-width lead
story, and six more stories in a two-column grid. No photos, no network
assets: every letter is rendered locally from the system Noto fonts.

## How it is made

`render.py` draws the front page with Pillow and saves `entry.png`:

```sh
python3 render.py
```

`main.ts` (Node, standard library only) copies `entry.png` into the
output directory for the bounty run:

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the [news-image-20261125 bounty](https://make.fun/bounty/news-image-20261125) on make.fun. Try make.fun yourself: https://make.fun/r/jjqnkn84
