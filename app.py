
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
