import os, glob
from pathlib import Path

module = Path(os.getcwd()).parent.name
url_dict = {}

files = [file for file in glob.glob('*.png')]
files.sort(key=os.path.getmtime)

for i,file in enumerate(files):
    new_fn = str(i) + '.png'
    os.rename(file,new_fn)
    url_dict[i] = f'https://onstakinc.github.io/cisco-tetration-hol/labguide/{module}/images/{new_fn}'

os.chdir('..')

with open('README.md','w') as f:
    f.write('# Cisco Tetration - Hands-On Lab\n')
    f.write('  \n')
    f.write(f'## {module.capitalize()}\n')
    f.write('  \n')

    for key in sorted(url_dict.keys()):
        f.write(f'![Alt Text]({url_dict[key]})  \n')
        f.write('  \n')




