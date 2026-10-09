# luc4s.co

Lucas Botbol Agusti's personal site. One self-contained HTML page served as
static assets from Cloudflare.

```
public/
  index.html    the whole site: markup, CSS and JS inline, no external requests
  og.png        1200x630 share card
  favicon.svg   spiral and plane mark, the primary icon
  favicon.ico   16/32/48 fallback for older browsers
  apple-touch-icon.png
  llms.txt      guide file for agents, per the llms.txt v2 spec
  llms.md       full site content as markdown
  robots.txt
  sitemap.xml
  _headers      cache and security headers
  BingSiteAuth.xml  Bing Webmaster ownership proof, must stay at the root
tools/
  og-card.html  source for og.png
  favicon.py    generates favicon.svg
```

## Notes

**Everything is inline.** No external scripts, stylesheets, fonts or images, so
the page is a single request. The globe is SVG paths generated in JS, not an
image.

**The share card is generated, not hand-drawn.** `tools/og-card.html` embeds a
snapshot of the live globe SVG taken about three seconds into the opening
flight, when Buenos Aires and Austin are both visible. To regenerate, copy
`document.querySelector('#globe').outerHTML` from the running page into the
card in place of the existing `<svg id="globe">`, screenshot the `.og` element
at 1200x630 and save it to `public/og.png`.

**`llms.md` is the markdown twin of the page.** When the page copy changes,
update it, and `llms.txt` if a link or section changed. `index.html` points at
it with `rel="alternate"`, and at `llms.txt` with `rel="describedby"`.

**The full name is in the `h1`.** The wordmark `luc4s` is `aria-hidden`, and
"Lucas Botbol Agusti" sits under it as the accessible and indexable name. The
same name drives the `Person` JSON-LD block, whose `sameAs` links tie the site
to X, LinkedIn and Instagram.

**The favicon is generated.** `tools/favicon.py` plots an Archimedean spiral
and writes `public/favicon.svg`, reusing the plane glyph the globe uses. Render
the SVG at 512 on a `#0B1017` page so nothing bleeds into the rounded corners,
downscale, punch the rounded alpha mask at each size, and pack 16/32/48 into the
`.ico`. `apple-touch-icon.png` stays a full opaque square, since iOS applies its
own mask.

**Unknown paths return a real 404**, not a copy of the homepage, which search
engines treat as a soft 404 and a duplicate.

**Cache lifetimes live in `public/_headers`.** Icons and `og.png` get a week,
crawler files a day, and `index.html` revalidates every time so copy edits go
live immediately.

**The demos are built from real material.** SellWant's cards use a listing that
is actually on sellwant.com, and the wa-slack transcript is in Spanish because
the support team and its customers are.

**SellWant's wordmark is ported, not redrawn.** The glyphs were pulled out of
Geist Bold with fontTools as vector paths, so the mark needs no webfont, and it
reproduces the app's own reveal: "Sell" wipes down, "Want" wipes up 600ms later.
