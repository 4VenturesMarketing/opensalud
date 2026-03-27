import os

paths = [
    '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/index.html',
    '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/_opensalud_deploy_fix_5/index.html',
    '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/_opensalud_deploy_fix_5/landing_diagnostico_b2b.html'
]

old_text = "Descúbrelo con esta auditoría de <strong>bienestar emocional</strong> en <strong>menos de 3 minutos</strong>."
new_text = "Descúbrelo con este test de bienestar corporativo en <strong>menos de 3 minutos</strong>."

# Or accounting for different variations since I might have bolded things
# Target is replacing "auditoría de bienestar emocional" with "test de bienestar corporativo"

for p in paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Comprehensive replacement mapping
        text = text.replace('esta auditoría de <strong>bienestar emocional</strong>', 'este test de bienestar corporativo')
        text = text.replace('esta auditoría de bienestar emocional', 'este test de bienestar corporativo')
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated {p}")

