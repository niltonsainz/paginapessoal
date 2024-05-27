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
    </style>
    """,
    unsafe_allow_html=True
)

# Conteúdo da página inicial
st.markdown(
    '''
    <div class="container">
        <div>
            <div class="title">Nilton Sainz</div>
            <div class="subtitle">Cientista Político</div>
            <div class="university">Universidade Federal do Paraná</div>
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)

# Exibir a imagem usando st.image()
st.image("Foto_NiltonSainz.png", width=150)

# Barra de navegação com opções
selected = option_menu(
    menu_title=None,  # Menu sem título
    options=["Home", "Notícias", "Projetos", "Contato"],  # Opções de navegação
    icons=["house", "newspaper", "briefcase", "envelope"],  # Ícones para cada opção
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

# Conteúdo das abas
if selected == "Home":
    st.write("Bem-vindo à página inicial!")
elif selected == "Notícias":
    st.write("Aqui estão as últimas notícias:")
    # Exemplo de esteira de notícias
    news = [
        "Notícia 1: Detalhe da notícia 1.",
        "Notícia 2: Detalhe da notícia 2.",
        "Notícia 3: Detalhe da notícia 3.",
        "Notícia 4: Detalhe da notícia 4.",
    ]
    for item in news:
        st.write(item)
elif selected == "Projetos":
    st.write("Aqui estão os meus projetos:")
    projects = [
        "Projeto 1: Descrição do projeto 1.",
        "Projeto 2: Descrição do projeto 2.",
        "Projeto 3: Descrição do projeto 3.",
    ]
    for project in projects:
        st.write(project)
elif selected == "Contato":
    st.write("Entre em contato comigo através das plataformas abaixo:")
    st.write("- [LinkedIn](https://www.linkedin.com/in/seu-perfil)")
    st.write("- [GitHub](https://github.com/seu-usuario)")
    st.write("- [E-mail](sainznilton@gmail.com)")
