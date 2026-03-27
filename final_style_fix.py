import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix Heading 10 Format (should match others like <h2 id="contenidos">4. Plan...)
# Looking for <h2 id="articulos">10. Contenido...
# If it's outside a section container, wrap it and fix formatting
# Correct format is sentence-case and proper wrapper if needed.
text = re.sub(r'<h2 id="articulos">10\. Contenido de los 10 blogposts b2b</h2>', 
              r'<h2 id="articulos">10. Contenido de los 10 blogposts b2b</h2>', text)

# 2. Fix the broken footer/div structure
# We saw: </div>\n</section>\n\n<footer
# And then right after: <h2 id="articulos">10...
# This means section was closed before block 10.
# Let's Move block 10 inside the container if it's stuck near footer.

# Current state seems to be: 
# ...Block 4 ends...
# ...Block 10 starts...
# ...Footer? (Wait, I saw <footer near Block 10 in previous view_file)

# Let's find exactly where footer is.
footer_pos = text.find('<footer')
b10_pos = text.find('<h2 id="articulos">10.')

if b10_pos > footer_pos and footer_pos != -1:
    # Block 10 is AFTER footer, move it before.
    # Actually, let's just use a more robust regex to clean up the whole area.
    pass

# Strategy: 
# 1. Capture the entire Block 10 section.
# 2. Capture Step 4.
# 3. Clean up the messed up middle part.

# Find end of Step 4 (the card div)
match_step4_end = re.search(r'(<h2 id="contenidos">4\. Plan de contenidos b2b.*?</div>)', text, flags=re.DOTALL)
if not match_step4_end:
    print("Step 4 not found")
    exit(1)

# Find Block 10
match_b10 = re.search(r'(<h2 id="articulos">10\..*?)(?=<footer|</body>|</html>)', text, flags=re.DOTALL)
if not match_b10:
    print("Block 10 not found")
    exit(1)

b10_content = match_b10.group(1).strip()

# Cleanup everything between end of step 4 and start of step 6/rest of doc
# Or just ensure Block 10 is inserted right after Step 4.

# Remove Block 10 from its current position
text = text.replace(match_b10.group(0), "")

# Re-insert Block 10 right after Step 4
insertion_point = match_step4_end.end()
text = text[:insertion_point] + "\n\n  " + b10_content + "\n" + text[insertion_point:]

# 3. Fix the "desconfigurado" style - likely missing the .container wrapper or being inside a broken div.
# Make sure Block 10 is inside the <section><div class="container">...
# Check if it has a broken footer before it
text = text.replace('<footer', '  </div>\n</section>\n\n<footer>')
# Remove any duplicate section closing that might have been created
text = re.sub(r'</div>\s*</section>\s*</div>\s*</section>', r'</div>\s*</section>', text)

# Ensure one single consistent container
# First, remove all stray footers/sections in the middle
text = re.sub(r'</div>\s*</section>\s*<footer.*?>.*?</footer>\s*', '', text, flags=re.DOTALL)
# Re-add footer at the very end
text = text.strip()
if not text.endswith('</html>'):
    text += '\n\n<footer>\n  <p>© 2026 4Ventures · Informe Analítico de Posicionamiento</p>\n</footer>\n</body>\n</html>'

# Final check: sentence case for Title 10
text = text.replace('10. Contenido de los 10 blogposts b2b', '10. Contenido de los 10 blogposts b2b')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success")
