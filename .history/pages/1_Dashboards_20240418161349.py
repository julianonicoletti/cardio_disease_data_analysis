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
    O dataset contem 70.000 linhas com 12 variáveis como idade, gênero, pressão arterial, colesterol, fumante ou não, etc.
    ### Descrição dos Dados
    1. **Age:** age | int (days).  
    2. **Height:** height | int (cm).  
    3. **Weight:** weight | float (kg).  
    4. **Gender:** gender | categorical code | 1: woman, 2: man.  
    5. **Systolic blood pressure:** ap_hi | int.  
    6. **Diastolic blood pressure:**  ap_lo | int.  
    7. **Cholesterol:**  cholesterol | 1: normal, 2: above normal, 3: well above normal.  
    8. **Glucose:**  gluc | 1: normal, 2: above normal, 3: well above normal.  
    9. **Smoking:**  smoke | binary.  
    10. **Alcohol intake:**  alco | binary.  
    11. **Physical activity:**  active | binary.  
    12. **Presence or absence of cardiovascular disease:** cardio | 1: disease, 0: no.  
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
    plt.figure(figsize=(14, 7))
    for i, feature in enumerate(categorical_features):
        plt.subplot(2, 3, i+1)
        sns.countplot(data=df, x=feature)
        plt.title(f'Distribution of {feature}')
        
    plt.tight_layout()
    st.pyplot(plt)
    st.markdown('---')

with tab2:
    st.markdown('### Há relação direta entre idade e incidência de problemas cardíacos?')
    plt.rcParams.update({'font.size': 5})
    plt.figure(figsize=(5, 3))
    sns.countplot(x='age', hue='cardio', data = df, palette="muted")
    plt.xlabel('Idade', fontsize=8)
    plt.ylabel('', fontsize=8)
    plt.legend(title='Cardiovascular Disease', labels=['No', 'Yes'])
    st.pyplot(plt)
    st.markdown('##### **SIM**. Os dados mostram que há uma relação direta entre idade e incidência de Doenças Cardiovasculares.')
    st.markdown('---')
    
    st.markdown('### Há relação direta entre pressão arterial e problemas cardiovasculares?')
    plt.rcParams.update({'font.size': 9})
    plt.figure(figsize=(11, 6))  
    plt.subplot(1, 2, 1) 
    ax = sns.boxplot(data=df, hue='cardio', y='ap_hi', palette='muted')
    
    handles, labels = ax.get_legend_handles_labels()
    colors = sns.color_palette('muted', len(labels))
    
    label_map = {'0': 'Não', '1': 'Sim'}  

    custom_labels = [label_map.get(label, label) for label in labels]
    custom_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
    ax.legend(custom_handles, custom_labels, title='Evento Cardíaco')
    plt.title('Systolic Blood Pressure Dist. by Cardio Disease')

    plt.subplot(1, 2, 2)
    ax = sns.boxplot(data=df, hue='cardio', y='ap_lo', palette='muted')
  
    handles, labels = ax.get_legend_handles_labels()
    colors = sns.color_palette('muted', len(labels))
    label_map = {'0': 'Não', '1': 'Sim'}  
    
    custom_labels = [label_map.get(label, label) for label in labels]
    custom_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
    ax.legend(custom_handles, custom_labels, title='Evento Cardíaco')
    plt.title('Diastolic Blood Pressure Dist. by Cardio Disease')

    plt.tight_layout()
    st.pyplot(plt)
    st.markdown('##### **SIM**. Verifica-se que em ambas as pressões a mediana é bem maior no grupo com doença cardiovascular.')
    st.markdown('---')
    
    st.markdown('### Há uma relação direta entre o BMI (Body Index Mass) e problemas cardíacos?')
    plt.figure(figsize=(10, 7)) 
    plt.rcParams.update({'font.size': 6}) 
    ax = sns.boxplot(data=df, hue='cardio', y='bmi', palette='muted')
    # Ajuste manual da legenda
    handles, labels = ax.get_legend_handles_labels()
    colors = sns.color_palette('muted', len(labels))

    # Mapeamento de rótulos
    label_map = {'0': 'Não', '1': 'Sim'}  

    # Criando legenda personalizada
    custom_labels = [label_map.get(label, label) for label in labels]
    custom_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
    ax.legend(custom_handles, custom_labels, title='Evento Cardíaco')
    plt.title('BMI distribuition by Cardiovascular Disease')
    plt.tight_layout()
    st.pyplot(plt, use_container_width=True)
    
    
    
    
    
    




