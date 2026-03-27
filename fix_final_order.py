import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Re-calculate markers for movement
# Find Step 4
start_step4 = text.find('<h2 id="contenidos">4. Plan de contenidos b2b')
if start_step4 == -1:
    print("Step 4 not found")
    exit(1)

# Find end of Step 4 (next h2)
next_h2_after_4 = text.find('<h2', start_step4 + 10)
if next_h2_after_4 == -1:
    print("Next h2 after step 4 not found")
    exit(1)

# Find Step 10
start_step10 = text.find('<h2 id="articulos">10. Contenido de los 10 blogposts b2b')
if start_step10 == -1:
    print("Step 10 not found")
    exit(1)

# Find end of Step 10 (footer or end of section)
# Usually before </div>\n</section>
end_of_step10 = text.find('</div>\n</section>', start_step10)
if end_of_step10 == -1:
    print("End of step 10 not found")
    exit(1)

# Extract contents
step10_content = text[start_step10:end_of_step10].strip()

# Create content without Step 10
text_no_10 = text[:start_step10] + text[end_of_step10:]

# Re-locate the insertion point in the new text
# We want to insert it after Step 4 ends and BEFORE Step 6 or whatever follows Step 4
# Since we removed Step 10, let's find the insertion point again
insert_marker = text_no_10.find('<h2', start_step4 + 10)

text_final = text_no_10[:insert_marker] + "\n\n  " + step10_content + "\n\n" + text_no_10[insert_marker:]

# --- Fix the duplicate <div class="grid-2"> while we are at it ---
text_final = text_final.replace('<div class="grid-2">\n    <div class="grid-2">', '<div class="grid-2">')
text_final = text_final.replace('<div class="grid-2">\n  <div class="grid-2">', '<div class="grid-2">')
# Close them correctly
text_final = text_final.replace('    </div>\n    </div>\n  </div>', '    </div>\n  </div>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text_final)

print("Success")
