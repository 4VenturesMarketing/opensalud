import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Capture Block 6 content and remove it
b6_marker = '<h2 id="geo">6. Estrategia global seo & geo: opensalud + menttum</h2>'
b6_start = text.find(b6_marker)
if b6_start == -1:
    print("B6 start not found")
    exit(1)

# Find natural end of B6 (usually next h2 or section close)
b6_end = text.find('<h2', b6_start + 10)
if b6_end == -1:
    b6_end = text.find('</div>\n</section>', b6_start)

b6_content = text[b6_start:b6_end].strip()

# New text without B6
text_no_6 = text[:b6_start] + text[b6_end:]

# 2. Re-insert AFTER the current section ends to make it a NEW section (design-wise "outside")
# Since the previous design might have had several blocks inside one <section><div class="container">...
# we will close the current one, add a small gap, and open a NEW one for Block 6.

# Let's find where the blogposts end (Art 10)
art10_end_marker = 'id="art10"'
art10_pos = text_no_6.find(art10_end_marker)
if art10_pos == -1:
    print("Art 10 not found")
    exit(1)

# Find the CLOSING of that card div and then the CONTAINER/SECTION closing
# We want to insert it after the current section closes.
# CURRENT STRUCTURE: <section><div class="container">...Cards...[WANT TO INSERT HERE]...
section_close_pos = text_no_6.find('</div>\n</section>', art10_pos)

# IF no section close is found near it, it might be later. Let's look for first one after art10.
if section_close_pos == -1:
    section_close_pos = text_no_6.find('</div>', art10_pos) + 6 # Fallback

# Actually, to make it completely "outside" at design level, we close section, and start a new section.
new_section_b6 = f'''
</div>
</section>

<section class="section-grey">
<div class="container">
  {b6_content}
</div>
</section>

<section>
<div class="container">
'''

# Replace the closing tag area with the new block
text_final = text_no_6[:section_close_pos] + new_section_b6 + text_no_6[section_close_pos+17:]

# Final cleanup to avoid triple-closing or empty containers
text_final = text_final.replace('<section>\n<div class="container">\n\n</div>\n</section>', '')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text_final)

print("Success")
