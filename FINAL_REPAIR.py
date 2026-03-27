import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Ensure "clima laboral de tu empresa" is bolded
text = text.replace('clima laboral de tu empresa', '<strong>clima laboral de tu empresa</strong>')
text = text.replace('<strong><strong>', '<strong>').replace('</strong></strong>', '</strong>')

# 2. Rename audit to test EXACTLY as requested
# Request: "Descúbrelo con esta auditoría de bienestar emocional en menos de 3 minutos." 
#    -> "Descúbrelo con este test de bienestar corporativo en menos de 3 minutos."
text = text.replace('esta auditoría de bienestar emocional', 'este test de bienestar corporativo')
text = text.replace('esta auditoría de <strong>bienestar emocional</strong>', 'este test de bienestar corporativo')
text = text.replace('con este test de bienestar corporativo en menos de 3 minutos', 'con este test de bienestar corporativo en <strong>menos de 3 minutos</strong>')

# 3. Repeat for the other files in subdirs
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

p2 = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/_opensalud_deploy_fix_5/index.html'
p3 = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/_opensalud_deploy_fix_5/landing_diagnostico_b2b.html'

for p in [p2, p3]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)

print("Final Repair Finished")
