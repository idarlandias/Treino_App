import pypdf
import glob
import os
import json

files = glob.glob('e:/Treino_Calisteina/*.pdf')
results = {}

for f in files:
    fname = os.path.basename(f)
    results[fname] = []
    try:
        r = pypdf.PdfReader(f)
        for page_num, page in enumerate(r.pages):
            if '/Annots' in page:
                for ann in page['/Annots']:
                    try:
                        obj = ann.get_object()
                        if '/A' in obj and '/URI' in obj['/A']:
                            url = obj['/A']['/URI']
                            # Tenta pegar o texto do link (nome do exercicio)
                            title = ''
                            if '/Contents' in obj:
                                title = obj['/Contents']
                            results[fname].append({
                                'page': page_num + 1,
                                'url': url,
                                'title': title
                            })
                    except:
                        pass
    except Exception as e:
        results[fname] = [{'error': str(e)}]

# Salva resultado
with open('e:/Treino_Calisteina/links_resultado.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

# Imprime resumo
total = sum(len(v) for v in results.values() if isinstance(v, list))
print(f'Total de links encontrados: {total}')
for fname, links in results.items():
    print(f'\n{fname}: {len(links)} links')
    for lnk in links[:5]:
        print(f"  [{lnk.get('title','?')}] -> {lnk.get('url','')}")
    if len(links) > 5:
        print(f'  ... e mais {len(links)-5}')
