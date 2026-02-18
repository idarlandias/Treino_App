import pdfplumber
import glob
import os
import json

files = glob.glob('e:/Treino_Calisteina/*.pdf')
all_mappings = {}

for f in files:
    fname = os.path.basename(f)
    print(f'\n{"="*60}')
    print(f'PDF: {fname}')
    
    try:
        with pdfplumber.open(f) as pdf:
            for page_num, page in enumerate(pdf.pages):
                print(f'\n--- Pagina {page_num+1} ---')
                
                # Pega todos os hyperlinks da pagina
                hyperlinks = page.hyperlinks
                
                # Pega todas as palavras com posicao
                words = page.extract_words()
                
                print(f'Links encontrados: {len(hyperlinks)}')
                
                for link in hyperlinks:
                    url = link.get('uri', '')
                    if not url:
                        continue
                    
                    # Coordenadas do link
                    lx0 = link.get('x0', 0)
                    ly0 = link.get('y0', 0)
                    lx1 = link.get('x1', 0)
                    ly1 = link.get('y1', 0)
                    
                    # Encontra palavras que se sobrepoem com o link
                    matching_words = []
                    for w in words:
                        wx0 = w.get('x0', 0)
                        wy0 = w.get('top', 0)
                        wx1 = w.get('x1', 0)
                        wy1 = w.get('bottom', 0)
                        
                        # Verifica sobreposicao
                        if (wx0 < lx1 and wx1 > lx0 and wy0 < ly1 and wy1 > ly0):
                            matching_words.append(w.get('text', ''))
                    
                    exercise_name = ' '.join(matching_words).strip()
                    print(f'  [{exercise_name}] -> {url}')
                    
                    if exercise_name:
                        all_mappings[exercise_name] = url

    except Exception as e:
        print(f'ERRO: {e}')

print(f'\n\nMAPEAMENTO FINAL ({len(all_mappings)} exercicios):')
for name, url in all_mappings.items():
    print(f'  {name}: {url}')

# Salva JSON
with open('e:/Treino_Calisteina/exercicios_urls.json', 'w', encoding='utf-8') as out:
    json.dump(all_mappings, out, ensure_ascii=False, indent=2)
