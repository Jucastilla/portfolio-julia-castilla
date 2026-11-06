
from pathlib import Path
import base64
from html import escape

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


# ==========================================
# CONFIGURAÇÃO
# ==========================================

ROOT = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Portfólio | Júlia Castilla",
    page_icon=Image.open(ROOT / "assets" / "favicon.png"),
    layout="wide",
    initial_sidebar_state="collapsed",
)

# O portfólio rola dentro do iframe.
# Isso permite manter o cabeçalho sempre visível.
st.markdown("""
<style>
#MainMenu, header, footer {
    display: none !important;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    overflow: hidden !important;
    background: white;
}
[data-testid="stCustomComponentV1"] {
    height: 100dvh !important;
    overflow: hidden !important;
}
[data-testid="stCustomComponentV1"] iframe {
    display: block;
    width: 100% !important;
    height: 100dvh !important;
    border: 0 !important;
}
</style>
""", unsafe_allow_html=True)


def image(name):
    suffix = "png" if name.endswith(".png") else "jpeg"
    data = (ROOT / "assets" / name).read_bytes()
    return (
        f"data:image/{suffix};base64,"
        + base64.b64encode(data).decode()
    )


# ==========================================
# PROJETOS
# ==========================================

projects = [
    (
        "Projeto Nossa Entrega",
        "Análise de dados de uma iniciativa voluntária de apoio a pessoas em situação de rua, identificando padrões de participação dos voluntários e da logística de transportes, com resultados apresentados em dashboard interativo.",
        "Python, Pandas, Plotly, Streamlit",
        "outras",
        "nossa-entrega.jpg",
        "projeto-nossa-entrega",
    ),
    (
        "Análise do Mercado Publicitário Audiovisual (ANCINE)",
        "Consolidação de 164 arquivos CSV e integração de três bases da ANCINE para analisar o mercado publicitário audiovisual, com resultados apresentados em dashboard interativo.",
        "Python, BigQuery, Looker Studio",
        "marketing",
        "ancine.jpg",
        "analise-mercado-publicitario-ancine",
    ),
    (
        "London Crime Analysis",
        "Estudo de 6 milhões de crimes em Londres para identificar áreas prioritárias e apresentar recomendações em um dashboard Power BI.",
        "Python, SQL, BigQuery, Power BI",
        "outras",
        "london.jpg",
        "london-crime-analysis",
    ),
    (
        "Análise de Dados da COVID-19",
        "Automação de consultas e tratamento de dados da COVID-19 com Python e BigQuery, gerando bases validadas em CSV e Parquet.",
        "Python, SQL, BigQuery",
        "outras",
        "covid.jpg",
        "projeto-covid-bigquery",
    ),
    (
        "Análise de Engajamento do Hacker News",
        "Análise de 49 milhões de registros com 12 consultas SQL, identificando padrões de publicação e engajamento no Hacker News.",
        "SQL, BigQuery",
        "marketing",
        "hacker.jpg",
        "hacker-news-bigquery-analysis-",
    ),
    (
        "Análise de Insatisfação de Clientes da Olist",
        "Investigação da insatisfação de clientes da Olist por meio de modelos preditivos e dashboard. A análise identificou maior insatisfação nos pedidos entregues com atraso.",
        "Python, Machine Learning, Looker Studio",
        "marketing",
        "olist.jpg",
        "analise-insatisfacao-olist",
    ),
    (
        "Análise Estratégica de Vendas",
        "Integração de seis bases comerciais no Power BI para analisar receita, custos, lucro e desempenho de vendas por produtos, regiões e representantes.",
        "Power BI, Power Query, DAX",
        "negocios",
        "vendas.jpg",
        "analise-vendas-powerbi",
    ),
    (
        "Análise Exploratória de E-commerce",
        "Análise de preços, avaliações e vendas de produtos de comércio eletrônico, identificando padrões e relações entre variáveis, com resultados apresentados em dashboard interativo.",
        "Python, Pandas, Plotly, Dash",
        "marketing",
        "ecommerce.jpg",
        "dashboard-ecommerce-",
    ),
    (
        "Análise de Dados de Restaurante",
        "Criação de banco de dados relacional para simular a gestão de um restaurante, com consultas SQL e indicadores de pedidos, clientes e produtos.",
        "MySQL, SQL",
        "negocios",
        "restaurante.jpg",
        "analise-dados-restaurante-sql",
    ),
    (
        "Calculadora em Python e Linux",
        "Desenvolvimento de calculadoras em Python e Bash, com operações matemáticas, repetição de cálculos e tratamento de erros no terminal Linux.",
        "Python, Shell Script, Linux",
        "outras",
        "calculadora.jpg",
        "calculadora-python-linux",
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
    ),
    (
        "▣",
        "Análise de Sites e E-commerce",
        "Análise de tráfego, navegação e comportamento dos visitantes para identificar obstáculos na jornada de compra e oportunidades de melhoria na experiência do usuário e na conversão.",
    ),
    (
        "◎",
        "Análise de Redes Sociais",
        "Avaliação de métricas de alcance, engajamento e desempenho de conteúdos para identificar oportunidades de melhoria e orientar estratégias que fortaleçam a presença digital da marca.",
    ),
    (
        "▦",
        "Estratégia de Social Media",
        "Planejamento de conteúdo para redes sociais com foco em objetivos, público-alvo e posicionamento de marca, fortalecendo a comunicação digital.",
    ),
    (
        "✎",
        "Produção de Conteúdo Digital",
        "Criação de conteúdos para redes sociais com técnicas de copywriting, alinhando linguagem, identidade da marca e interesses do público para comunicar mensagens relevantes e estimular o engajamento.",
    ),
]


