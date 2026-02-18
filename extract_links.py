import re
import os
import glob

pdf_files = glob.glob(r'e:\Treino_Calisteina\*.pdf')
all_urls = []

for pdf_path in pdf_files:
    print(f'\n=== {os.path.basename(pdf_path)} ===')
    with open(pdf_path, 'rb') as f:
        content = f.read().decode('latin-1', errors='ignore')
    
    # Procura URLs diretas
    urls = re.findall(r'https?://[^\s\x00-\x1f\)\]>\"\\]+', content)
    urls = list(dict.fromkeys(urls))
    
    # Procura também padrões de URI em PDFs (objetos /URI)
    uri_pattern = re.findall(r'/URI\s*\(([^)]+)\)', content)
    uri_pattern = list(dict.fromkeys(uri_pattern))
    
    combined = list(dict.fromkeys(urls + uri_pattern))
    
    if combined:
        for u in combined:
            print(u)
            all_urls.append(u)
    else:
        print('(nenhuma URL encontrada)')

print(f'\n\nTOTAL: {len(all_urls)} URLs encontradas')
