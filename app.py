"""Portfólio de Júlia Castilla — Streamlit.
Execute com: python -m streamlit run app.py
"""

from pathlib import Path
from html import escape
import base64

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

st.set_page_config(
    page_title="Portfólio | Júlia Castilla",
    page_icon=Image.open(ASSETS / "favicon.png"),
    layout="wide",
    initial_sidebar_state="collapsed",
)

# O Streamlit não deve rolar o iframe inteiro.
# A rolagem acontece dentro do próprio portfólio.
st.markdown("""
<style>
#MainMenu,
header[data-testid="stHeader"],
footer[data-testid="stFooter"] {
    display: none !important;
}

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
}

.block-container,
[data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}

[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}

[data-testid="stCustomComponentV1"] {
    height: 100dvh !important;
    overflow: hidden !important;
}

[data-testid="stCustomComponentV1"] iframe {
    position: fixed !important;
    inset: 0 !important;
    display: block !important;
    width: 100vw !important;
    height: 100dvh !important;
    border: 0 !important;
}
</style>
""", unsafe_allow_html=True)


def img(name):
    data = (ASSETS / name).read_bytes()
    return (
        "data:image/jpeg;base64,"
        + base64.b64encode(data).decode()
    )


# ==========================================
# PROJETOS
# ==========================================

projects = [
    dict(
        name="Projeto Nossa Entrega",
        desc="Análise de dados de uma iniciativa voluntária de apoio a pessoas em situação de rua, identificando padrões de participação dos voluntários e da logística de transportes, com resultados apresentados em dashboard interativo.",
        tech=["Python", "Pandas", "Plotly", "Streamlit"],
        cat="outras",
        image="nossa-entrega.jpg",
        url="https://github.com/Jucastilla/projeto-nossa-entrega",
    ),
    dict(
        name="Análise do Mercado Publicitário Audiovisual (ANCINE)",
        desc="Consolidação de 164 arquivos CSV e integração de três bases da ANCINE para analisar o mercado publicitário audiovisual, com resultados apresentados em dashboard interativo.",
        tech=["Python", "BigQuery", "Looker Studio"],
        cat="marketing",
        image="ancine.jpg",
        url="https://github.com/Jucastilla/analise-mercado-publicitario-ancine",
    ),
    dict(
        name="London Crime Analysis",
        desc="Estudo de 6 milhões de crimes em Londres para identificar áreas prioritárias e apresentar recomendações em um dashboard Power BI.",
        tech=["Python", "SQL", "BigQuery", "Power BI"],
        cat="outras",
        image="london.jpg",
        url="https://github.com/Jucastilla/london-crime-analysis",
    ),
    dict(
        name="Análise de Dados da COVID-19",
        desc="Automação de consultas e tratamento de dados da COVID-19 com Python e BigQuery, gerando bases validadas em CSV e Parquet.",
        tech=["Python", "SQL", "BigQuery"],
        cat="outras",
        image="covid.jpg",
        url="https://github.com/Jucastilla/projeto-covid-bigquery",
    ),
    dict(
        name="Análise de Engajamento do Hacker News",
        desc="Análise de 49 milhões de registros com 12 consultas SQL, identificando padrões de publicação e engajamento no Hacker News.",
        tech=["SQL", "BigQuery"],
        cat="marketing",
        image="hacker.jpg",
        url="https://github.com/Jucastilla/hacker-news-bigquery-analysis-",
    ),
    dict(
        name="Análise de Insatisfação de Clientes da Olist",
        desc="Investigação da insatisfação de clientes da Olist por meio de modelos preditivos e dashboard. A análise identificou maior insatisfação nos pedidos entregues com atraso.",
        tech=["Python", "Machine Learning", "Looker Studio"],
        cat="marketing",
        image="olist.jpg",
        url="https://github.com/Jucastilla/analise-insatisfacao-olist",
    ),
    dict(
        name="Análise Estratégica de Vendas",
        desc="Integração de seis bases comerciais no Power BI para analisar receita, custos, lucro e desempenho de vendas por produtos, regiões e representantes.",
        tech=["Power BI", "Power Query", "DAX"],
        cat="negocios",
        image="vendas.jpg",
        url="https://github.com/Jucastilla/analise-vendas-powerbi",
    ),
    dict(
        name="Análise Exploratória de E-commerce",
        desc="Análise de preços, avaliações e vendas de produtos de comércio eletrônico, identificando padrões e relações entre variáveis, com resultados apresentados em dashboard interativo.",
        tech=["Python", "Pandas", "Plotly", "Dash"],
        cat="marketing",
        image="ecommerce.jpg",
        url="https://github.com/Jucastilla/dashboard-ecommerce-",
    ),
    dict(
        name="Análise de Dados de Restaurante",
        desc="Criação de banco de dados relacional para simular a gestão de um restaurante, com consultas SQL e indicadores de pedidos, clientes e produtos.",
        tech=["MySQL", "SQL"],
        cat="negocios",
        image="restaurante.jpg",
        url="https://github.com/Jucastilla/analise-dados-restaurante-sql",
    ),
    dict(
        name="Calculadora em Python e Linux",
        desc="Desenvolvimento de calculadoras em Python e Bash, com operações matemáticas, repetição de cálculos e tratamento de erros no terminal Linux.",
        tech=["Python", "Shell Script", "Linux"],
        cat="outras",
        image="calculadora.jpg",
        url="https://github.com/Jucastilla/calculadora-python-linux",
    ),
]

