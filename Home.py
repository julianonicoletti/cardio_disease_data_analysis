import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Cardio Disease Prediction',
    layout='wide',
)

image1= Image.open('pages/images/doencas-cardiovasculares-gTq50UO9DE.jpeg')
image2 = Image.open('pages/images/image2.jpg')
with st.sidebar:
    st.expander("barra lateral expandida", expanded=True)
    st.sidebar.image(image1, width=350, use_column_width='always')

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

st.title('Estudo sobre fatores de predisposição a problemas cardíacos e modelo de predição')
st.image(image2, width=650, use_column_width='auto')
st.markdown(
    '''
    ### FUNCIONALIDADES:
    - Visualização interativa dos dados sobre doenças cardiovasculares.
    - Respostas para perguntas comuns sobre as doenças cardiovasculares.
    - Previsão da chance de desenvolver doenças cardiovasculares com base nos dados fornecidos.
    
    <br>
    
    
    ### COMO UTILIZAR?
    - ANÁLISE EXPLORATÓRIA DOS DADOS:
        - Apresentação dos dados.
        - Respondendo perguntas com os dados
        
        <br>
        
    - MODELO PREVISÃO:
        - Entrada de valores para medir a chance de desenvolver Doenças Cardiovasculares.     
   
    ''', unsafe_allow_html=True
)