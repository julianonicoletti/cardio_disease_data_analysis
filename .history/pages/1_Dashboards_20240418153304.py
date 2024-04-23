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
plt.style.use("bmh")
st.title('Análise Exploratória dos Dados')
st.markdown("""
Para esse estudo utilizamos de uma base de dados pública disponivel no site [Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset).
Foram feitos tratamentos nos dados para retirada de outliers (valores muito acima da média) 
e criação de uma coluna chamada BMI que é um fator entre Altura e Peso de cada paciente
""")

tab1, tab2 = st.tabs(['Gráficos', 'Respondendo a Perguntas'])

with tab1:
    st.markdown('### Gráficos de Distribuição')
    
    features_num = ['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'bmi']
    plt.figure(figsize=(15, 7))
    for i, feature in enumerate(features_num):
        plt.subplot(2, 3, i+1)
        sns.histplot(df[feature], bins=25, kde=True)
        plt.title(f'Distribution of {feature}') 
    plt.tight_layout()
    st.pyplot(plt)
    st.markdown('---')
    
    categorical_features = ['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']
    plt.figure(figsize=(14, 9))
    for i, feature in enumerate(categorical_features):
        plt.subplot(2, 3, i+1)
        sns.countplot(data=df, x=feature)
        plt.title(f'Distribution of {feature}')
        
    plt.tight_layout()
    st.pyplot(plt)
    st.markdown('---')
    
    
    
    
    




