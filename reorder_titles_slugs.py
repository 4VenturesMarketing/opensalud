import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for Article titles inside cards
# Example: <h3 style="margin-top:0; color:var(--blue)">Artículo 1 — slug: <code>ley-riesgos-psicosociales-empresa</code></h3>
# want to transform to something like: Artículo 1 (Title from meta?) — slug: ...
# Actually, the user says "poner los títulos de los blogposts y después el slug".
# Let's extract the actual SEO title from the next line <h4>Meta title: ...

# Function to reorder
def reorder(match):
    full_h3 = match.group(0)
    art_num = match.group(1) # "Artículo 1"
    slug_code = match.group(2) # "<code>...</code>"
    
    # We need to find the meta title that follows this h3
    # It's usually in a <h4> right after it.
    # Searching for Meta Title after this position in the original text
    start_pos = match.start()
    meta_match = re.search(r'<h4.*?>Meta title: (.*?) \| opensalud</h4>', text[start_pos:start_pos+500])
    if meta_match:
        seo_title = meta_match.group(1).strip()
        # Sentence case check (only first letter of FIRST word upper)
        seo_title = seo_title[0].upper() + seo_title[1:].lower()
        return f'<h3 style="margin-top:0; color:var(--blue)">{art_num}: {seo_title} — slug: {slug_code}</h3>'
    else:
        return full_h3

# Regex for the current H3 structure
pattern = re.compile(r'<h3 style="margin-top:0; color:var(--blue)">(Artículo \d+) — slug: (<code>.*?</code>)</h3>')

new_text = pattern.sub(reorder, text)

# Let's do a manual check for one just in case regex didn't catch nuances
# Or just apply it if we are confident.

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Reordered article titles and slugs")
