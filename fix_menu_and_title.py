import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the Navigation Menu based on current page blocks
# Current blocks: 0. intro, 1. salud, 2. hallazgos, 3. onpage, 4. contenidos, 5. articulos (will rename), 6. geo, 7. ctas, 8. elite, 9. roadmap
# Let's find the nav section
nav_pattern = re.compile(r'<ul class="nav-links">.*?</ul>', re.DOTALL)
new_nav = '''<ul class="nav-links">
    <li><a href="#intro">0. Intro</a></li>
    <li><a href="#salud">1. Salud SEO</a></li>
    <li><a href="#hallazgos">2. Hallazgos</a></li>
    <li><a href="#onpage">3. On-Page B2B</a></li>
    <li><a href="#contenidos">4. Plan B2B</a></li>
    <li><a href="#articulos">5. Blogposts</a></li>
    <li><a href="#geo">6. SEO & GEO</a></li>
    <li><a href="#ctas">7. CTAs</a></li>
    <li><a href="#elite">8. PSEO</a></li>
    <li><a href="#roadmap">9. Roadmap</a></li>
  </ul>'''

text = nav_pattern.sub(new_nav, text)

# 2. Rename Block 10 to Block 5 in the content
text = text.replace('<h2 id="articulos">10. Contenido de los 10 blogposts b2b</h2>', 
                    '<h2 id="articulos">5. Contenido de los 10 blogposts b2b</h2>')

# 3. Fix the "desconfigurado" blogposts
# They seem to be inside Step 4's section/container or stuck between tags.
# Let's ensure a clean structure:
# Close Step 4's container correctly before Step 5 starts.

# Find where Step 5 (formerly 10) starts
b5_marker = '<h2 id="articulos">5. Contenido'
b5_pos = text.find(b5_marker)

# Find where Step 4 ends (it has a <div class="card">...</table></div>)
step4_start = text.find('<h2 id="contenidos">4. Plan')
step4_card_end = text.find('</div>', step4_start + 100) + 6

# We want to ensure there is NO closing of main container between Step 4 and Step 5,
# OR that both are inside the SAME container.
# Currently they are likely following each other in the text.

# Let's make sure they are both wrapped in <div class="container"> if they aren't.
# The previous script might have messed up the </div> tags.

# Remove any stray "</div>\n</section>" between 4 and 5
middle_part = text[step4_card_end:b5_pos]
cleansed_middle = re.sub(r'</div>\s*</section>\s*<section>\s*<div class="container">', '', middle_part)
text = text[:step4_card_end] + cleansed_middle + text[b5_pos:]

# Final touch: ensure the whole page is wrapped in ONE section/container for simplicity if it's broken
# Or just fix the immediate mess.

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success")
