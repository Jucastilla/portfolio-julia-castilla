"""Portfólio de Júlia Castilla — Streamlit.
Execute com: streamlit run app.py
As imagens em assets/ foram recortadas das referências visuais aprovadas.
"""
from pathlib import Path
import base64
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portfólio | Júlia Castilla", page_icon=Image.open(Path(__file__).resolve().parent / "assets" / "favicon.png"), layout="wide", initial_sidebar_state="collapsed")
st.markdown('''<style>
#MainMenu, footer, header {visibility:hidden!important}
.block-container {max-width:100%!important;padding:0!important;margin:0!important}
[data-testid="stAppViewContainer"] {background:#fff}
[data-testid="stVerticalBlock"] {gap:0!important}
iframe {display:block;border:0!important;height:100vh!important}
[data-testid="stAppViewContainer"] {overflow:hidden!important}
[data-testid="stMain"] {overflow:hidden!important}

/* Justificado preservado, com palavras inteiras, sem hifenização. */
.about-text p,.service-card p,.project-body p{
  text-align:justify;
  text-align-last:left;
  hyphens:none;
  -webkit-hyphens:none;
  overflow-wrap:normal;
  word-break:normal;
  word-spacing:normal;
  -webkit-text-size-adjust:100%;
}

/* Sobre mim: alinhamento justificado preservado */
.about-text p{ text-align:justify; text-align-last:left; text-justify:inter-word; hyphens:none; -webkit-hyphens:none; overflow-wrap:normal; }
</style>''', unsafe_allow_html=True)
ROOT = Path(__file__).resolve().parent

def img(name):
    data=(ROOT/'assets'/name).read_bytes()
    return 'data:image/jpeg;base64,'+base64.b64encode(data).decode()

projects = [
    dict(name='Projeto Nossa Entrega', desc='Análise de dados de uma iniciativa voluntária de apoio a pessoas em situação de rua, identificando padrões de participação dos voluntários e da logística de transportes, com resultados apresentados em dashboard interativo.', tech=['Python','Pandas','Plotly','Streamlit'], cat='outras', image='nossa-entrega.jpg', url='https://github.com/Jucastilla/projeto-nossa-entrega'),
    dict(name='Análise do Mercado Publicitário Audiovisual (ANCINE)', desc='Consolidação de 164 arquivos CSV e integração de três bases da ANCINE para analisar o mercado publicitário audiovisual, com resultados apresentados em dashboard interativo.', tech=['Python','BigQuery','Looker Studio'], cat='marketing', image='ancine.jpg', url='https://github.com/Jucastilla/analise-mercado-publicitario-ancine'),
    dict(name='London Crime Analysis', desc='Estudo de 6 milhões de crimes em Londres para identificar áreas prioritárias e apresentar recomendações em um dashboard Power BI.', tech=['Python','SQL','BigQuery','Power BI'], cat='outras', image='london.jpg', url='https://github.com/Jucastilla/london-crime-analysis'),
    dict(name='Análise de Dados da COVID-19', desc='Automação de consultas e tratamento de dados da COVID-19 com Python e BigQuery, gerando bases validadas em CSV e Parquet.', tech=['Python','SQL','BigQuery'], cat='outras', image='covid.jpg', url='https://github.com/Jucastilla/projeto-covid-bigquery'),
    dict(name='Análise de Engajamento do Hacker News', desc='Análise de 49 milhões de registros com 12 consultas SQL, identificando padrões de publicação e engajamento no Hacker News.', tech=['SQL','BigQuery'], cat='marketing', image='hacker.jpg', url='https://github.com/Jucastilla/hacker-news-bigquery-analysis-'),
    dict(name='Análise de Insatisfação de Clientes da Olist', desc='Investigação da insatisfação de clientes da Olist por meio de modelos preditivos e dashboard. A análise identificou maior insatisfação nos pedidos entregues com atraso.', tech=['Python','Machine Learning','Looker Studio'], cat='marketing', image='olist.jpg', url='https://github.com/Jucastilla/analise-insatisfacao-olist'),
    dict(name='Análise Estratégica de Vendas', desc='Integração de seis bases comerciais no Power BI para analisar receita, custos, lucro e desempenho de vendas por produtos, regiões e representantes.', tech=['Power BI','Power Query','DAX'], cat='negocios', image='vendas.jpg', url='https://github.com/Jucastilla/analise-vendas-powerbi'),
    dict(name='Análise Exploratória de E-commerce', desc='Análise de preços, avaliações e vendas de produtos de comércio eletrônico, identificando padrões e relações entre variáveis, com resultados apresentados em dashboard interativo.', tech=['Python','Pandas','Plotly','Dash'], cat='marketing', image='ecommerce.jpg', url='https://github.com/Jucastilla/dashboard-ecommerce-'),
    dict(name='Análise de Dados de Restaurante', desc='Criação de banco de dados relacional para simular a gestão de um restaurante, com consultas SQL e indicadores de pedidos, clientes e produtos.', tech=['MySQL','SQL'], cat='negocios', image='restaurante.jpg', url='https://github.com/Jucastilla/analise-dados-restaurante-sql'),
    dict(name='Calculadora em Python e Linux', desc='Desenvolvimento de calculadoras em Python e Bash, com operações matemáticas, repetição de cálculos e tratamento de erros no terminal Linux.', tech=['Python','Shell Script','Linux'], cat='outras', image='calculadora.jpg', url='https://github.com/Jucastilla/calculadora-python-linux'),
]