# ==========================================
# SERVIÇOS
# ==========================================

services = [
    (
        "🛒",
        "Análise de Vendas",
        "Análise de faturamento, ticket médio, produtos mais vendidos e sazonalidade para identificar padrões de consumo, avaliar o desempenho comercial e orientar decisões estratégicas de vendas.",
        "blue",
    ),
    (
        "▣",
        "Análise de Sites e E-commerce",
        "Análise de tráfego, navegação e comportamento dos visitantes para identificar obstáculos na jornada de compra e oportunidades de melhoria na experiência do usuário e na conversão.",
        "purple",
    ),
    (
        "◎",
        "Análise de Redes Sociais",
        "Avaliação de métricas de alcance, engajamento e desempenho de conteúdos para identificar oportunidades de melhoria e orientar estratégias que fortaleçam a presença digital da marca.",
        "blue",
    ),
    (
        "▦",
        "Estratégia de Social Media",
        "Planejamento de conteúdo para redes sociais com foco em objetivos, público-alvo e posicionamento de marca, fortalecendo a comunicação digital.",
        "purple",
    ),
    (
        "✎",
        "Produção de Conteúdo Digital",
        "Criação de conteúdos para redes sociais com técnicas de copywriting, alinhando linguagem, identidade da marca e interesses do público para comunicar mensagens relevantes e estimular o engajamento.",
        "blue",
    ),
]

service_html = "".join(
    f"""
    <article class="service-card">
      <div class="service-icon {color}">{icon}</div>
      <h3>{escape(title)}</h3>
      <p>{escape(desc)}</p>
    </article>
    """
    for icon, title, desc, color in services
)

project_html = ""

for p in projects:
    tags = "".join(
        f"<span>{escape(t)}</span>"
        for t in p["tech"]
    )

    project_html += f"""
    <a class="project-card"
       data-category="{p['cat']}"
       href="{p['url']}"
       target="_blank"
       rel="noopener noreferrer"
       aria-label="Abrir {escape(p['name'])} no GitHub">

      <div class="project-photo">
        <img loading="lazy"
             src="{img(p['image'])}"
             alt="Ilustração do projeto {escape(p['name'])}">
      </div>

      <div class="project-body">
        <h3>{escape(p['name'])}</h3>
        <p>{escape(p['desc'])}</p>

        <div class="project-bottom">
          <div class="tags">{tags}</div>
          <span class="github-icon" aria-hidden="true">↗</span>
        </div>
      </div>
    </a>
    """


# ==========================================
# DOCUMENTO HTML
# ==========================================

