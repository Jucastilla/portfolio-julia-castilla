# Portfólio | Júlia Castilla

Portfólio profissional desenvolvido com Python e Streamlit para apresentar minha trajetória, meus serviços e meus projetos nas áreas de **Análise de Dados, Business Intelligence e Marketing Digital**.

**[Acessar meu portfólio online](https://julia-castilla-portfolio.streamlit.app/)**

## Contexto

Sou Júlia Castilla, Analista de Dados, graduada em Marketing Digital pela Universidade Estácio de Sá, com formação profissional em Análise de Dados e Social Media Manager pela EBAC.

Minha experiência com SEO, Social Media e análise de indicadores de desempenho ampliou meu interesse pelo uso estratégico dos dados. O contato com métricas, comportamento do público e avaliação de resultados contribuiu para o desenvolvimento de uma visão analítica, aprofundada por meio da formação em Análise de Dados.

Ao longo dessa trajetória, desenvolvi projetos envolvendo preparação, integração, análise e visualização de dados. Este portfólio reúne essas experiências em uma aplicação web, organizando os projetos, as tecnologias utilizadas e os canais de contato profissional.

## Objetivo

Desenvolver um portfólio digital para apresentar minha trajetória profissional, minhas competências técnicas e os projetos realizados em diferentes áreas de aplicação da Análise de Dados.

A aplicação foi estruturada para facilitar a navegação entre os projetos, permitir a visualização por categorias e disponibilizar acesso aos respectivos repositórios no GitHub.

Também contempla a apresentação de serviços relacionados à Análise de Dados e ao Marketing Digital.

## Desenvolvimento

### 1. Estruturação da aplicação

A aplicação foi desenvolvida em Python, utilizando Streamlit para executar a interface web e HTML, CSS e JavaScript para organizar os elementos visuais e as interações.

O conteúdo foi dividido em quatro seções:

- **Início:** apresentação do portfólio, acesso aos serviços e links profissionais.
- **Sobre mim:** trajetória, formação e competências técnicas.
- **Serviços:** apresentação de cinco serviços relacionados à análise de dados e ao marketing digital.
- **Projetos:** catálogo de dez projetos com descrições, tecnologias e links para seus repositórios.

### 2. Organização dos projetos

Foram cadastrados dez projetos, distribuídos em três categorias:

| Categoria | Quantidade |
|---|---:|
| Marketing & E-commerce | 4 |
| Negócios & BI | 2 |
| Outras Análises | 4 |
| **Total** | **10** |

Os projetos apresentados são:

**Marketing & E-commerce**
- Análise do Mercado Publicitário Audiovisual (ANCINE)
- Análise de Engajamento do Hacker News
- Análise de Insatisfação de Clientes da Olist
- Análise Exploratória de E-commerce

**Negócios & BI**
- Análise Estratégica de Vendas
- Análise de Dados de Restaurante

**Outras Análises**
- Projeto Nossa Entrega
- London Crime Analysis
- Análise de Dados da COVID-19
- Calculadora em Python e Linux

Cada projeto é apresentado em um cartão contendo imagem, título, descrição, tecnologias e link para o respectivo repositório.

### 3. Implementação dos filtros

Foram implementados filtros em JavaScript para permitir a seleção de projetos por categoria.

A interface disponibiliza quatro opções:

- Todos
- Marketing & E-commerce
- Negócios & BI
- Outras Análises

Ao selecionar uma categoria, o código altera a exibição dos cartões conforme a classificação cadastrada.

### 4. Desenvolvimento da interface e responsividade

A identidade visual utiliza tons de azul, lilás e roxo, com alternância de fundos claros entre as seções.

Foram implementados:

- Navegação entre as seções da página.
- Menu de navegação adaptado para telas menores.
- Regras CSS de responsividade para diferentes larguras de tela.
- Cartões de serviços e projetos.
- Filtros interativos.
- Links para LinkedIn, GitHub e contato por e-mail.
- Imagens e favicon armazenados na pasta `assets`.

O código contém adaptações para computadores, tablets e celulares. A existência dessas regras não comprova testes de funcionamento em todos os dispositivos.

### 5. Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Organização das informações e geração do conteúdo |
| Streamlit | Execução da aplicação web |
| HTML | Estruturação da interface |
| CSS | Estilização e responsividade |
| JavaScript | Filtros e navegação interativa |
| Pillow | Carregamento do favicon |

As tecnologias apresentadas nos cartões dos projetos, como SQL, Google BigQuery, Power BI, Looker Studio, Pandas e Plotly, correspondem aos respectivos trabalhos e não necessariamente às dependências da aplicação do portfólio.

### 6. Estrutura do repositório

```text
portfolio-julia-castilla/
├── app.py
├── requirements.txt
├── README.md
└── assets/
    ├── favicon.png
    ├── hero.jpg
    ├── sobre.jpg
    ├── ancine.jpg
    ├── hacker.jpg
    ├── olist.jpg
    ├── ecommerce.jpg
    ├── vendas.jpg
    ├── restaurante.jpg
    ├── nossa-entrega.jpg
    ├── london.jpg
    ├── covid.jpg
    └── calculadora.jpg
```

### 7. Execução local

Para executar o portfólio localmente, é necessário ter o Python instalado.

Clone o repositório:

```bash
git clone https://github.com/Jucastilla/portfolio-julia-castilla.git
```

Acesse a pasta do projeto:

```bash
cd portfolio-julia-castilla
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Inicie a aplicação:

```bash
python -m streamlit run app.py
```

### 8. Publicação online

O projeto foi configurado para implantação no Streamlit Community Cloud, utilizando:

- Repositório: `Jucastilla/portfolio-julia-castilla`
- Branch: `main`
- Arquivo principal: `app.py`
- Dependências: `requirements.txt`

O processo de implantação foi iniciado na plataforma. O endereço público poderá ser acrescentado após a confirmação de que a aplicação está acessível.

## Resultados

O desenvolvimento resultou no código de uma aplicação de portfólio que reúne:

- **4 seções principais** de apresentação e navegação.
- **5 serviços profissionais** relacionados à análise de dados e ao marketing digital.
- **10 projetos** organizados em três categorias.
- **4 opções de filtragem** para os projetos.
- Cartões com descrições, tecnologias e links para os repositórios.
- Navegação entre seções e acesso aos canais profissionais.
- Regras de responsividade para diferentes tamanhos de tela.

O portfólio reúne projetos que abordam temas como mercado publicitário audiovisual, engajamento digital, comportamento de clientes, vendas, dados criminais e dados da COVID-19.

As informações e os resultados específicos de cada análise devem ser consultados nos respectivos repositórios.

## Habilidades Demonstradas

- Desenvolvimento de aplicações web com Python e Streamlit.
- Estruturação de interfaces com HTML.
- Estilização e implementação de layouts responsivos com CSS.
- Implementação de filtros e interações com JavaScript.
- Organização e apresentação de projetos técnicos.
- Estruturação de conteúdo para comunicação profissional.
- Documentação e organização de repositórios no GitHub.

---

## Contato

**Júlia Castilla**  
Análise de Dados | Marketing Digital

[Portfólio online](https://julia-castilla-portfolio.streamlit.app/)  
[LinkedIn](https://www.linkedin.com/in/juliacastilla)  
[GitHub](https://github.com/Jucastilla)  
[E-mail](mailto:juliacruz943@gmail.com)