services = [
    ('<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2 2h2l2.4 12.4a2 2 0 0 0 2 1.6h10.2a2 2 0 0 0 2-1.6L22 7H5"/></svg>','Análise de Vendas','Análise de faturamento, ticket médio, produtos mais vendidos e sazonalidade para identificar padrões de consumo, avaliar o desempenho comercial e orientar decisões estratégicas de vendas.','blue'),
    ('<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="15" height="13" rx="2"/><path d="M7 21h5m-2-5v5"/><rect x="17" y="9" width="5" height="12" rx="1"/></svg>','Análise de Sites e E-commerce','Análise de tráfego, navegação e comportamento dos visitantes para identificar obstáculos na jornada de compra e oportunidades de melhoria na experiência do usuário e na conversão.','purple'),
    ('<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>','Análise de Redes Sociais','Avaliação de métricas de alcance, engajamento e desempenho de conteúdos para identificar oportunidades de melhoria e orientar estratégias que fortaleçam a presença digital da marca.','blue'),
    ('<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4m10-4v4M3 10h18M7 14h3m4 0h3m-10 4h3"/></svg>','Estratégia de Social Media','Planejamento de conteúdo para redes sociais com foco em objetivos, público-alvo e posicionamento de marca, fortalecendo a comunicação digital.','purple'),
    ('<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L9 17l-4 1 1-4Z"/></svg>','Produção de Conteúdo Digital','Criação de conteúdos para redes sociais com técnicas de copywriting, alinhando linguagem, identidade da marca e interesses do público para comunicar mensagens relevantes e estimular o engajamento.','blue'),
]

from html import escape
service_html=''.join(f'<article class="service-card"><div class="service-icon {color}">{icon}</div><h3>{escape(title)}</h3><p>{escape(desc)}</p></article>' for icon,title,desc,color in services)
project_html=''.join(f'''<a class="project-card{' olist-card' if p['image']=='olist.jpg' else ''}" data-category="{p['cat']}" href="{p['url']}" target="_blank" rel="noopener noreferrer" aria-label="Abrir {escape(p['name'])} no GitHub">
<div class="project-photo"><img loading="lazy" src="{img(p['image'])}" alt="Ilustração do projeto {escape(p['name'])}"></div>
<div class="project-body"><h3>{escape(p['name']).replace('E-commerce', '<span style="white-space:nowrap">E-commerce</span>') if p['image']=='ecommerce.jpg' else escape(p['name'])}</h3><p>{escape(p['desc'])}</p><div class="project-bottom"><div class="tags">{''.join(f'<span>{escape(t)}</span>' for t in p['tech'])}</div><span class="github" aria-hidden="true"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56 0-.27-.01-1-.02-1.97-3.2.7-3.88-1.54-3.88-1.54-.52-1.32-1.28-1.67-1.28-1.67-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.56-.29-5.25-1.28-5.25-5.69 0-1.26.45-2.29 1.18-3.1-.12-.29-.51-1.47.11-3.05 0 0 .96-.31 3.16 1.18A11 11 0 0 1 12 6.07c.98 0 1.97.13 2.89.39 2.2-1.49 3.16-1.18 3.16-1.18.62 1.58.23 2.76.11 3.05.74.81 1.18 1.84 1.18 3.1 0 4.42-2.7 5.4-5.27 5.69.41.35.78 1.05.78 2.12 0 1.53-.01 2.76-.01 3.13 0 .31.21.68.8.56A11.51 11.51 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/></svg></span></div></div></a>''' for p in projects)

html = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Portfólio | Júlia Castilla</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--ink:#09164d;--text:#4f638d;--violet:#7839ff;--blue:#0859d6;--bg:#f7f9ff;--line:#e8edfb}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:'DM Sans',sans-serif;color:var(--ink);background:#fff}a{text-decoration:none;color:inherit}button{font:inherit;cursor:pointer}section{scroll-margin-top:104px}#servicos{scroll-margin-top:104px}.container{max-width:1390px;padding:0 36px;margin:auto}.topbar{height:88px;background:rgba(255,255,255,.96);border-bottom:1px solid #f1f3fb;position:sticky;top:0;z-index:20;backdrop-filter:blur(14px)}.nav-wrap{height:100%;display:flex;align-items:center;justify-content:space-between;gap:24px}.logo{font-family:Outfit,sans-serif;font-size:35px;font-weight:800;letter-spacing:-2.1px;white-space:nowrap;color:#101650}.logo-u{position:relative;color:#101650}.logo-u::before{content:"";position:absolute;width:.22em;height:.15em;left:.24em;top:.17em;transform:rotate(-32deg);transform-origin:center;background:linear-gradient(120deg,#00c6ed 10%,#3456ff 55%,#8c3cff 95%);border-radius:100% 0 100% 0;z-index:2;pointer-events:none}.logo-u{font-variant-ligatures:none;display:inline-block}.menu{display:flex;gap:42px;align-items:center}.menu a{font-size:18px;color:#354b7b;padding:12px 0;position:relative}.menu a.active{color:#693bff}.menu a:hover{color:#693bff}.menu a:hover:after,.menu a.active:after{content:'';height:2px;background:#6b3cff;position:absolute;bottom:5px;left:0;right:0}.cta,.primary{background:linear-gradient(100deg,#0055c9,#8b39f4);color:#fff;border-radius:11px;padding:16px 26px;font-weight:700;white-space:nowrap;box-shadow:0 8px 24px #2544c51b}.cta .cta-email{display:block;font-size:11px;font-weight:500;letter-spacing:.1px;margin-top:3px;opacity:.96}.cta .cta-title{display:block}.cta:hover,.primary:hover{filter:brightness(1.07)}.hamburger{display:none;border:0;background:none;color:var(--ink);font-size:27px}
.hero{min-height:710px;display:grid;grid-template-columns:49% 51%;align-items:center;gap:12px;padding-top:34px;padding-bottom:50px}.hero-copy h1{font-family:Outfit,sans-serif;font-size:clamp(34px,3.45vw,56px);line-height:1.13;letter-spacing:-2.6px;margin:0 0 55px;font-weight:800}.hero-line{white-space:nowrap}.highlight{background:linear-gradient(110deg,#0b5dcc,#873cf7);color:transparent;background-clip:text;-webkit-background-clip:text;white-space:nowrap;position:relative}.highlight:before{content:'';position:absolute;z-index:-1;background:#eef0ff;border-radius:11px;inset:0 -6px}.hero .primary{display:inline-flex;gap:16px;align-items:center;font-size:17px;padding:19px 26px}.social{display:flex;gap:16px;margin-top:33px}.social a{display:flex;width:48px;height:48px;align-items:center;justify-content:center;background:#e9efff;color:#0a397e;border-radius:13px;font-size:20px;font-weight:800}.social a:hover{background:#d9e4ff}.hero-art{position:relative;display:flex;justify-content:flex-end}.hero-art img{display:block;width:100%;max-width:700px;height:590px;object-fit:cover;object-position:center;border-radius:80px 40px 60px 85px;mask-image:linear-gradient(to right,transparent 0%,black 12%,black 100%)}
.about{background:#fff;padding:100px 0 112px}.about-layout{display:grid;grid-template-columns:48% 52%;gap:64px;align-items:center}.about-visual img{width:100%;max-width:610px;border-radius:24px;display:block}.eyebrow{color:#653aff;font-size:13px;font-weight:800;letter-spacing:.8px;text-transform:uppercase}.about-text{max-width:620px}.about-text p{color:#3e5184;font-size:17px;line-height:1.76;margin:22px 0;text-align:left}.about-text p:last-child{margin-bottom:0}.about-heading{font-family:Outfit,sans-serif;font-size:32px;font-weight:800;line-height:1.25;letter-spacing:-.8px;margin:0 0 26px}.about-heading span{display:inline-block;background:linear-gradient(110deg,#0b5dcc,#873cf7);background-clip:text;-webkit-background-clip:text;color:transparent}
.services,.projects{background:#f7f9ff;padding:95px 0 108px}.section-heading{text-align:center;margin-bottom:38px}.section-heading h2{font:700 clamp(26px,2.4vw,38px)/1.2 Outfit,sans-serif;margin:10px 0 10px}.section-heading p{font-size:16px;color:#667799;margin:0}.service-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;max-width:1050px;margin:auto}.service-card{padding:28px 32px 30px;background:white;border-radius:22px;min-height:220px;box-shadow:0 6px 26px #173d7710}.service-grid>.service-card:last-child{grid-column:1/-1;justify-self:center;width:calc((100% - 20px)/2)}.service-card h3{font-size:19px;margin:22px 0 15px}.service-card p{font-size:16px;line-height:1.65;text-align:left;hyphens:none;-webkit-hyphens:none;overflow-wrap:normal;word-spacing:normal;color:#677693;margin:0}.service-icon{width:54px;height:54px;border-radius:15px;display:grid;place-items:center;font-size:27px}.blue{background:#e6eeff;color:#2760e4}.purple{background:#eee7ff;color:#7634ec}.pink{background:#ffeaf2;color:#e83e84}.mint{background:#dff8f1;color:#1caa93}.orange{background:#fff0e7;color:#ef7b3e}
.projects{padding-top:86px}.projects .section-heading{margin-bottom:30px}.filters{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:26px}.filter{border:0;border-radius:11px;background:#edf2ff;color:#355591;padding:14px 20px;font-size:18px;min-width:170px;white-space:nowrap}.filter.active{background:linear-gradient(100deg,#0758d8,#8b3bf7);color:#fff}.filter:hover{box-shadow:0 4px 14px #284fd61c}.project-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}.project-card{display:flex;flex-direction:column;overflow:hidden;border:7px solid #fff;border-radius:19px;background:#fff;box-shadow:0 7px 28px #102e6b0d;transition:transform .2s,box-shadow .2s}.project-card:hover{transform:translateY(-5px);box-shadow:0 14px 32px #173b7b23}.project-card.hidden{display:none}.project-photo{width:100%;height:150px;overflow:hidden;border-radius:12px}.project-photo img{width:100%;height:100%;object-fit:cover}.project-body{padding:13px 12px 14px;display:flex;flex-direction:column;flex:1}.project-body h3{font-size:16px;line-height:1.25;margin:0 0 8px;font-weight:800}.project-body p{color:#637598;font-size:13px;line-height:1.48;margin:0 0 15px;flex:1}.project-bottom{display:flex;justify-content:space-between;align-items:flex-end;gap:6px}.tags{display:flex;gap:5px;flex-wrap:wrap}.tags span{font-size:11px;color:#6342df;background:#f0edff;border-radius:5px;padding:5px 7px}.github{font-size:24px;font-weight:700;color:#101650;line-height:1}.footer{padding:34px 0;text-align:center;color:#667799;font-size:13px;border-top:1px solid #eef0f8}.footer a{color:#5b40d5}
@media(max-width:1100px){.menu a{font-size:16px}.project-grid{grid-template-columns:repeat(3,1fr)}.hero-copy h1{font-size:clamp(31px,3.5vw,44px)}.menu{gap:24px}.about-layout{gap:30px}.about-text p{font-size:15px}}@media(max-width:760px){.container{padding-left:22px;padding-right:22px}.topbar{height:76px}.logo{font-size:27px}.topbar .cta{display:none}.hamburger{display:block}.menu{display:none;position:absolute;top:76px;left:0;right:0;background:#fff;padding:20px 24px;box-shadow:0 15px 22px #101d471c;flex-direction:column;gap:12px}.menu.open{display:flex}.hero{grid-template-columns:1fr;min-height:0;padding-top:64px;padding-bottom:65px}.hero-copy h1{font-size:clamp(28px,6.4vw,48px);letter-spacing:-1.8px;margin-bottom:30px}.hero-art{margin-top:36px;justify-content:center}.hero-art img{height:430px;max-width:500px}.about{padding:60px 0}.about-layout{grid-template-columns:1fr;gap:28px}.about-visual img{max-width:100%}.about-text p{font-size:15px}.services,.projects{padding:70px 0}.service-grid{grid-template-columns:1fr}.service-grid>.service-card:last-child{grid-column:auto;justify-self:stretch;width:100%}.project-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.project-photo{height:140px}.filter{min-width:0;flex:1 1 135px}.filters{gap:8px}.section-heading p{font-size:14px}.project-body h3{font-size:14px}}@media(max-width:470px){.project-grid{grid-template-columns:1fr}.project-photo{height:180px}.hero-art img{height:340px}.hero-copy h1{font-size:clamp(25px,6.8vw,34px)}.service-card{padding:23px}.section-heading h2{font-size:27px}}

/* Paleta extraída da referência enviada por Júlia — acabamento suave, sem neon. */
:root{
 --ink:#150F2C;
 --text:#4F4073;
 --violet:#4F4073;
 --blue:#3C2D5C;
 --bg:#F8F7FB;
 --line:#E8E3F0;
 --accent-light:#92CDED;
 --accent-lilac:#B382CD;
}
body{color:var(--ink);background:#FFFFFF}
.topbar{background:rgba(255,255,255,.98);border-bottom-color:#EDEAF3;backdrop-filter:blur(8px)}
.logo,.logo-u{color:#4F4073}
.logo-u::before{background:linear-gradient(120deg,#92CDED 8%,#B382CD 90%)}
.menu a{color:#3C2D5C}
.menu a.active,.menu a:hover{color:#4F4073}
.menu a:hover::after,.menu a.active::after{background:#B382CD}
.cta,.primary{background:linear-gradient(105deg,#426D97 0%,#567CA3 100%);color:white;box-shadow:0 7px 22px #426D971A}
.cta:hover,.primary:hover{filter:brightness(1.09)}
.highlight{background:linear-gradient(105deg,#376B9A 0%,#5A86AD 100%);background-clip:text;-webkit-background-clip:text;color:transparent}.about-heading span{background:linear-gradient(105deg,#3C2D5C 0%,#4F4073 56%,#76548D 100%);background-clip:text;-webkit-background-clip:text;color:transparent}
.highlight::before{background:#EAF2F8}
.social a{background:#F0EDF6;color:#3C2D5C}
.social a:hover{background:#E4DCEC}
.about{background:#fff}
.about-text p{color:#4F4073}
.services,.projects{background:#F8F7FB}
.service-card,.project-card{background:#FFFFFF;box-shadow:0 8px 26px #150F2C0B}
.service-card h3,.project-body h3{color:#150F2C}
.service-card p,.project-body p{color:#4F4073}
.service-icon.blue{background:#E8F4FA;color:#345A72}
.service-icon.purple{background:#EFE9F6;color:#61497E}
.service-icon.pink{background:#F3EAF1;color:#784C6F}
.service-icon.mint{background:#E8F3F2;color:#396B69}
.service-icon.orange{background:#F7EDE7;color:#8B604C}
.service-icon.blue{background:#E8F3FA;color:#527FA8}.service-icon.purple{background:#F0EAF7;color:#795DA2}.service-icon svg{display:block;width:25px;height:25px;flex-shrink:0}
.filter{background:#EEEAF4;color:#3C2D5C}
.filter:hover{background:#E6DCEC;color:#3C2D5C}
.filter.active{background:linear-gradient(105deg,#3C2D5C,#665080);color:#fff;box-shadow:0 4px 12px #150F2C10}
.tags span{background:#F0EAF5;color:#4F4073}
.github{color:#150F2C}
.project-card:hover{box-shadow:0 12px 28px #150F2C18}
.footer{color:#4F4073;border-top-color:#EDEAF3}
.footer a{color:#4F4073}
/* Hover das categorias e links de navegação em azul, sem neon. */
.menu a:hover,.menu a.active{color:#527FA8}
.menu a:hover::after,.menu a.active::after{background:#527FA8}
.filter:hover{background:#E8F3FA;color:#376B9A;box-shadow:0 4px 14px #527FA81A}
/* Reduzir intensidade da arte neon sem modificar os arquivos originais. */
.hero-art img{filter:none}
@media(max-width:760px){.menu{background:#FFFFFF}}
/* Alinhamento natural das descrições, sem lacunas de justificação. */
.project-body p{text-align:left;hyphens:none;-webkit-hyphens:none;overflow-wrap:normal;word-spacing:normal}
/* Mantém as três tecnologias da Olist lado a lado, com etiquetas discretamente mais compactas. */
.olist-card .tags{flex-wrap:nowrap;gap:3px;min-width:0}
.olist-card .tags span{font-size:10px;padding:4px 5px;white-space:nowrap}
.olist-card .project-bottom{gap:4px}
/* Leitura mais confortável em telas pequenas. */
@media(max-width:760px){.project-body p{text-align:left;hyphens:none;-webkit-hyphens:none}}
/* Alternância aprovada de fundos: início branco, sobre lilás, serviços branco, projetos lilás, rodapé branco. */
.hero{background:#FFFFFF}
.about{background:#FAF8FC}
.services{background:#FFFFFF}
.projects{background:#FAF8FC}
.footer{background:#FFFFFF}
/* Descrições justificadas dentro do iframe, sem hifenização, preservando palavras inteiras. */
.service-card p, .project-body p {
  text-align: justify !important;
  text-align-last: left;
  text-justify: inter-word;
  hyphens: none !important;
  -webkit-hyphens: none !important;
  overflow-wrap: normal;
  word-break: normal;
  word-spacing: normal;
}
/* Regra no documento do iframe: justificação efetiva do Sobre mim. */
.about-text p {text-align:justify !important;text-align-last:left;text-justify:inter-word;hyphens:none;-webkit-hyphens:none;overflow-wrap:normal;word-spacing:normal;}

/* Justificação sem hifenização: palavras inteiras em todas as descrições. */
.about-text p, .service-card p, .project-body p {
  text-align: justify !important;
  text-align-last: left;
  hyphens: none !important;
  -webkit-hyphens: none !important;
  -ms-hyphens: none !important;
  overflow-wrap: normal !important;
  word-break: normal !important;
  word-spacing: normal;
}
/* Refinamento global de leitura: justificado sem hifens e com linhas mais equilibradas.
   Em colunas estreitas a justificação pode criar espacos; ampliar a area util
   e reduzir levemente a fonte diminui esse efeito sem mudar o layout. */
.about-text p, .service-card p, .project-body p {
  text-align: justify !important;
  text-align-last: left !important;
  hyphens: none !important;
  -webkit-hyphens: none !important;
  -ms-hyphens: none !important;
  word-break: normal !important;
  overflow-wrap: normal !important;
  letter-spacing: 0.04px;
}
.project-body{padding-left:9px;padding-right:9px}
.project-body p{font-size:12.5px;line-height:1.55}
.service-card{padding-left:27px;padding-right:27px}
.service-card p{font-size:15.5px;line-height:1.68}
@media(max-width:760px){.project-body p{font-size:13px}.service-card p{font-size:15px}}
/* Rodapé horizontal: identidade à esquerda, contatos à direita. */
.footer{padding:28px 0 20px;background:#FFFFFF;text-align:left}
.footer-content{display:flex;flex-direction:column;align-items:stretch;gap:0}
.footer-main{display:flex;align-items:center;justify-content:space-between;gap:24px;padding-bottom:22px}
.footer-identity{display:flex;flex-direction:column;align-items:flex-start;min-width:0}
.footer-name{font-family:'Outfit',sans-serif;font-size:19px;font-weight:700;line-height:1.35;color:#3C2D5C}
.footer-role{margin-top:5px;font-size:13px;line-height:1.5;color:#4F4073}
.footer-links{display:flex;justify-content:flex-end;align-items:center;gap:22px;flex-wrap:wrap;margin:0}
.footer-links a{display:inline-flex;align-items:center;gap:7px;color:#4F4073;text-decoration:none;font-size:13px;transition:color .2s}
.footer-links a:hover{color:#8B63AE}
.footer-links svg{width:16px;height:16px;flex-shrink:0}
.footer-bottom{border-top:1px solid #EDE8F3;padding-top:15px;width:100%;color:#6E6284;font-size:12px;line-height:1.6;text-align:left}
@media(max-width:600px){.footer{padding:26px 0 20px}.footer-main{align-items:flex-start;flex-direction:column;gap:16px}.footer-links{justify-content:flex-start;gap:18px}.footer-name{font-size:18px}}

/* Responsividade: tablets e celulares */
html,body{max-width:100%;overflow-x:hidden}
.container{width:100%}
.hero,.about-layout,.service-grid,.project-grid,.hero-copy,.about-text,.service-card,.project-card{min-width:0}
@media(min-width:761px) and (max-width:1100px){
.container{padding-inline:28px}.logo{font-size:27px;letter-spacing:-1.4px}.menu{gap:17px}.menu a{font-size:15px}.cta{padding:13px 15px;font-size:14px}
.hero{grid-template-columns:minmax(0,1fr) minmax(0,1fr);min-height:560px;gap:22px}
.hero-copy h1{font-size:clamp(27px,3.3vw,39px);letter-spacing:-1.4px}.hero-art img{height:440px;border-radius:42px}
.about-layout{grid-template-columns:minmax(0,44%) minmax(0,56%);gap:22px}
.project-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.project-photo{height:190px}
}
@media(max-width:760px){
section,#servicos{scroll-margin-top:80px}
.container{padding-inline:20px}.topbar{height:72px}.nav-wrap{gap:12px}
.logo{font-size:clamp(23px,5vw,29px);letter-spacing:-1.4px}
.hamburger{display:flex;align-items:center;justify-content:center;min-width:44px;height:44px;border-radius:10px}
.hamburger:focus-visible,.menu a:focus-visible,.filter:focus-visible{outline:2px solid #527FA8;outline-offset:3px}
.menu{top:72px;gap:0;padding:12px 20px 18px;max-height:calc(100dvh - 72px);overflow-y:auto}
.menu a{width:100%;padding:13px 10px;font-size:17px}
.menu a:hover:after,.menu a.active:after{left:10px;right:auto;width:45px;bottom:7px}
.hero{display:flex;flex-direction:column;align-items:stretch;gap:22px;min-height:0;padding-top:45px;padding-bottom:55px}
.hero-copy h1{font-size:clamp(27px,5.9vw,43px);line-height:1.18;letter-spacing:-1.3px;margin-bottom:26px}
.hero-line,.highlight{white-space:normal}
.hero .primary{font-size:15px;padding:15px 18px}
.hero-art{margin:0;justify-content:center}
.hero-art img{width:100%;height:auto;max-height:420px;aspect-ratio:1.3;object-fit:cover;border-radius:35px;mask-image:none}
.about{padding:55px 0}.about-layout{grid-template-columns:minmax(0,1fr)}
.about-visual img{max-width:580px;margin-inline:auto}.about-text{max-width:none}.about-text p{font-size:15px;line-height:1.7}
.services,.projects{padding:58px 0 65px}
.service-grid{grid-template-columns:minmax(0,1fr)}.service-card{min-height:0}
.service-grid>.service-card:last-child{width:100%}
.project-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.project-photo{height:160px}.project-body{padding:12px}.project-body p{font-size:13px;line-height:1.55}
.filters{gap:8px}.filter{flex:1 1 auto;min-width:0;font-size:14px;padding:12px 14px;white-space:normal}
.footer-main{flex-wrap:wrap}
}
@media(max-width:520px){
.container{padding-inline:18px}.hero-copy h1{font-size:clamp(25px,6.2vw,34px)}
.hero-art img{max-height:330px}.project-grid{grid-template-columns:minmax(0,1fr)}
.project-photo{height:190px}.project-body h3{font-size:16px}.project-body p{font-size:14px}
.filter{flex:1 1 calc(50% - 8px)}.service-card{padding:23px}.footer-links{flex-wrap:wrap}
}
@media(max-width:360px){.container{padding-inline:14px}.logo{font-size:22px}.hero-copy h1{font-size:25px}.filter{font-size:13px;padding:11px 8px}}
</style></head><body>
<header class="topbar"><div class="container nav-wrap"><a class="logo" href="#inicio" aria-label="Júlia Castilla, início">J<span class="logo-u">u</span>lia Castilla</a><nav class="menu" id="menu"><a href="#inicio" class="active">Início</a><a href="#sobre">Sobre</a><a href="#servicos">Serviços</a><a href="#projetos">Projetos</a></nav><a class="cta" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=juliacruz943%40gmail.com&amp;su=Contato%20pelo%20portf%C3%B3lio%20de%20J%C3%BAlia%20Castilla" target="_blank" rel="noopener noreferrer" aria-label="Vamos conversar: enviar e-mail para Júlia Castilla pelo Gmail">Vamos conversar →</a><button class="hamburger" aria-label="Abrir menu" aria-controls="menu" aria-expanded="false" onclick="const m=document.getElementById('menu');const o=m.classList.toggle('open');this.setAttribute('aria-expanded',String(o));this.setAttribute('aria-label',o?'Fechar menu':'Abrir menu')">☰</button></div></header>
<main><section class="container hero" id="inicio"><div class="hero-copy"><h1>Transformando<br><span class="hero-line">dados em <span class="highlight">estratégias</span></span><br>para o seu negócio.</h1><a class="primary" href="#servicos">Conheça meus serviços&nbsp; →</a><div class="social"><a href="https://www.linkedin.com/in/juliacastilla" target="_blank" rel="noopener" title="LinkedIn" aria-label="LinkedIn">in</a><a href="https://github.com/Jucastilla" target="_blank" rel="noopener" title="GitHub" aria-label="GitHub"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56 0-.27-.01-1-.02-1.97-3.2.7-3.88-1.54-3.88-1.54-.52-1.32-1.28-1.67-1.28-1.67-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.56-.29-5.25-1.28-5.25-5.69 0-1.26.45-2.29 1.18-3.1-.12-.29-.51-1.47.11-3.05 0 0 .96-.31 3.16 1.18A11 11 0 0 1 12 6.07c.98 0 1.97.13 2.89.39 2.2-1.49 3.16-1.18 3.16-1.18.62 1.58.23 2.76.11 3.05.74.81 1.18 1.84 1.18 3.1 0 4.42-2.7 5.4-5.27 5.69.41.35.78 1.05.78 2.12 0 1.53-.01 2.76-.01 3.13 0 .31.21.68.8.56A11.51 11.51 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/></svg></a><a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=juliacruz943%40gmail.com&amp;su=Contato%20pelo%20portf%C3%B3lio%20de%20J%C3%BAlia%20Castilla" target="_blank" rel="noopener noreferrer" title="Enviar e-mail" aria-label="Enviar e-mail">✉</a></div></div><div class="hero-art"><img src="__HERO__" alt="Retrato futurista com circuitos luminosos e elementos de análise de dados"></div></section>
<section class="about" id="sobre"><div class="container about-layout"><div class="about-visual"><img src="__ABOUT__" alt="Espaço de trabalho com notebook, gráficos, livros e elementos geométricos em azul e roxo"></div><div class="about-text"><h2 class="about-heading"><span>Sobre mim</span></h2><p>Sou Júlia Castilla, Analista de Dados, graduada em Marketing Digital pela Universidade Estácio de Sá, com formação profissional em Análise de Dados e Social Media Manager pela EBAC.</p><p>Minha experiência em Marketing Digital, especialmente com SEO, Social Media e análise de indicadores de desempenho, ampliou meu interesse pelo uso estratégico dos dados. O contato com métricas, comportamento do público e avaliação de resultados contribuiu para o desenvolvimento de uma visão analítica, que aprofundei por meio da formação em Análise de Dados.</p><p>Desenvolvi competências em SQL, Python, Power BI, Google BigQuery e Looker Studio, aplicadas à preparação, integração, validação e visualização de dados. Em projetos práticos, analisei bases com aproximadamente 6 milhões de ocorrências criminais e 49 milhões de registros de engajamento, além de consolidar 164 arquivos CSV para estudar o mercado publicitário audiovisual brasileiro.</p><p>Hoje, reúno conhecimentos técnicos em Análise de Dados e experiência em Marketing Digital para identificar padrões, desenvolver indicadores e dashboards e transformar informações em análises que apoiem decisões estratégicas.</p></div></div></section>
<section class="services" id="servicos"><div class="container"><div class="section-heading"><h2 class="about-heading"><span>Meus serviços</span></h2></div><div class="service-grid">__SERVICES__</div></div></section>
<section class="projects" id="projetos"><div class="container"><div class="section-heading"><h2 class="about-heading"><span>Projetos</span></h2></div><div class="filters" role="group" aria-label="Filtrar projetos"><button class="filter active" data-filter="all">▦ &nbsp; Todos (10)</button><button class="filter" data-filter="marketing">♧ &nbsp; Marketing &amp; E-commerce</button><button class="filter" data-filter="negocios">◴ &nbsp; Negócios &amp; BI</button><button class="filter" data-filter="outras">▦ &nbsp; Outras Análises</button></div><div class="project-grid" id="projectGrid">__PROJECTS__</div></div></section></main>
<footer class="footer"><div class="container footer-content">
<div class="footer-main"><div class="footer-identity"><div class="footer-name">Júlia Castilla</div>
<div class="footer-role">Análise de Dados | Marketing Digital</div></div>
<div class="footer-links">
<a href="https://www.linkedin.com/in/juliacastilla" target="_blank" rel="noopener noreferrer" aria-label="Perfil no LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.35V9h3.414v1.561h.049c.476-.9 1.637-1.85 3.37-1.85 3.601 0 4.265 2.37 4.265 5.455v6.286zM5.337 7.433a2.062 2.062 0 1 1 0-4.124 2.062 2.062 0 0 1 0 4.124zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0z"/></svg>LinkedIn</a>
<a href="https://github.com/Jucastilla" target="_blank" rel="noopener noreferrer" aria-label="Perfil no GitHub"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56 0-.27-.01-1-.02-1.97-3.2.7-3.88-1.54-3.88-1.54-.52-1.32-1.28-1.67-1.28-1.67-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.56-.29-5.25-1.28-5.25-5.69 0-1.26.45-2.29 1.18-3.1-.12-.29-.51-1.47.11-3.05 0 0 .96-.31 3.16 1.18A11 11 0 0 1 12 6.07c.98 0 1.97.13 2.89.39 2.2-1.49 3.16-1.18 3.16-1.18.62 1.58.23 2.76.11 3.05.74.81 1.18 1.84 1.18 3.1 0 4.42-2.7 5.4-5.27 5.69.41.35.78 1.05.78 2.12 0 1.53-.01 2.76-.01 3.13 0 .31.21.68.8.56A11.51 11.51 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/></svg>GitHub</a>
<a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=juliacruz943%40gmail.com&amp;su=Contato%20pelo%20portf%C3%B3lio%20de%20J%C3%BAlia%20Castilla" target="_blank" rel="noopener noreferrer" aria-label="Enviar e-mail para Júlia pelo Gmail"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="m3.5 6 8.5 6.5L20.5 6"/></svg>E-mail</a>
</div></div>
<div class="footer-bottom">© <span id="year"></span> Júlia Castilla · Todos os direitos reservados.</div>
</div></footer>
<script>
document.getElementById('year').textContent=new Date().getFullYear();
document.querySelectorAll('.filter').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.filter').forEach(b=>b.classList.remove('active'));button.classList.add('active');const f=button.dataset.filter;document.querySelectorAll('.project-card').forEach(card=>card.classList.toggle('hidden',f!=='all'&&card.dataset.category!==f));}));
// Menu: navega dentro da página e posiciona a seção logo abaixo do cabeçalho fixo.
function goToSection(id){
  const target=document.getElementById(id);
  if(!target)return;
  const header=document.querySelector('.topbar');
  const offset=(header?header.offsetHeight:88)+4;
  const top=target.getBoundingClientRect().top+document.documentElement.scrollTop-offset;
  window.scrollTo({top:Math.max(0,top),behavior:'smooth'});
  if(window.history && window.history.replaceState){window.history.replaceState(null,'','#'+id);}
  document.querySelectorAll('.menu a').forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+id));
  document.getElementById('menu').classList.remove('open');
}
document.querySelectorAll('.menu a, .logo, .hero-copy .primary').forEach(a=>a.addEventListener('click',e=>{
  const href=a.getAttribute('href')||'';
  if(!href.startsWith('#'))return;
  e.preventDefault();
  goToSection(href.slice(1));
}));
// Ao abrir um endereço com #servicos, mostra a seção abaixo do menu.
window.addEventListener('load',()=>{const id=decodeURIComponent(location.hash.slice(1));if(id && document.getElementById(id)){setTimeout(()=>goToSection(id),80);}});
const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){const id=entry.target.id;document.querySelectorAll('.menu a').forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+id))}})},{rootMargin:'-20% 0px -60% 0px'});document.querySelectorAll('main section[id]').forEach(s=>observer.observe(s));
</script></body></html>'''
html=html.replace('__HERO__',img('hero.jpg')).replace('__ABOUT__',img('sobre.jpg')).replace('__SERVICES__',service_html).replace('__PROJECTS__',project_html)
components.html(html,height=850,scrolling=True)
