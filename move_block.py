import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Define boundaries
# Block 10
match_b10 = re.search(r'(  <h2 id="articulos">10.*?)(</div>\n</section>)', text, flags=re.DOTALL)
if not match_b10:
    print("Could not find block 10")
    exit(1)

b10_content = match_b10.group(1)
end_of_file_content = match_b10.group(2) + text[match_b10.end():]

# Remove block 10 from original position
text = text[:match_b10.start()] + end_of_file_content

# Now find where to insert Block 10 (after Block 4 ends)

# We want to insert right before <h2 id="geo">6.
match_geo = re.search(r'(\n\s*<h2 id="geo">6\.)', text)
if not match_geo:
    print("Could not find block 6 to insert before")
    exit(1)

# Insert it
text = text[:match_geo.start()] + "\n\n" + b10_content + text[match_geo.start():]

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success")
