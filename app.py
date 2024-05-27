import streamlit as st
from streamlit_option_menu import option_menu

# Define a cor de fundo preta e letras brancas usando CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
    }
    .subtitle {
        font-size: 30px;
        margin-bottom: 10px;
    }
    .university {
        font-size: 20px;
        margin-bottom: 50px;
    }
    .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .text {
        flex: 1;
    }
    .container img {
        margin-left: 60px;
        width: 500px;  /* Aumenta o tamanho da imagem */
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir a imagem ao lado das informações
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<div class="text"><div class="title">Nilton Sainz</div><div class="subtitle">Cientista Político</div><div class="university">Universidade Federal do Paraná</div></div>', unsafe_allow_html=True)
with col2:
    st.image("image.png", use_column_width=True)

# Barra de navegação com opções
selected = option_menu(
    menu_title=None,  # Menu sem título
    options=["Apresentação", "Projetos", "Produção Acadêmica", "Contato"],  # Opções de navegação
    icons=["person", "briefcase", "book", "envelope"],  # Ícones para cada opção
    menu_icon="cast",  # Ícone do menu
    default_index=0,  # Índice padrão
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "black"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#333"},
        "nav-link-selected": {"background-color": "#444"},
    }
)

if selected == "Apresentação":
    st.markdown("""
    Me chamo Nilton Garcia Sainz, tenho 27 anos, nascido em Rio Grande, no extremo sul do Rio Grande do Sul.

    Atualmente, faço doutorado em Ciência Política no Programa de Pós-Graduação em Ciência Política da Universidade
    Federal do Paraná, onde também sou pós-graduando em Data Science & Big Data, curso oferecido pelos Departamentos
    de Estatística e Informática da UFPR. Realizo graduação em Direito na Pontifícia Universidade Católica do Paraná,
    onde também atuo como pesquisador. Sou graduado em Ciências Sociais e mestre em Ciência Política pela Universidade
    Federal de Pelotas.

    Sou pesquisador vinculado ao [Instituto Nacional de Ciência Tecnologia - Representação e Legitimidade Democrática (INCT-ReDem)](https://redem.tec.br/)
    e ao [Núcleo de Pesquisa em Políticas Públicas e Desenvolvimento Humano da PUCPR (NUPED)](https://www.nuped.com.br/).
    
    Meus interesses de pesquisa são elites parlamentares, carreiras políticas, eleições e poder Legislativo 
    e metodologia de pesquisa em Ciência Política e Sociais. Também possuo interesse nas áreas de regulação de novas técnicas
    e transformação da administração pública digital.

    Atuo como pesquisador e analista de dados no Observatório do Controle, onde atualmente estou como Diretor de pesquisa. Também presto
    assessoria e consultoria em pesquisas científicas.
    """)
elif selected == "Projetos":
    st.write("Aqui estão os meus projetos:")
    projects = [
        "Projeto 1: Descrição do projeto 1.",
        "Projeto 2: Descrição do projeto 2.",
        "Projeto 3: Descrição do projeto 3.",
    ]
    for project in projects:
        st.write(project)
elif selected == "Produção Acadêmica":
    st.write("Aqui está a minha produção acadêmica:")
    production = [
        "Produção 1: Descrição da produção 1.",
        "Produção 2: Descrição da produção 2.",
        "Produção 3: Descrição da produção 3.",
    ]
    for item in production:
        st.write(item)
elif selected == "Contato":
    st.write("Entre em contato comigo através das plataformas abaixo:")
    st.write("- [LinkedIn](https://www.linkedin.com/in/nilton-sainz/)")
    st.write("- [GitHub](https://github.com/niltonsainz)")
    st.write("- [E-mail](mailto:sainznilton@gmail.com)")
    st.write("- [Lattes](http://lattes.cnpq.br/7733003139844460)")
