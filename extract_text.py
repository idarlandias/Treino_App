import pypdf
import glob
import os
import json

files = glob.glob('e:/Treino_Calisteina/*.pdf')

for f in files:
    fname = os.path.basename(f)
    print(f'\n{"="*60}')
    print(f'PDF: {fname}')
    print('='*60)
    try:
        r = pypdf.PdfReader(f)
        for page_num, page in enumerate(r.pages):
            print(f'\n--- Pagina {page_num+1} ---')
            # Extrai todo o texto da pagina
            text = page.extract_text()
            if text:
                print('TEXTO:')
                print(text[:3000])
            
            # Lista os links
            if '/Annots' in page:
                print('\nLINKS:')
                for i, ann in enumerate(page['/Annots']):
                    try:
                        obj = ann.get_object()
                        if '/A' in obj and '/URI' in obj['/A']:
                            url = obj['/A']['/URI']
                            # Pega o rect (posicao do link na pagina)
                            rect = obj.get('/Rect', [])
                            print(f'  [{i}] rect={rect} -> {url}')
                    except:
                        pass
    except Exception as e:
        print(f'ERRO: {e}')
