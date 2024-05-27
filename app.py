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
    .container .text {
        flex: 1;
    }
    .container img {
        margin-left: 20px;
        width: 300px;  /* Aumenta o tamanho da imagem */
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conteúdo da página inicial
st.markdown(
    '''
    <div class="container">
        <div class="text">
            <div class="title">Nilton Sainz</div>
            <div class="subtitle">Cientista Político</div>
            <div class="university">Universidade Federal do Paraná</div>
        </div>
        <img src="Foto_NiltonSainz.png">
    </div>
    ''',
    unsafe_allow_html=True
)

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

# Conteúdo das abas
if selected == "Apresentação":
    st.write("Bem-vindo à página de apresentação!")
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
