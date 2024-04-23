import streamlit as st
from PIL import Image
import pages.page1  # Importe o módulo da página 1
import pages.page2  # Importe o módulo da página 2

# Mapeamento de nomes de página aos módulos correspondentes
pages_mapping = {
    "Página 1": pages.page1,
    "Página 2": pages.page2,
}

# Título da aplicação
st.title("Minha Aplicação Streamlit")

# Barra lateral para seleção de página
selected_page = st.sidebar.selectbox("Selecione uma página", list(pages_mapping.keys()))

# Executa a página selecionada
pages_mapping[selected_page].main()
st.set_page_config(
    page_title='Cardio Disease Prediction',
    layout='wide'
)

image= Image.open('pages/images/doencas-cardiovasculares-gTq50UO9DE.jpeg')

st.sidebar.image(image, width=350)

st.sidebar.markdown('# CARDIO DISEASE')

st.sidebar.markdown('## Sobre o Projeto')
st.sidebar.markdown("""
Este aplicativo apresenta dashboards para uma análise exploratória de dados sobre doenças cardiovasculares,
bem como um modelo de previsão da chance de ser acometido por problemas cardiovasculares. 
Explore os dashboards e preveja sua chance de desenvolver doenças cardiovasculares.
""")

st.sidebar.markdown('## Desenvolvido por Juliano Batistela Nicoletti')
st.sidebar.markdown('[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/juliano-nicoletti/)')
st.sidebar.markdown('[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github)](https://github.com/julianonicoletti/julianonicoletti)')

st.title('Studying cardio disease predictions and features')
st.markdown(
    '''
    ### FUNCIONALIDADES:
    - Visualização interativa dos dados sobre doenças cardiovasculares.
    - Respostas para perguntas comuns sobre as doenças cardiovasculares.
    - Previsão da chance de desenvolver doenças cardiovasculares com base nos dados fornecidos.
    
    <br>
    
    
    ### COMO UTILIZAR?
    - DASHBOARDS:
        - Apresentação dos dados.
        - Respondendo perguntas com os dados
        
        <br>
        
    - MODELO PREVISÃO:
        - Entrada de valores para medir a chance de desenvolver Doenças Cardiovasculares.     
   
    
   
    ''', unsafe_allow_html=True
)