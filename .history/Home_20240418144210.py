import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home',
    layout='wide'
)

image= Image.open('pages/images/doencas-cardiovasculares-gTq50UO9DE.jpeg')

st.sidebar.image(image, width=250)

st.sidebar.markdown('# CARDIO DISEASE')
st.sidebar.markdown("""---""")

st.write('# Studying cardio disease predictions and features')

st.markdown(
    '''
    Este foi um estudo de análise exploratória de dados e criação de um modelo preditor para estudo
    de Doenças Cardiovasculares.add()
    ### COMO UTILIZAR?
    - DASHBOARDS:
        - Apresentação dos dados.
        - Respondendo perguntas com os dados
        
    -MODELO PREVISÃO:
        - Entrada de valores para medir a chance de desenvolver Doenças Cardiovasculares.     
   ___
    
    - Data Sciente (Juliano Batistela Nicoletti)
    '''
)