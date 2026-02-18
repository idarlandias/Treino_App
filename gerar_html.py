
# Converte URL do Drive para URL direta de imagem
def drive_img(file_id):
    return f"https://lh3.googleusercontent.com/d/{file_id}"

def drive_url_to_id(url):
    # https://drive.google.com/file/d/ID/view?usp=sharing
    import re
    m = re.search(r'/d/([^/]+)/', url)
    return m.group(1) if m else None

# Mapeamento dos GIFs do Drive (extraidos dos PDFs)
# Exercicios de academia disponiveis:
DRIVE = {
    "pulley_corda":     "1r8kXucHXelSiUXG7iKzMF5t_AVuvNu5N",
    "supininho":        "1GlwcKx2NyC9d4tLY7KzLG6iGCmMOCzRe",
    "pulldown":         "1ZuEyqWhYLjtPLNYFmSBHXfvWVgsNt6iY",
    "barra_fixa":       "1R7zdVANa4P2W4mtTq59PlehVRMX7NAsa",
    "remada_curvada":   "1RDBUzgVS3-nXH5Vp23xN_RUJWljgOChQ",
    "rosca_martelo":    "1ZuEyqWhYLjtPLNYFmSBHXfvWVgsNt6iY",
    "rosca_direta":     "1ge1jnA1-6BH3GdfkiTZce5cYB5zY8s5e",
    "encolhimento":     "1AZJ79XqNwJMkl-Sz4lFSbIn1CARGLKHi",
    "supino_inclinado": "1BRyGX_cR8cZGZuxudJvtRM6xcY5oN8aO",
    "supino_reto":      "1W6ibsEIde5mcJxui4rnwQiRdDsT1L1EO",
    "rosca_21":         "1hld_imFINYZ2nV-nxNK8XB4OOo5oPjc8",
    "rosca_alternada":  "1RDBUzgVS3-nXH5Vp23xN_RUJWljgOChQ",
    "desenvolvimento":  "1fmspp8ufXk-LbMy9t8XxG7TbkjvgfsaT",
    "flexao_joelho":    "1-i_kZHTVlZtM-mHEWzWvSQBu2hkYboIg",
    "afundo":           "1sLzi_Xnmy4U_38qiVO1iP1DkO4dCNZuC",
    "paralela":         "1AZJ79XqNwJMkl-Sz4lFSbIn1CARGLKHi",
    "triceps_testa":    "1qvchD55eVGMXdNPvXFT9N25B1b1YU-RI",
    "crossover":        "1RZhap3zBgpVdfaBp2lbEjIKTLhist-G8",
    "supino_incl2":     "1-rIbW9ygaihZ0-CGdU6F5Ffy_XB2bbOa",
    "abdomen":          "1ZuEyqWhYLjtPLNYFmSBHXfvWVgsNt6iY",
    "exercicio_gen":    "1hld_imFINYZ2nV-nxNK8XB4OOo5oPjc8",
    "agach_bulgaro":    "1A5OSmDDwM25JUXkqLa_DV_2aV9XDH_gg",
    "ponte":            "1D1N7rVwtS6ZYj1VC6nNSf8LwKKfI47Pt",
    "panturrilha":      "1Nb5o_fOokk-IqLRvI9eb0SSLzelXTx6T",
    "prancha":          "1hOS2-l4EFHX9xeutX8GCIBk6k85ahUdy",
    "superman":         "1cd6bthCXemX8zWFUJ4uJIuesq1S2YIq9",
    "burpee":           "1D9GaliZUyPMNKLGTKQKQklmIo5RrGv8a",
    "mountain":         "1CO8TAjIm60PXdLEFyZ3XzgU1dW9UOEbA",
    "jumping_jack":     "1uySwPdS6LBjI-WqIF_2tYHIVMbdDdGXC",
    "agach_salto":      "1JTAkfullt5N3xJRXbJckvpyFz5axKjuZ",
    "joelho_alto":      "1kd2C7PerZcg2vKtdB1RTyuLqxtxb8xnT",
    "polichinelo":      "1aze2Yc5RRF9bGQNzkVPuh7BnbG82evjv",
    "remada_inv":       "1fmspp8ufXk-LbMy9t8XxG7TbkjvgfsaT",
    "prancha_lat":      "1NJSD8adc6XzBobkMXKAQ2i8WzXc2bHJX",
    "bicicleta":        "1-Sq0LuLfB2rfy_C64m2qGs-gyokyONM_",
    "prancha_ombro":    "1REwtt2tZ2BAIOFOlHsGq01wgiFz3jPzj",
    "agachamento":      "1y9fhKMGFh9fj_LST2CvkIAVCVp-fEymz",
    "flexao":           "1d5-lYx2e0VztuVt0JVh8XQ-S4bCI7ns0",
    "flexao_larga":     "1ge1jnA1-6BH3GdfkiTZce5cYB5zY8s5e",
    "rosca_galao":      "1_CnTy4aBr_Jb9cwYR4xX247QiKhlf2CO",
    "mergulho":         "1FMs3eFx5teDXkc87qE9-RyIfF82Guyv5",
    "pike":             "1nmY6YXTLi0TIb6NxeSLDGKjBn2i0q7ko",
    "hindu":            "1ljNwzS9fKossboRcoMIWwZlajbF_sdds",
    "afundo2":          "1-i_kZHTVlZtM-mHEWzWvSQBu2hkYboIg",
}

