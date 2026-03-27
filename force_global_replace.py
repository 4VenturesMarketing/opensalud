import os
import re

paths = [
    '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/index.html',
    '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/_opensalud_deploy_fix_5/index.html',
    '/Users/mfargas/Documents/4Ventures/00001-Atigravity/Opensalud/_opensalud_deploy_fix_5/landing_diagnostico_b2b.html'
]

for p in paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Replace if not already bolded
        # Avoiding nested strongs
        new_text = text.replace('clima laboral de tu empresa', '<strong>clima laboral de tu empresa</strong>')
        new_text = new_text.replace('<strong><strong>clima laboral de tu empresa</strong></strong>', '<strong>clima laboral de tu empresa</strong>')
        
        if text != new_text:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(new_text)
            print(f"Updated {p}")
        else:
            print(f"No changes for {p}")

