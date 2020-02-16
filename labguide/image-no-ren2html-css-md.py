import os, glob
from pathlib import Path
from shutil import copy2

module = Path(os.getcwd()).parent.name
url_dict = {}
stepnum_dict = {}
toc_steps_dict = {}

files = [file for file in glob.glob('*.png')]
files.sort(key=os.path.splitext)

for i,file in enumerate(files):
    new_fn = f'{module}_' + str(i).zfill(3) + '.png'
    url_dict[i] = f'https://onstakinc.github.io/cisco-tetration-hol/labguide/{module}/images/{new_fn}'
    stepnum = str(i).zfill(3)
    stepnum_dict[i] = f'{stepnum}'

os.chdir('..')

if os.path.exists('README.md'):
    print("Backing up README.md")
    copy2('README.md', 'README.bak.md') 
else:
    pass

with open('README.md','w') as f:
    f.write('# Cisco Tetration - Hands-On Lab\n')
    f.write('  \n')
    f.write(f'## {module.capitalize()}\n')
    f.write('  \n\n')
    f.write('#### Module Steps')
    f.write('  \n')

    for key in sorted(url_dict.keys()):
        toc_steps_dict[i] = f.write(f'###### <a href="#step-{stepnum_dict[key]}">Step {stepnum_dict[key]}</a>')
        f.write('  \n')

    f.write('\n\n')

    for key in sorted(url_dict.keys()):
        f.write(f'<div class="step" id="step-{stepnum_dict[key]}">')
        f.write(f'<a href="#step-{stepnum_dict[key]}">Step {stepnum_dict[key]}</a>')
        f.write(f'</div>')
        f.write(f'<a href="{url_dict[key]}"><img src="{url_dict[key]}" style="width:100%;height:100%;"></a>  \n')
        f.write('  \n\n')

    f.write('  \n')
    f.write('[Return to Table of Contents](https://onstakinc.github.io/cisco-tetration-hol/labguide/)')