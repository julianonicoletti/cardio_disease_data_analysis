import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Dashboards', layout='wide')
df = pd.read_csv("data/processed/df_pronto.csv")


# SIDEBAR

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

# LAYOUT STREAMLIT

st.title('Análise Exploratória dos Dados')
st.sidebar.markdown("""
Para esse estudo utilizamos de uma base de dados pública disponivel no site Kaggle. Foram feitos tratamentos
nos dados para retirada de outliers (valores muito acima da média) e criação de uma coluna chamada BMI que é um fator
entre Altura e Peso de cada paciente
""")