def img(key, alt):
    fid = DRIVE.get(key, DRIVE["exercicio_gen"])
    url = drive_img(fid)
    return f'''<div class="vid-box">
        <img src="{url}" alt="{alt}" loading="lazy" onerror="this.src='https://lh3.googleusercontent.com/d/1hld_imFINYZ2nV-nxNK8XB4OOo5oPjc8'">
        <span class="source">Google Drive</span>
      </div>'''

CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#06090f;--card:#0c1220;--surface:#111a2e;
  --accent:#4f8cff;--accent2:#00d4aa;--red:#ff6b6b;
  --warm:#ffb347;--purple:#a78bfa;
  --text:#e8ecf4;--text2:#94a3c0;--border:#1a2744;
}
body{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
.hero{text-align:center;padding:48px 24px 28px}
.hero::after{content:'';display:block;max-width:600px;height:1px;background:linear-gradient(90deg,transparent,var(--border),transparent);margin:28px auto 0}
.pill{display:inline-flex;align-items:center;gap:6px;background:var(--surface);border:1px solid var(--border);color:var(--accent2);padding:5px 14px;border-radius:100px;font-size:.72rem;font-weight:600;letter-spacing:.4px;text-transform:uppercase;margin-bottom:16px}
.hero h1{font-size:clamp(1.6rem,4vw,2.5rem);font-weight:700;color:#fff}
.hero h1 span{background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text2);margin-top:8px;font-size:.9rem}
.tabs{display:flex;justify-content:center;gap:6px;padding:20px 16px;position:sticky;top:0;z-index:20;background:linear-gradient(var(--bg) 65%,transparent);flex-wrap:wrap}
.tab{background:var(--card);border:1px solid var(--border);color:var(--text2);padding:9px 18px;border-radius:11px;font-family:inherit;font-size:.82rem;font-weight:600;cursor:pointer;transition:.3s;position:relative;overflow:hidden}
.tab::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,var(--accent),var(--accent2));opacity:0;transition:.3s}
.tab:hover{border-color:var(--accent);color:#fff}
.tab.active{border-color:transparent;color:#fff;box-shadow:0 4px 20px rgba(79,140,255,.25)}
.tab.active::before{opacity:1}
.tab em{position:relative;z-index:1;font-style:normal}
.panel{max-width:900px;margin:0 auto;padding:0 20px 40px;display:none}
.panel.show{display:block;animation:fadeIn .4s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.panel-head{margin-bottom:28px}
.panel-head h2{font-size:1.35rem;font-weight:700;color:#fff;display:flex;align-items:center;gap:10px}
.panel-head h2 .tag{font-size:.65rem;padding:4px 10px;border-radius:6px;font-weight:700;letter-spacing:.5px}
.panel-head p{color:var(--text2);margin-top:4px;font-size:.85rem}
.ex{background:var(--card);border:1px solid var(--border);border-radius:18px;margin-bottom:14px;overflow:hidden;transition:.3s}
.ex:hover{border-color:rgba(79,140,255,.25)}
.ex-top{display:flex;align-items:center;justify-content:space-between;padding:16px 20px;cursor:pointer;gap:12px}
.ex-top h3{font-size:.95rem;font-weight:600;color:#fff;flex:1}
.reps{font-family:'Space Mono',monospace;font-size:.72rem;color:var(--accent2);background:rgba(0,212,170,.08);padding:3px 10px;border-radius:7px;white-space:nowrap}
.chevron{width:28px;height:28px;border-radius:8px;background:var(--surface);display:flex;align-items:center;justify-content:center;transition:.3s;flex-shrink:0;color:var(--text2);font-size:.7rem}
.ex.open .chevron{background:var(--accent);color:#fff;transform:rotate(180deg)}
.ex-body{max-height:0;overflow:hidden;transition:max-height .45s cubic-bezier(.4,0,.2,1)}
.ex.open .ex-body{max-height:1400px}
.ex-inner{padding:0 20px 20px;display:grid;grid-template-columns:280px 1fr;gap:24px;align-items:start}
@media(max-width:680px){.ex-inner{grid-template-columns:1fr;gap:16px}}
.vid-box{background:#000;border-radius:14px;overflow:hidden;aspect-ratio:1/1;position:relative;border:1px solid var(--border)}
.vid-box img{width:100%;height:100%;object-fit:cover;display:block}
.vid-box .source{position:absolute;bottom:6px;right:8px;font-size:.55rem;color:rgba(255,255,255,.35);font-family:'Space Mono',monospace;background:rgba(0,0,0,.5);padding:2px 6px;border-radius:4px}
.info h4{font-size:.68rem;text-transform:uppercase;letter-spacing:.8px;color:var(--accent);margin-bottom:12px;font-weight:700}
.step{display:flex;gap:10px;margin-bottom:10px}
.step-n{width:22px;height:22px;border-radius:7px;background:var(--surface);border:1px solid var(--border);color:var(--accent);font-family:'Space Mono',monospace;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.step p{font-size:.85rem;line-height:1.5}
.tip{margin-top:12px;padding:10px 14px;background:rgba(255,179,71,.06);border:1px solid rgba(255,179,71,.12);border-radius:10px;display:flex;gap:8px}
.tip p{font-size:.8rem;color:var(--warm);line-height:1.45}
.muscles{display:flex;flex-wrap:wrap;gap:5px;margin-top:12px}
.muscle{font-size:.65rem;padding:2px 8px;border-radius:5px;background:rgba(167,139,250,.08);color:var(--purple);font-weight:600;border:1px solid rgba(167,139,250,.12)}
.footer{text-align:center;padding:32px 20px 56px;border-top:1px solid var(--border);max-width:900px;margin:0 auto}
.footer p{color:var(--text2);font-size:.8rem}
"""

def ex_card(name, reps, gif_key, steps, tip, muscles, open_class=""):
    steps_html = "".join(f'<div class="step"><div class="step-n">{i+1}</div><p>{s}</p></div>' for i,s in enumerate(steps))
    muscles_html = "".join(f'<span class="muscle">{m}</span>' for m in muscles)
    return f"""
  <div class="ex {open_class}">
    <div class="ex-top"><h3>{name}</h3><span class="reps">{reps}</span><div class="chevron">▼</div></div>
    <div class="ex-body"><div class="ex-inner">
      {img(gif_key, name)}
      <div class="info">
        <h4>Execucao Correta</h4>
        {steps_html}
        <div class="tip"><span>💡</span><p>{tip}</p></div>
        <div class="muscles">{muscles_html}</div>
      </div>
    </div></div>
  </div>"""

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Protocolo Calistenia — Guia Visual com Demonstracoes</title>
<style>{CSS}</style>
</head>
<body>

<div class="hero">
  <div class="pill">Guia Visual com Demonstracoes Reais</div>
  <h1>Protocolo de <span>Calistenia</span></h1>
  <p>GIFs animados mostrando a execucao correta de cada exercicio</p>
</div>

<div class="tabs">
  <button class="tab active" data-t="a"><em>Treino A</em></button>
  <button class="tab" data-t="b"><em>Treino B</em></button>
  <button class="tab" data-t="c"><em>Treino C</em></button>
  <button class="tab" data-t="h"><em>HIIT Cardio</em></button>
</div>

<!-- TREINO A -->
<div class="panel show" id="p-a">
  <div class="panel-head">
    <h2><span class="tag" style="background:rgba(79,140,255,.12);color:var(--accent)">TREINO A</span>Peito, Ombro e Triceps</h2>
    <p>Foco em empurrar — 6 exercicios — ~40 min</p>
  </div>
  {ex_card("Flexao","4 × 10-15","flexao",
    ["Maos na largura dos ombros, corpo reto da cabeca aos pes. Core contraido.",
     "Desce controlado ate o peito quase encostar no chao. Cotovelos a ~45° do tronco.",
     "Empurra o chao com forca pra subir, sem travar os cotovelos no topo."],
    "Muito pesada? Comeca com as maos num banco ou sofa e vai abaixando a altura.",
    ["Peitoral","Triceps","Deltoide Anterior"], "open")}
  {ex_card("Flexao Diamante","3 × 8-12","supininho",
    ["Maos juntas formando um losango — indicadores e polegares se tocam.",
     "Desce controlado com os cotovelos colados ao corpo.",
     "Empurra pra cima focando na contracao do triceps."],
    "Se nao consegue 8 reps, faz de joelhos ate ganhar forca.",
    ["Triceps","Peitoral Interno"])}
  {ex_card("Mergulho em Cadeira (Triceps)","4 × 10-15","mergulho",
    ["Maos na borda da cadeira/banco, dedos pra frente. Pernas esticadas.",
     "Desce dobrando os cotovelos ate ~90°. Costas perto da cadeira.",
     "Empurra pra cima com a forca do triceps."],
    "Facilitar: dobre os joelhos. Dificultar: pes numa segunda cadeira.",
    ["Triceps","Deltoide Anterior","Peitoral Inferior"])}
  {ex_card("Flexao Pike (Ombro)","3 × 8-12","pike",
    ["Posicao de flexao, empurra o quadril pra cima formando um V invertido.",
     "Desce a cabeca em direcao ao chao entre as maos.",
     "Empurra pra cima. Foco nos deltoides (ombros)."],
    "Pes mais perto das maos = mais dificil. E a base pro handstand pushup.",
    ["Deltoide","Triceps","Trapezio"])}
  {ex_card("Flexao Hindu","3 × 8-10","hindu",
    ["Comeca em V invertido. Mergulha o corpo pra frente e pra baixo.",
     "Desliza o peito rente ao chao num arco fluido.",
     "Termina arqueando as costas (cobra), volta ao V."],
    "Movimento fluido e circular. Trabalha peito, ombro e flexibilidade.",
    ["Peitoral","Deltoide","Triceps","Erector Spinae"])}
  {ex_card("Prancha Frontal","3 × 30-45s","prancha",
    ["Apoio nos antebracos e pontas dos pes. Corpo alinhado como tabua.",
     "Contrai abdomen e gluteos. Quadril nao sobe nem desce.",
     "Mantem a posicao respirando normalmente."],
    "Se tremer, ta funcionando. Foca na respiracao estavel.",
    ["Reto Abdominal","Transverso","Obliquos","Gluteos"])}
</div>

<!-- TREINO B -->
<div class="panel" id="p-b">
  <div class="panel-head">
    <h2><span class="tag" style="background:rgba(0,212,170,.1);color:var(--accent2)">TREINO B</span>Perna e Core</h2>
    <p>Membros inferiores + estabilidade — 6 exercicios — ~40 min</p>
  </div>
  {ex_card("Agachamento Livre","4 × 15-20","agachamento",
    ["Pes na largura dos ombros, pontas levemente pra fora.",
     "Desce como se fosse sentar. Joelhos na direcao dos pes.",
     "Coxas paralelas ao chao. Sobe empurrando com os calcanhares."],
    "Bracos a frente ajudam no equilibrio. Peso nos calcanhares.",
    ["Quadriceps","Gluteos","Isquiotibiais"])}
  {ex_card("Afundo Alternado","4 × 12 cada","afundo",
    ["Em pe, da um passo largo pra frente mantendo tronco reto.",
     "Desce ate o joelho de tras quase tocar o chao. Ambos a ~90°.",
     "Empurra com a perna da frente pra voltar. Alterna."],
    "Joelho da frente nao passa a ponta do pe. Tronco ereto.",
    ["Quadriceps","Gluteos","Isquiotibiais"])}
  {ex_card("Agachamento Bulgaro","3 × 10 cada","agach_bulgaro",
    ["De costas pro sofa, apoia o peito do pe de tras no assento.",
     "Desce controlado ate o joelho de tras quase tocar o chao.",
     "Sobe empurrando com a perna da frente. Faz todas reps de um lado, troca."],
    "Um dos melhores exercicios pra quadriceps e gluteos. Se tremer, e normal.",
    ["Quadriceps","Gluteo Maximo","Core"])}
  {ex_card("Elevacao de Quadril (Ponte)","4 × 15-20","ponte",
    ["Deitado de barriga pra cima, joelhos dobrados, pes no chao.",
     "Empurra o quadril pra cima apertando os gluteos.",
     "Segura 1-2s no topo, desce controlado sem encostar no chao."],
    "Pra dificultar: faz unilateral (uma perna estendida).",
    ["Gluteo Maximo","Isquiotibiais","Core"])}
  {ex_card("Panturrilha em Pe (Unilateral)","4 × 15 cada","panturrilha",
    ["Em pe, apoio na parede. Uma perna flexionada atras.",
     "Sobe na ponta do pe o maximo possivel, segura 1s.",
     "Desce controlado. Usar degrau aumenta amplitude."],
    "Panturrilha forte previne lesao e melhora explosao.",
    ["Gastrocnemio","Soleo"])}
  {ex_card("Prancha Lateral","3 × 30s cada","prancha_lat",
    ["De lado, apoio no antebraco. Corpo reto, pes empilhados.",
     "Levanta o quadril. Linha reta da cabeca aos pes.",
     "Mantem contraindo o obliquo. Troca de lado."],
    "Essencial pra cintura definida. Trabalha obliquos intensamente.",
    ["Obliquos","Gluteo Medio","Core"])}
</div>

<!-- TREINO C -->
<div class="panel" id="p-c">
  <div class="panel-head">
    <h2><span class="tag" style="background:rgba(167,139,250,.1);color:var(--purple)">TREINO C</span>Costas, Biceps e Core</h2>
    <p>Foco em puxar — mesa, vassoura e mochila — 6 exercicios — ~40 min</p>
  </div>
  {ex_card("Remada Invertida (mesa)","4 × 10-12","remada_inv",
    ["Deita embaixo de mesa firme. Segura na borda.",
     "Corpo reto, calcanhares no chao. Puxa o peito pra mesa.",
     "Aperta escapulas no topo, desce controlado."],
    "Alternativa: vassoura entre duas cadeiras. Melhor substituto da barra fixa.",
    ["Dorsal","Romboides","Biceps","Trapezio"])}
  {ex_card("Superman (Lombar)","3 × 15","superman",
    ["Deitado de brucos, bracos a frente, pernas esticadas.",
     "Levanta bracos e pernas ao mesmo tempo, contraindo lombar.",
     "Segura 1-2s no topo, desce controlado. Queixo neutro."],
    "Fortalece cadeia posterior e previne dor nas costas.",
    ["Eretor da Espinha","Gluteos","Trapezio"])}
  {ex_card("Flexao Larga","3 × 10-12","flexao_larga",
    ["Flexao com maos bem mais abertas que os ombros.",
     "Desce controlado sentindo o peito esticar.",
     "Sobe focando na contracao do peitoral externo."],
    "Mais enfase no peitoral. Complementa as outras variacoes.",
    ["Peitoral (externo)","Deltoide Anterior"])}
  {ex_card("Rosca com Mochila/Galao","3 × 12-15","rosca_galao",
    ["Em pe segurando galao de agua (5L) ou mochila com livros.",
     "Cotovelo fixo na lateral. Sobe dobrando o braco.",
     "Contrai biceps no topo, desce sem balancar o corpo."],
    "Galao 5L = ~5kg. Mochila com livros chega a 8-10kg facil.",
    ["Biceps","Braquial"])}
  {ex_card("Prancha com Toque no Ombro","3 × 10 cada","prancha_ombro",
    ["Prancha alta (bracos esticados).",
     "Tira uma mao e toca o ombro oposto. Corpo nao gira.",
     "Volta e repete do outro lado. Quadril firme."],
    "Anti-rotacao pura. Quanto mais lento, mais efetivo.",
    ["Core","Deltoide","Obliquos"])}
  {ex_card("Abdominal Bicicleta","3 × 20 total","bicicleta",
    ["Deitado, maos atras da cabeca, pernas elevadas.",
     "Cotovelo direito ao joelho esquerdo, estica a outra perna.",
     "Alterna num movimento de pedalar. Nao puxa o pescoco."],
    "O tronco gira, nao o pescoco. Sente o obliquo queimar.",
    ["Obliquos","Reto Abdominal","Iliopsoas"])}
</div>

<!-- HIIT -->
<div class="panel" id="p-h">
  <div class="panel-head">
    <h2><span class="tag" style="background:rgba(239,68,68,.1);color:var(--red)">HIIT</span>Cardio — Queima Maxima</h2>
    <p>4 rodadas | 30s trabalho / 15s descanso | 1-2 min entre rodadas | ~25 min</p>
  </div>
  {ex_card("Burpee","30s ON / 15s OFF","burpee",
    ["Em pe — agacha, maos no chao.",
     "Joga pes pra tras (flexao), faz uma flexao.",
     "Puxa pes de volta, salta com bracos pra cima. Repete."],
    "Pesado? Tira a flexao ou o salto. O importante e manter o ritmo.",
    ["Corpo Inteiro","Cardio"])}
  {ex_card("Mountain Climber","30s ON / 15s OFF","mountain",
    ["Prancha alta (bracos esticados).",
     "Puxa um joelho ao peito rapidamente.",
     "Alterna rapido mantendo core ativado."],
    "Quadril baixo e estavel. Velocidade controlada vence.",
    ["Core","Iliopsoas","Cardio"])}
  {ex_card("Jumping Jack","30s ON / 15s OFF","jumping_jack",
    ["Em pe, pes juntos, bracos na lateral.",
     "Salta abrindo pernas e levantando bracos acima da cabeca.",
     "Salta de volta. Ritmo alto e constante."],
    "Parece simples, mas em alta intensidade por 30s vira cardio pesado.",
    ["Deltoides","Panturrilha","Cardio"])}
  {ex_card("Agachamento com Salto","30s ON / 15s OFF","agach_salto",
    ["Agachamento completo, coxas paralelas.",
     "Explode num salto o mais alto possivel.",
     "Aterrissa suave na ponta dos pes, ja desce pro proximo."],
    "Aterrissagem suave protege os joelhos. Cai leve, flexionando.",
    ["Quadriceps","Gluteos","Panturrilha"])}
  {ex_card("Corrida no Lugar (Joelho Alto)","30s ON / 15s OFF","joelho_alto",
    ["Corre no lugar levantando joelhos ate a cintura.",
     "Bracos acompanham naturalmente.",
     "Ritmo alto por 30 segundos."],
    "Se o joelho nao chega na cintura, nao conta!",
    ["Iliopsoas","Quadriceps","Cardio"])}
  {ex_card("Polichinelo Cruzado","30s ON / 15s OFF","polichinelo",
    ["Similar ao jumping jack, mas bracos e pernas cruzam.",
     "Salta abrindo, depois salta cruzando.",
     "Alterna qual braco/perna fica na frente."],
    "Trabalha coordenacao e ativa aductores (parte interna da coxa).",
    ["Aductores","Deltoides","Cardio"])}
</div>

<div class="footer">
  <p style="font-weight:600;color:#fff;margin-bottom:4px">Protocolo de Calistenia em Casa — Guia Visual</p>
  <p>24 exercicios com demonstracao animada | GIFs: Google Drive | Custo: R$0,00</p>
</div>

<script>
document.querySelectorAll('.tab').forEach(t => {{
  t.addEventListener('click', () => {{
    document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
    t.classList.add('active');
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('show'));
    document.getElementById('p-' + t.dataset.t).classList.add('show');
  }});
}});
document.querySelectorAll('.ex-top').forEach(h => {{
  h.addEventListener('click', () => h.closest('.ex').classList.toggle('open'));
}});
</script>
</body>
</html>"""

with open('e:/Treino_Calisteina/guia_exercicios_com_videos.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML gerado com sucesso!")
print(f"Total de exercicios: 24")