html = r"""
<!doctype html>
<html lang="pt-BR">

<head>
<meta charset="utf-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1">

<title>Portfólio | Júlia Castilla</title>

<link rel="preconnect"
      href="https://fonts.googleapis.com">

<link rel="preconnect"
      href="https://fonts.gstatic.com"
      crossorigin>

<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap"
      rel="stylesheet">

<style>

/* ==========================================
   CONFIGURAÇÕES GERAIS
========================================== */

:root {
  --ink: #150F2C;
  --text: #4F4073;
  --blue: #527FA8;
  --purple: #3C2D5C;
  --lilac: #FAF8FC;
  --line: #EDEAF3;
}

* {
  box-sizing: border-box;
}

html {
  height: 100%;
  overflow: hidden;
  scroll-behavior: smooth;
}

body {
  height: 100dvh;
  margin: 0;
  padding-top: 88px;
  padding-bottom: 0;
  overflow-x: hidden;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  -webkit-overflow-scrolling: touch;
  scroll-behavior: smooth;
  scroll-padding-top: 100px;
  background: #FFFFFF;
  color: var(--ink);
  font-family: "DM Sans", sans-serif;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  font: inherit;
  cursor: pointer;
}

section {
  scroll-margin-top: 100px;
}

.container {
  width: 100%;
  max-width: 1390px;
  padding: 0 36px;
  margin: auto;
}

/* ==========================================
   MENU FIXO - DESKTOP E MOBILE
========================================== */

.topbar {
  position: fixed !important;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 88px;
  z-index: 9999;

  background: rgba(255,255,255,.98);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(8px);
}

.nav-wrap {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  gap: 24px;
}

.logo {
  font-family: "Outfit", sans-serif;
  font-size: 35px;
  font-weight: 800;
  letter-spacing: -2px;
  white-space: nowrap;
  color: #4F4073;
}


.menu {
  display: flex;
  align-items: center;
  gap: 42px;
}

.menu a {
  position: relative;
  padding: 12px 0;
  color: #3C2D5C;
  font-size: 18px;
}

.menu a.active,
.menu a:hover {
  color: var(--blue);
}

.menu a.active::after,
.menu a:hover::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 5px;
  height: 2px;
  background: var(--blue);
}

.cta,
.primary {
  display: inline-block;
  padding: 16px 26px;
  border-radius: 11px;
  color: #FFFFFF;
  font-weight: 700;
  white-space: nowrap;

  background: linear-gradient(
    105deg,
    #426D97,
    #567CA3
  );

  box-shadow: 0 7px 22px #426D971A;
}

.cta:hover,
.primary:hover {
  filter: brightness(1.08);
}

.hamburger {
  display: none;
  border: 0;
  background: transparent;
  color: var(--ink);
  font-size: 27px;
}

/* ==========================================
   SEÇÃO INICIAL
========================================== */

.hero {
  min-height: 710px;
  display: grid;
  grid-template-columns: 49% 51%;
  align-items: center;
  gap: 12px;
  padding-top: 34px;
  padding-bottom: 50px;
}

.hero-copy h1 {
  font-family: "Outfit", sans-serif;
  font-size: clamp(34px,3.45vw,56px);
  line-height: 1.13;
  font-weight: 800;
  letter-spacing: -2.6px;
  margin: 0 0 55px;
}

.hero-line {
  white-space: nowrap;
}

.highlight {
  color: transparent;
  background: linear-gradient(
    105deg,
    #376B9A,
    #5A86AD
  );
  background-clip: text;
  -webkit-background-clip: text;
  white-space: nowrap;
}

.hero .primary {
  font-size: 17px;
  padding: 19px 26px;
}

.social {
  display: flex;
  gap: 16px;
  margin-top: 33px;
}

.social a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 13px;
  background: #F0EDF6;
  color: #3C2D5C;
  font-size: 20px;
  font-weight: 800;
}

.social a:hover {
  background: #E4DCEC;
}

.hero-art {
  display: flex;
  justify-content: flex-end;
}

.hero-art img {
  display: block;
  width: 100%;
  max-width: 700px;
  height: 590px;
  object-fit: cover;
  object-position: center;
  border-radius: 80px 40px 60px 85px;
  mask-image: linear-gradient(
    to right,
    transparent 0%,
    black 12%,
    black 100%
  );
}

/* ==========================================
   SOBRE MIM
========================================== */

.about {
  background: #FAF8FC;
  padding: 100px 0 112px;
}

.about-layout {
  display: grid;
  grid-template-columns: 48% 52%;
  gap: 64px;
  align-items: center;
}

.about-visual img {
  display: block;
  width: 100%;
  max-width: 610px;
  border-radius: 24px;
}

.about-text {
  max-width: 620px;
}

.about-heading {
  font-family: "Outfit", sans-serif;
  font-size: 32px;
  font-weight: 800;
  line-height: 1.25;
  letter-spacing: -.8px;
  margin: 0 0 26px;
  color: #4F4073;
}

.about-heading span {
  color: transparent;
  background: linear-gradient(
    105deg,
    #3C2D5C,
    #76548D
  );
  background-clip: text;
  -webkit-background-clip: text;
}

.about-text p {
  color: #4F4073;
  font-size: 17px;
  line-height: 1.76;
  margin: 22px 0;
}

/* ==========================================
   SERVIÇOS
========================================== */

.services {
  background: #FFFFFF;
  padding: 95px 0 108px;
}

.section-heading {
  text-align: center;
  margin-bottom: 38px;
}

.section-heading h2 {
  font-family: "Outfit", sans-serif;
  font-size: 36px;
  font-weight: 800;
  margin: 0;
}

.service-grid {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: 20px;
  max-width: 1050px;
  margin: auto;
}

.service-card {
  padding: 28px 27px 30px;
  min-height: 220px;
  background: #FFFFFF;
  border-radius: 22px;
  box-shadow: 0 8px 26px #150F2C0B;
}

.service-grid > .service-card:last-child {
  grid-column: 1 / -1;
  justify-self: center;
  width: calc((100% - 20px)/2);
}

.service-icon {
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 15px;
  font-size: 26px;
}

.service-icon.blue {
  background: #E8F3FA;
  color: #527FA8;
}

.service-icon.purple {
  background: #F0EAF7;
  color: #795DA2;
}

.service-card h3 {
  font-size: 19px;
  margin: 22px 0 15px;
}

.service-card p {
  color: #4F4073;
  font-size: 15.5px;
  line-height: 1.68;
  margin: 0;
}

/* ==========================================
   PROJETOS
========================================== */

.projects {
  background: #FAF8FC;
  padding: 86px 0 145px;
}

.filters {
  display: flex;
  gap: 14px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 26px;
}

.filter {
  min-width: 170px;
  border: 0;
  border-radius: 11px;
  padding: 14px 20px;
  background: #EEEAF4;
  color: #3C2D5C;
  font-size: 18px;
}

.filter.active {
  background: linear-gradient(
    105deg,
    #3C2D5C,
    #665080
  );
  color: #FFFFFF;
}

.filter:hover:not(.active) {
  background: #E8F3FA;
  color: #376B9A;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(4,minmax(0,1fr));
  gap: 20px;
}

.project-card {
  display: flex;
  flex-direction: column;
  min-width: 0;
  overflow: hidden;
  border: 7px solid #FFFFFF;
  border-radius: 19px;
  background: #FFFFFF;
  box-shadow: 0 8px 26px #150F2C0B;
  transition: transform .2s;
}

.project-card:hover {
  transform: translateY(-5px);
}

.project-card.hidden {
  display: none;
}

.project-photo {
  width: 100%;
  height: 150px;
  overflow: hidden;
  border-radius: 12px;
}

.project-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-body {
  display: flex;
  flex-direction: column;
  flex: 1;
  padding: 13px 9px 14px;
}

.project-body h3 {
  font-size: 16px;
  line-height: 1.25;
  margin: 0 0 8px;
  font-weight: 800;
}

.project-body p {
  color: #4F4073;
  font-size: 12.5px;
  line-height: 1.55;
  margin: 0 0 15px;
  flex: 1;
}

.project-bottom {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 6px;
}

.tags {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
}

.tags span {
  padding: 5px 7px;
  border-radius: 5px;
  background: #F0EAF5;
  color: #4F4073;
  font-size: 11px;
}

.github-icon {
  font-size: 24px;
  color: #150F2C;
}

/* ==========================================
   TEXTO JUSTIFICADO
========================================== */

.about-text p,
.service-card p,
.project-body p {
  text-align: justify;
  text-align-last: left;
  hyphens: none;
  -webkit-hyphens: none;
  word-break: normal;
  overflow-wrap: normal;
}

/* ==========================================
   TABLETS
========================================== */

@media (min-width:761px) and (max-width:1100px) {

  .container {
    padding-inline: 28px;
  }

  .logo {
    font-size: 27px;
  }

  .menu {
    gap: 17px;
  }

  .menu a {
    font-size: 15px;
  }

  .cta {
    padding: 13px 15px;
    font-size: 14px;
  }

  .hero {
    grid-template-columns: 1fr 1fr;
    min-height: 560px;
    gap: 22px;
  }

  .hero-copy h1 {
    font-size: clamp(27px,3.3vw,39px);
    letter-spacing: -1.4px;
  }

  .hero-art img {
    height: 440px;
  }

  .about-layout {
    grid-template-columns: 44% 56%;
    gap: 22px;
  }

  .project-grid {
    grid-template-columns: repeat(2,minmax(0,1fr));
  }

  .project-photo {
    height: 190px;
  }
}

/* ==========================================
   CELULARES
========================================== */

@media (max-width:760px) {

  html {
    scroll-padding-top: 84px;
  }

  body {
    padding-top: 72px;
  }

  section {
    scroll-margin-top: 84px;
  }

  .container {
    padding-inline: 20px;
  }

  .topbar {
    height: 72px;
  }

  .nav-wrap {
    gap: 12px;
  }

  .logo {
    font-size: clamp(23px,5vw,29px);
    letter-spacing: -1.4px;
  }

  .topbar .cta {
    display: none;
  }

  .hamburger {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 44px;
    height: 44px;
    border-radius: 10px;
  }

  /* Dropdown compacto à direita */
  .menu {
    display: none;
    position: absolute;
    top: calc(100% + 8px);
    right: 0;
    left: auto;
    width: min(205px,calc(100vw - 36px));
    max-height: calc(100dvh - 90px);
    overflow-y: auto;
    padding: 8px;
    background: #FFFFFF;
    border: 1px solid #EEEAF5;
    border-radius: 14px;
    box-shadow: 0 12px 30px #3C2D5C24;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    z-index: 10000;
  }

  .menu.open {
    display: flex;
  }

  .menu a {
    display: block;
    width: 100%;
    padding: 11px 14px;
    border-radius: 9px;
    text-align: left;
    font-size: 16px;
  }

  .menu a:hover,
  .menu a.active {
    background: #F3F7FB;
    color: #527FA8;
  }

  .menu a::after {
    display: none;
  }

  /* Imagem antes do título */
  .hero {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 22px;
    min-height: 0;
    padding-top: 45px;
    padding-bottom: 55px;
  }

  .hero-art {
    order: -1;
    justify-content: center;
    margin: 0;
  }

  .hero-copy {
    order: 1;
  }

  .hero-art img {
    width: 100%;
    height: auto;
    max-height: 420px;
    aspect-ratio: 1.3;
    object-fit: cover;
    border-radius: 35px;
    mask-image: none;
  }

  .hero-copy h1 {
    font-size: clamp(27px,5.9vw,43px);
    line-height: 1.18;
    letter-spacing: -1.3px;
    margin-bottom: 26px;
  }

  .hero-line,
  .highlight {
    white-space: normal;
  }

  .hero .primary {
    font-size: 15px;
    padding: 15px 18px;
  }

  .about {
    padding: 55px 0;
  }

  .about-layout {
    grid-template-columns: 1fr;
    gap: 28px;
  }

  .about-visual img {
    max-width: 580px;
    margin-inline: auto;
  }

  .about-text {
    max-width: none;
  }

  .about-text .about-heading {
    text-align: center;
  }

  .about-text p {
    font-size: 15px;
    line-height: 1.7;
  }

  .services,
  .projects {
    padding: 58px 0 95px;
  }

  .service-grid {
    grid-template-columns: 1fr;
  }

  .service-card {
    min-height: 0;
  }

  .service-grid > .service-card:last-child {
    grid-column: auto;
    width: 100%;
  }

  .project-grid {
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 14px;
  }

  .project-photo {
    height: 160px;
  }

  .project-body p {
    font-size: 13px;
  }

  .filters {
    gap: 8px;
  }

  .filter {
    flex: 1 1 auto;
    min-width: 0;
    padding: 12px 14px;
    font-size: 14px;
    white-space: normal;
  }
}

@media (max-width:520px) {

  .container {
    padding-inline: 18px;
  }

  .hero-copy h1 {
    font-size: clamp(25px,6.2vw,34px);
  }

  .hero-art img {
    max-height: 330px;
  }

  .project-grid {
    grid-template-columns: 1fr;
  }

  .project-photo {
    height: 190px;
  }

  .project-body h3 {
    font-size: 16px;
  }

  .project-body p {
    font-size: 14px;
  }

  .filter {
    flex: 1 1 calc(50% - 8px);
  }

  .service-card {
    padding: 23px;
  }
}


/* Estrutura unica de rolagem: menu fora da area rolavel */
html, body {
  width: 100%;
  height: 100%;
  min-height: 0;
  margin: 0;
  padding: 0;
  overflow: hidden;
}
body {
  display: flex;
  flex-direction: column;
}
.topbar {
  position: relative !important;
  top: auto;
  left: auto;
  right: auto;
  flex: 0 0 88px;
  height: 88px;
  width: 100%;
}
.page-scroll {
  flex: 1 1 auto;
  min-height: 0;
  width: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  scroll-behavior: smooth;
  scroll-padding-top: 16px;
  -webkit-overflow-scrolling: touch;
}
/* Espaço real DENTRO do contêiner rolável, após o último projeto.
   Evita que a barra inferior do navegador cubra o fim do último cartão. */
.mobile-scroll-end { height: 0; flex-shrink: 0; }
@media (max-width: 760px) {
  .mobile-scroll-end {
    height: calc(280px + env(safe-area-inset-bottom, 0px));
    min-height: 280px;
    pointer-events: none;
  }
}
.page-scroll section { scroll-margin-top: 16px; }
@media (max-width: 760px) {
  .topbar { flex-basis: 72px; height: 72px; }
  .page-scroll { scroll-padding-top: 12px; }
  .page-scroll section { scroll-margin-top: 12px; }
  }
</style>
</head>

<body>

<!-- ==========================================
     MENU DE NAVEGAÇÃO
========================================== -->

<header class="topbar">
  <div class="container nav-wrap">

    <a class="logo"
       href="#inicio"
       aria-label="Júlia Castilla, início">
      Júlia Castilla
    </a>

    <nav class="menu" id="menu">
      <a href="#inicio" class="active">Início</a>
      <a href="#sobre">Sobre</a>
      <a href="#servicos">Serviços</a>
      <a href="#projetos">Projetos</a>
    </nav>

    <a class="cta"
       href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=juliacruz943%40gmail.com&amp;su=Contato%20pelo%20portf%C3%B3lio%20de%20J%C3%BAlia%20Castilla"
       target="_blank"
       rel="noopener noreferrer">
      Vamos conversar →
    </a>

    <button
      class="hamburger"
      type="button"
      aria-label="Abrir menu"
      aria-controls="menu"
      aria-expanded="false">
      ☰
    </button>

  </div>
</header>

<div class="page-scroll" id="pageScroll">
<main>

<!-- ==========================================
     INÍCIO
========================================== -->

<section class="container hero" id="inicio">

  <div class="hero-copy">

    <h1>
      Transformando<br>
      <span class="hero-line">
        dados em
        <span class="highlight">estratégias</span>
      </span>
      <br>para o seu negócio.
    </h1>

    <a class="primary" href="#servicos">
      Conheça meus serviços →
    </a>

    <div class="social">

      <a href="https://www.linkedin.com/in/juliacastilla"
         target="_blank"
         rel="noopener noreferrer"
         aria-label="LinkedIn">in</a>

      <a href="https://github.com/Jucastilla"
         target="_blank"
         rel="noopener noreferrer"
         aria-label="GitHub">GH</a>

      <a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=juliacruz943%40gmail.com"
         target="_blank"
         rel="noopener noreferrer"
         aria-label="E-mail">✉</a>

    </div>
  </div>

  <div class="hero-art">
    <img src="__HERO__"
         alt="Retrato futurista com elementos de análise de dados">
  </div>

</section>

<!-- ==========================================
     SOBRE MIM
========================================== -->

<section class="about" id="sobre">

  <div class="container about-layout">

    <div class="about-visual">
      <img src="__ABOUT__"
           alt="Espaço de trabalho com gráficos e elementos geométricos">
    </div>

    <div class="about-text">

      <h2 class="about-heading">
        <span>Sobre mim</span>
      </h2>

      <p>
        Sou Júlia Castilla, Analista de Dados, graduada em
        Marketing Digital pela Universidade Estácio de Sá,
        com formação profissional em Análise de Dados e
        Social Media Manager pela EBAC.
      </p>

      <p>
        Minha experiência em Marketing Digital, especialmente
        com SEO, Social Media e análise de indicadores de
        desempenho, ampliou meu interesse pelo uso estratégico
        dos dados. O contato com métricas, comportamento do
        público e avaliação de resultados contribuiu para o
        desenvolvimento de uma visão analítica, que aprofundei
        por meio da formação em Análise de Dados.
      </p>

      <p>
        Desenvolvi competências em SQL, Python, Power BI,
        Google BigQuery e Looker Studio, aplicadas à preparação,
        integração, validação e visualização de dados.
        Em projetos práticos, analisei bases com aproximadamente
        6 milhões de ocorrências criminais e 49 milhões de
        registros de engajamento, além de consolidar 164
        arquivos CSV para estudar o mercado publicitário
        audiovisual brasileiro.
      </p>

      <p>
        Hoje, reúno conhecimentos técnicos em Análise de Dados
        e experiência em Marketing Digital para identificar
        padrões, desenvolver indicadores e dashboards e
        transformar informações em análises que apoiem
        decisões estratégicas.
      </p>

    </div>
  </div>

</section>

<!-- ==========================================
     SERVIÇOS
========================================== -->

<section class="services" id="servicos">

  <div class="container">

    <div class="section-heading">
      <h2 class="about-heading">
        <span>Meus serviços</span>
      </h2>
    </div>

    <div class="service-grid">
      __SERVICES__
    </div>

  </div>
</section>

<!-- ==========================================
     PROJETOS
========================================== -->

<section class="projects" id="projetos">

  <div class="container">

    <div class="section-heading">
      <h2 class="about-heading">
        <span>Projetos</span>
      </h2>
    </div>

    <div class="filters"
         role="group"
         aria-label="Filtrar projetos">

      <button class="filter active"
              data-filter="all">
        Todos (10)
      </button>

      <button class="filter"
              data-filter="marketing">
        Marketing &amp; E-commerce
      </button>

      <button class="filter"
              data-filter="negocios">
        Negócios &amp; BI
      </button>

      <button class="filter"
              data-filter="outras">
        Outras Análises
      </button>

    </div>

    <div class="project-grid" id="projectGrid">
      __PROJECTS__
    </div>

  </div>
</section>

</main>

<!-- Reserva de rolagem para o ultimo cartao no Safari/Brave mobile. -->
<div class="mobile-scroll-end" aria-hidden="true"></div>

</div><!-- fim da area rolavel -->

<!-- ==========================================
     JAVASCRIPT
========================================== -->

<script>

const menu = document.getElementById("menu");
const menuButton = document.querySelector(".hamburger");

// Abre e fecha o menu mobile.
function closeMenu() {
  menu.classList.remove("open");
  menuButton.setAttribute("aria-expanded", "false");
  menuButton.setAttribute("aria-label", "Abrir menu");
}

menuButton.addEventListener("click", () => {
  const isOpen = menu.classList.toggle("open");

  menuButton.setAttribute(
    "aria-expanded",
    String(isOpen)
  );

  menuButton.setAttribute(
    "aria-label",
    isOpen ? "Fechar menu" : "Abrir menu"
  );
});

// Navegação entre seções.
function goToSection(id) {
  const target = document.getElementById(id);

  if (!target) {
    return;
  }

  const scroller = document.getElementById("pageScroll");
  const top = target.getBoundingClientRect().top -
              scroller.getBoundingClientRect().top +
              scroller.scrollTop - 8;

  document.getElementById("pageScroll").scrollTo({
    top: Math.max(0, top),
    behavior: "smooth"
  });

  if (window.history && window.history.replaceState) {
    window.history.replaceState(null, "", "#" + id);
  }

  document.querySelectorAll(".menu a").forEach(link => {
    link.classList.toggle(
      "active",
      link.getAttribute("href") === "#" + id
    );
  });

  closeMenu();
}

// Links de navegação.
document.querySelectorAll(
  ".menu a, .logo, .hero-copy .primary"
).forEach(link => {

  link.addEventListener("click", event => {
    const href = link.getAttribute("href") || "";

    if (!href.startsWith("#")) {
      return;
    }

    event.preventDefault();
    goToSection(href.slice(1));
  });

});

// Fecha dropdown ao clicar fora.
document.addEventListener("click", event => {
  if (
    !menu.contains(event.target) &&
    !menuButton.contains(event.target)
  ) {
    closeMenu();
  }
});

// Fecha dropdown com Escape.
document.addEventListener("keydown", event => {
  if (event.key === "Escape") {
    closeMenu();
  }
});

// Filtros dos projetos.
document.querySelectorAll(".filter").forEach(button => {

  button.addEventListener("click", () => {

    document.querySelectorAll(".filter").forEach(item => {
      item.classList.remove("active");
    });

    button.classList.add("active");

    const selected = button.dataset.filter;

    document.querySelectorAll(".project-card").forEach(card => {
      card.classList.toggle(
        "hidden",
        selected !== "all" &&
        card.dataset.category !== selected
      );
    });

  });

});

// Seção ativa durante a rolagem.
const observer = new IntersectionObserver(entries => {

  entries.forEach(entry => {

    if (entry.isIntersecting) {
      document.querySelectorAll(".menu a").forEach(link => {
        link.classList.toggle(
          "active",
          link.getAttribute("href") ===
          "#" + entry.target.id
        );
      });
    }

  });

}, {
  root: document.getElementById("pageScroll"),
  rootMargin: "-20% 0px -60% 0px"
});

document.querySelectorAll("main section[id]").forEach(section => {
  observer.observe(section);
});

// Respeita âncoras na abertura da página.
window.addEventListener("load", () => {

  const id = decodeURIComponent(location.hash.slice(1));

  if (id && document.getElementById(id)) {
    setTimeout(() => goToSection(id), 80);
  }

});

</script>

</body>
</html>
"""

# ==========================================
# MONTAGEM FINAL
# ==========================================

html = (
    html
    .replace("__HERO__", img("hero.jpg"))
    .replace("__ABOUT__", img("sobre.jpg"))
    .replace("__SERVICES__", service_html)
    .replace("__PROJECTS__", project_html)
)

components.html(
    html,
    height=850,
    scrolling=False
)
