import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Cardio Disease Prediction',
    layout='wide'
)

image= Image.open('pages/images/doencas-cardiovasculares-gTq50UO9DE.jpeg')

st.sidebar.image(image, width=250)

st.sidebar.markdown('# CARDIO DISEASE')
st.sidebar.markdown("""---""")

st.sidebar.markdown('## Desenvolvido por Juliano Batistela Nicoletti')
st.sidebar.markdown('[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/juliano-nicoletti/)')
st.sidebar.markdown('[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github)](https://github.com/julianonicoletti/julianonicoletti)')


st.write('# Studying cardio disease predictions and features')

st.markdown(
    '''
    Este foi um estudo de análise exploratória de dados e criação de um modelo preditor para estudo de Doenças Cardiovasculares
    
    ### COMO UTILIZAR?
    - DASHBOARDS:
        - Apresentação dos dados.
        - Respondendo perguntas com os dados
        
        <br>
        
    - MODELO PREVISÃO:
        - Entrada de valores para medir a chance de desenvolver Doenças Cardiovasculares.     
   ___
    
   
    ''', unsafe_allow_html=True
)