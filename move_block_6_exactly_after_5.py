import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Capture Block 6 and remove it
b6_pattern = re.compile(r'<section class="section-grey">\s*<div class="container">\s*<h2 id="geo">6\. Estrategia global seo & geo: opensalud \+ menttum</h2>.*?</div>\s*</section>', re.DOTALL)
b6_match = b6_pattern.search(text)
if not b6_match:
    print("B6 pattern not found in its new section")
    # Fallback to older pattern if previous script failed to update it fully
    b6_pattern = re.compile(r'<h2 id="geo">6\. Estrategia global seo & geo: opensalud \+ menttum</h2>.*?</div>', re.DOTALL)
    b6_match = b6_pattern.search(text)

if b6_match:
    b6_content = b6_match.group(0)
    text = text.replace(b6_content, "")
else:
    print("Could not find B6")
    exit(1)

# 2. Re-insert EXACTLY after Block 5 (which is formerly 10)
# Block 5 ends where the last card is (#art10).
# Let's find end of the list of 10 articles.
# Previous view_file showed them inside the section containing h2 id="articulos".
art10_end = text.find('</details>\n  </div>', text.find('id="art10"')) + 19

# Insert B6 right there, inside the SAME section as Block 5 for proximity
text_final = text[:art10_end] + "\n\n  " + b6_content + "\n\n" + text[art10_end:]

# Cleanup double sections created before
text_final = text_final.replace('<section class="section-grey">\n<div class="container">\n\n  <section class="section-grey">', '<section class="section-grey">')
text_final = text_final.replace('  </section>\n\n</div>\n</section>', '  </section>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text_final)

print("Success")