service_cards = "".join(
    f"""
    <article class="service-card">
        <div class="service-icon">{icon}</div>
        <h3>{escape(title)}</h3>
        <p>{escape(desc)}</p>
    </article>
    """
    for icon, title, desc in services
)


project_cards = ""

for name, desc, tech, cat, filename, repo in projects:
    tags = "".join(
        f"<span>{escape(t.strip())}</span>"
        for t in tech.split(",")
    )

    project_cards += f"""
    <a class="project-card"
       data-category="{cat}"
       href="https://github.com/Jucastilla/{repo}"
       target="_blank"
       rel="noopener noreferrer">

        <img loading="lazy"
             src="{image(filename)}"
             alt="Projeto {escape(name)}">

        <div class="project-body">
            <h3>{escape(name)}</h3>
            <p>{escape(desc)}</p>

            <div class="project-bottom">
                <div class="tags">{tags}</div>
                <span class="github-icon" aria-hidden="true">↗</span>
            </div>
        </div>
    </a>
    """


# ==========================================
# HTML COMPLETO
# ==========================================

html = r"""
<!doctype html>
<html lang="pt-BR">

<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Portfólio | Júlia Castilla</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>

:root {
    --ink: #150F2C;
    --text: #4F4073;
    --blue: #527FA8;
    --purple: #3C2D5C;
    --lilac: #FAF8FC;
}

* {
    box-sizing: border-box;
}

html {
    height: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    scroll-behavior: smooth;
    scroll-padding-top: 90px;
}

body {
    margin: 0;
    font-family: "DM Sans", sans-serif;
    color: var(--ink);
    background: white;
    overflow-x: hidden;
}

a {
    text-decoration: none;
    color: inherit;
}

button {
    font: inherit;
    cursor: pointer;
}

section {
    scroll-margin-top: 90px;
}

.container {
    max-width: 1390px;
    padding: 0 36px;
    margin: auto;
    width: 100%;
}

/* ========================================
   CABEÇALHO FIXO NA ROLAGEM
======================================== */

.topbar {
    height: 88px;
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(255,255,255,.98);
    border-bottom: 1px solid #EDEAF3;
    backdrop-filter: blur(8px);
}

.nav-wrap {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    position: relative;
}

.logo {
    font-family: Outfit, sans-serif;
    font-size: 35px;
    font-weight: 800;
    letter-spacing: -2px;
    white-space: nowrap;
    color: #4F4073;
}

.logo-u {
    position: relative;
}

.logo-u:before {
    content: "";
    position: absolute;
    left: 25%;
    top: 15%;
    width: 22%;
    height: 15%;
    background: linear-gradient(120deg,#92CDED,#B382CD);
    border-radius: 100% 0 100% 0;
    transform: rotate(-32deg);
}

.menu {
    display: flex;
    align-items: center;
    gap: 40px;
}

.menu a {
    font-size: 18px;
    color: #3C2D5C;
    padding: 12px 0;
    position: relative;
}

.menu a.active,
.menu a:hover {
    color: var(--blue);
}

.menu a.active:after,
.menu a:hover:after {
    content: "";
    position: absolute;
    height: 2px;
    background: var(--blue);
    bottom: 5px;
    left: 0;
    right: 0;
}

.cta,
.primary {
    display: inline-block;
    background: linear-gradient(105deg,#426D97,#567CA3);
    color: white;
    border-radius: 11px;
    padding: 16px 26px;
    font-weight: 700;
    white-space: nowrap;
}

.cta:hover,
.primary:hover {
    filter: brightness(1.08);
}

.hamburger {
    display: none;
    background: none;
    border: 0;
    color: var(--ink);
    font-size: 28px;
}

/* ========================================
   INÍCIO
======================================== */

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
    font: 800 clamp(34px,3.45vw,56px)/1.13 Outfit,sans-serif;
    letter-spacing: -2.6px;
    margin: 0 0 55px;
}

.hero-line {
    white-space: nowrap;
}

.highlight {
    color: #527FA8;
    background: #EAF2F8;
    border-radius: 6px;
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
    width: 48px;
    height: 48px;
    align-items: center;
    justify-content: center;
    background: #F0EDF6;
    color: #3C2D5C;
    border-radius: 13px;
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
    width: 100%;
    max-width: 700px;
    height: 590px;
    object-fit: cover;
    border-radius: 80px 40px 60px 85px;
    mask-image: linear-gradient(to right,transparent,black 12%);
}

/* ========================================
   SOBRE MIM
======================================== */

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
    width: 100%;
    max-width: 610px;
    border-radius: 24px;
    display: block;
}

.about-text {
    max-width: 620px;
}

.about-heading {
    font: 800 32px/1.25 Outfit,sans-serif;
    letter-spacing: -.8px;
    margin: 0 0 26px;
    color: #4F4073;
}

.about-text p,
.service-card p,
.project-body p {
    text-align: justify;
    text-align-last: left;
    hyphens: none;
    overflow-wrap: normal;
    word-break: normal;
}

.about-text p {
    font-size: 17px;
    line-height: 1.76;
    color: #4F4073;
    margin: 22px 0;
}

/* ========================================
   SERVIÇOS
======================================== */

.services,
.projects {
    padding: 95px 0 108px;
}

.services {
    background: #fff;
}

.projects {
    background: #FAF8FC;
}

.section-heading {
    text-align: center;
    margin-bottom: 38px;
}

.section-heading h2 {
    font: 800 36px Outfit,sans-serif;
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
    background: #fff;
    border-radius: 22px;
    min-height: 220px;
    box-shadow: 0 8px 26px #150F2C0B;
}

.service-grid > .service-card:last-child {
    grid-column: 1/-1;
    justify-self: center;
    width: calc((100% - 20px)/2);
}

.service-icon {
    width: 54px;
    height: 54px;
    border-radius: 15px;
    display: grid;
    place-items: center;
    background: #E8F3FA;
    color: #527FA8;
    font-size: 26px;
}

.service-card:nth-child(even) .service-icon {
    background: #F0EAF7;
    color: #795DA2;
}

.service-card h3 {
    font-size: 19px;
    margin: 22px 0 15px;
}

.service-card p {
    font-size: 15.5px;
    line-height: 1.68;
    color: #4F4073;
    margin: 0;
}

/* ========================================
   PROJETOS
======================================== */

.filters {
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
    margin-bottom: 26px;
}

.filter {
    border: 0;
    border-radius: 11px;
    background: #EEEAF4;
    color: #3C2D5C;
    padding: 14px 20px;
    font-size: 18px;
    min-width: 170px;
}

.filter.active {
    background: linear-gradient(105deg,#3C2D5C,#665080);
    color: white;
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
    border: 7px solid white;
    border-radius: 19px;
    overflow: hidden;
    background: white;
    box-shadow: 0 8px 26px #150F2C0B;
    transition: transform .2s;
}

.project-card:hover {
    transform: translateY(-4px);
}

.project-card.hidden {
    display: none;
}

.project-card > img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 12px;
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
}

.project-body p {
    color: #4F4073;
    font-size: 12.5px;
    line-height: 1.55;
    flex: 1;
    margin: 0 0 15px;
}

.project-bottom {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 5px;
}

.tags {
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
}

.tags span {
    font-size: 10px;
    background: #F0EAF5;
    color: #4F4073;
    padding: 5px;
    border-radius: 5px;
}

.github-icon {
    font-size: 24px;
}

/* ========================================
   RODAPÉ
======================================== */

.footer {
    padding: 28px 0 20px;
    background: white;
    border-top: 1px solid #EDEAF3;
    color: #4F4073;
}

.footer-main {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
    padding-bottom: 22px;
}

.footer-name {
    font: 700 19px Outfit,sans-serif;
}

.footer-role {
    font-size: 13px;
    margin-top: 5px;
}

.footer-links {
    display: flex;
    align-items: center;
    gap: 22px;
    flex-wrap: wrap;
    font-size: 13px;
}

.footer-links a:hover {
    color: #527FA8;
}

.footer-bottom {
    border-top: 1px solid #EDE8F3;
    padding-top: 15px;
    font-size: 12px;
    color: #6E6284;
}

/* ========================================
   TABLET
======================================== */

@media (max-width: 1100px) {
    .menu {
        gap: 20px;
    }

    .menu a {
        font-size: 15px;
    }

    .logo {
        font-size: 28px;
    }

    .project-grid {
        grid-template-columns: repeat(2,minmax(0,1fr));
    }

    .hero-copy h1 {
        font-size: clamp(30px,3.5vw,44px);
    }

    .about-layout {
        gap: 30px;
    }
}

/* ========================================
   MOBILE
======================================== */

@media (max-width: 760px) {

    html {
        scroll-padding-top: 80px;
    }

    section {
        scroll-margin-top: 80px;
    }

    .container {
        padding-inline: 20px;
    }

    .topbar {
        height: 72px;
    }

    .logo {
        font-size: 27px;
    }

    .cta {
        display: none;
    }

    .hamburger {
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 44px;
        height: 44px;
    }

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
        border: 1px solid #eeeaf5;
        border-radius: 14px;
        background: white;
        box-shadow: 0 12px 30px #3c2d5c24;
        flex-direction: column;
        gap: 0;
        z-index: 1100;
    }

    .menu.open {
        display: flex;
    }

    .menu a {
        width: 100%;
        padding: 11px 14px;
        font-size: 16px;
        border-radius: 9px;
    }

    .menu a:hover,
    .menu a.active {
        background: #f3f7fb;
    }

    .menu a:after {
        display: none;
    }

    .hero {
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 22px;
        min-height: 0;
        padding: 45px 0 55px;
    }

    .hero-art {
        order: -1;
        justify-content: center;
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
        letter-spacing: -1.3px;
        line-height: 1.18;
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
        margin: auto;
    }

    .about-text {
        max-width: none;
    }

    .about-heading {
        text-align: center;
    }

    .about-text p {
        font-size: 15px;
        line-height: 1.7;
    }

    .services,
    .projects {
        padding: 58px 0 65px;
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

    .project-card > img {
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
        font-size: 14px;
        padding: 12px;
    }

    .footer-main {
        flex-wrap: wrap;
    }
}

@media (max-width: 520px) {

    .container {
        padding-inline: 18px;
    }

    .hero-art img {
        max-height: 330px;
    }

    .project-grid {
        grid-template-columns: 1fr;
    }

    .project-card > img {
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

    .footer-main {
        flex-direction: column;
        align-items: flex-start;
    }

    .service-card {
        padding: 23px;
    }
}

</style>
</head>

<body>

<!-- ========================================
     MENU
======================================== -->

<header class="topbar">
    <div class="container nav-wrap">

        <a class="logo" href="#inicio"
           aria-label="Júlia Castilla, início">
            J<span class="logo-u">u</span>lia Castilla
        </a>

        <nav class="menu" id="menu">
            <a href="#inicio" class="active">Início</a>
            <a href="#sobre">Sobre</a>
            <a href="#servicos">Serviços</a>
            <a href="#projetos">Projetos</a>
        </nav>

        <a class="cta"
           href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=juliacruz943%40gmail.com"
           target="_blank"
           rel="noopener noreferrer">
            Vamos conversar →
        </a>

        <button
            class="hamburger"
            aria-label="Abrir menu"
            aria-expanded="false"
            aria-controls="menu"
            type="button">
            ☰
        </button>

    </div>
</header>

<main>

<!-- ========================================
     INÍCIO
======================================== -->

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

<!-- ========================================
     SOBRE MIM
======================================== -->

<section class="about" id="sobre">

    <div class="container about-layout">

        <div class="about-visual">
            <img src="__ABOUT__"
                 alt="Espaço de trabalho com gráficos e elementos geométricos">
        </div>

        <div class="about-text">

            <h2 class="about-heading">Sobre mim</h2>

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
                Google BigQuery e Looker Studio, aplicadas à
                preparação, integração, validação e visualização
                de dados. Em projetos práticos, analisei bases com
                aproximadamente 6 milhões de ocorrências criminais
                e 49 milhões de registros de engajamento, além de
                consolidar 164 arquivos CSV para estudar o mercado
                publicitário audiovisual brasileiro.
            </p>

            <p>
                Hoje, reúno conhecimentos técnicos em Análise de
                Dados e experiência em Marketing Digital para
                identificar padrões, desenvolver indicadores e
                dashboards e transformar informações em análises
                que apoiem decisões estratégicas.
            </p>

        </div>
    </div>

</section>

<!-- ========================================
     SERVIÇOS
======================================== -->

<section class="services" id="servicos">

    <div class="container">

        <div class="section-heading">
            <h2>Meus serviços</h2>
        </div>

        <div class="service-grid">
            __SERVICES__
        </div>

    </div>

</section>

<!-- ========================================
     PROJETOS
======================================== -->

<section class="projects" id="projetos">

    <div class="container">

        <div class="section-heading">
            <h2>Projetos</h2>
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

<!-- ========================================
     RODAPÉ
======================================== -->

<footer class="footer">

    <div class="container">

        <div class="footer-main">

            <div>
                <div class="footer-name">
                    Júlia Castilla
                </div>

                <div class="footer-role">
                    Análise de Dados | Marketing Digital
                </div>
            </div>

            <div class="footer-links">

                <a href="https://www.linkedin.com/in/juliacastilla"
                   target="_blank"
                   rel="noopener noreferrer">
                    LinkedIn
                </a>

                <a href="https://github.com/Jucastilla"
                   target="_blank"
                   rel="noopener noreferrer">
                    GitHub
                </a>

                <a href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=juliacruz943%40gmail.com"
                   target="_blank"
                   rel="noopener noreferrer">
                    E-mail
                </a>

            </div>

        </div>

        <div class="footer-bottom">
            © <span id="year"></span> Júlia Castilla ·
            Todos os direitos reservados.
        </div>

    </div>

</footer>

<!-- ========================================
     JAVASCRIPT
======================================== -->

<script>

const menu = document.getElementById("menu");
const menuButton = document.querySelector(".hamburger");

function closeMenu() {
    menu.classList.remove("open");

    menuButton.setAttribute("aria-expanded", "false");
    menuButton.setAttribute("aria-label", "Abrir menu");
}

menuButton.addEventListener("click", () => {
    const open = menu.classList.toggle("open");

    menuButton.setAttribute(
        "aria-expanded",
        String(open)
    );

    menuButton.setAttribute(
        "aria-label",
        open ? "Fechar menu" : "Abrir menu"
    );
});

// Fecha o menu ao clicar fora dele.
document.addEventListener("click", event => {
    if (
        !menu.contains(event.target) &&
        !menuButton.contains(event.target)
    ) {
        closeMenu();
    }
});

// Fecha o menu ao pressionar Escape.
document.addEventListener("keydown", event => {
    if (event.key === "Escape") {
        closeMenu();
    }
});

// Navegação entre as seções.
function goToSection(id) {
    const target = document.getElementById(id);

    if (!target) {
        return;
    }

    const header = document.querySelector(".topbar");
    const offset = header.offsetHeight + 8;

    const top =
        target.getBoundingClientRect().top +
        window.scrollY -
        offset;

    window.scrollTo({
        top: Math.max(0, top),
        behavior: "smooth"
    });

    document.querySelectorAll(".menu a").forEach(link => {
        link.classList.toggle(
            "active",
            link.getAttribute("href") === "#" + id
        );
    });

    closeMenu();

    history.replaceState(null, "", "#" + id);
}

// Ativa os links do menu, logo e botão.
document.querySelectorAll(
    ".menu a, .logo, .hero-copy .primary"
).forEach(link => {

    link.addEventListener("click", event => {
        const href = link.getAttribute("href");

        if (href && href.startsWith("#")) {
            event.preventDefault();
            goToSection(href.slice(1));
        }
    });

});

// Filtros dos projetos.
document.querySelectorAll(".filter").forEach(button => {

    button.addEventListener("click", () => {

        document.querySelectorAll(".filter").forEach(b => {
            b.classList.remove("active");
        });

        button.classList.add("active");

        const filter = button.dataset.filter;

        document.querySelectorAll(".project-card").forEach(card => {
            card.classList.toggle(
                "hidden",
                filter !== "all" &&
                card.dataset.category !== filter
            );
        });

    });

});

// Ano automático do rodapé.
document.getElementById("year").textContent =
    new Date().getFullYear();

// Atualiza a indicação da seção ativa.
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
    rootMargin: "-20% 0px -60% 0px"
});

document.querySelectorAll("main section[id]").forEach(section => {
    observer.observe(section);
});

// Navegação por links com âncora.
window.addEventListener("load", () => {

    const id = decodeURIComponent(
        location.hash.slice(1)
    );

    if (id && document.getElementById(id)) {
        goToSection(id);
    }

});

</script>

</body>
</html>
"""

# ==========================================
# INSERÇÃO DO CONTEÚDO DINÂMICO
# ==========================================

html = (
    html
    .replace("__HERO__", image("hero.jpg"))
    .replace("__ABOUT__", image("sobre.jpg"))
    .replace("__SERVICES__", service_cards)
    .replace("__PROJECTS__", project_cards)
)

# ==========================================
# EXIBIÇÃO DO PORTFÓLIO
# ==========================================

components.html(
    html,
    height=900,
    scrolling=True
)
