import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit.components.v1 as components
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Análise Exploratória dos Dados', layout='wide')
df = pd.read_csv("data/processed/df_pronto.csv")
df_transformed = pd.read_csv("data/processed/df_pronto.csv")
df_original = pd.read_csv("data/raw/cardio_train.csv")
csv_transformed = df_transformed.to_csv(index=False).encode('utf-8')
csv_original = df_original.to_csv(index=False).encode('utf-8')

# SIDEBAR

image= Image.open('pages/images/doencas-cardiovasculares-gTq50UO9DE.jpeg')

st.sidebar.image(image, width=350, use_column_width='always')

st.sidebar.markdown('# CARDIO DISEASE')

st.sidebar.markdown('## Sobre o Projeto')
st.sidebar.markdown("""
Este aplicativo apresenta dashboards para uma análise exploratória de dados sobre doenças cardiovasculares,
bem como um modelo de previsão da chance de ser acometido por problemas cardiovasculares. 
Explore os dashboards e preveja sua chance de desenvolver doenças cardiovasculares.
""")


st.sidebar.download_button(
    label='Download dos dados originais',
    data=csv_original,
    file_name='cardio_disease_final.csv',
    mime='text/csv',
    type='primary'
    
)

st.sidebar.download_button(
    label='Download dos dados transformados',
    data=csv_transformed,
    file_name='cardio_disease_final.csv',
    mime='text/csv',
    type='primary'
    
)
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
st.write('---')
st.markdown('<br><br>', unsafe_allow_html=True)

tab1, tab2 = st.tabs([':bar_chart: Gráficos  ', ':mag_right: Respondendo a Perguntas'])

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:21px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)
with tab1:
    #load the saved html file ( visualized using sweetviz library)
    analysis_report2= open("pages/sweetviz_report.html", 'r', encoding='utf-8')
    components.html(analysis_report2.read(), height="100vh", width="100vw", scrolling=False)
    
    # st.markdown('### Gráficos de Distribuição')
    
    # features_num = ['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'bmi']
    # plt.figure(figsize=(15, 7))
    # for i, feature in enumerate(features_num):
    #     plt.subplot(2, 3, i+1)
    #     sns.histplot(df[feature], bins=25, kde=True)
    #     plt.title(f'Distribution of {feature}') 
    # plt.tight_layout()
    # st.pyplot(plt)
    # st.markdown('---')
    
    # categorical_features = ['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']
    # plt.figure(figsize=(14, 7))
    # for i, feature in enumerate(categorical_features):
    #     plt.subplot(2, 3, i+1)
    #     sns.countplot(data=df, x=feature)
    #     plt.title(f'Distribution of {feature}')
        
    # plt.tight_layout()
    # st.pyplot(plt)
    # st.markdown('---')

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
    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(8,7)) 
        plt.rcParams.update({'font.size': 11}) 
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
        st.pyplot(plt)
    with col2:
        plt.figure(figsize=(8,7)) 
        plt.rcParams.update({'font.size': 11}) 
        ax = sns.violinplot(data=df, x="gender", y="bmi", hue="cardio",split=True, inner="quart", fill=True, palette='muted')
       
        handles, labels = ax.get_legend_handles_labels()
        colors = sns.color_palette('muted', len(labels))

        label_map = {'0': 'Não', '1': 'Sim'}  

        custom_labels = [label_map.get(label, label) for label in labels]
        custom_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]

        ax.legend(custom_handles, custom_labels, title='Cardio Disease')
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['Women', 'Man'])
        ax.set_xlabel('')
        ax.set_ylabel('Body Index Mass (BMI)')
        ax.set_title('Distribuition of BMI by Age and Cardio Disease')
        st.pyplot(plt)
    st.markdown('##### **SIM**. Verifica-se que há uma mediana e distribuição mais elevados no valor de BMI no grupo ' 
                'com doença cardiovascular.')
    st.markdown('---')
    
    st.markdown('### Há uma relação direta entre o colesterol sanguíneo e problemas cardíacos?')
    col1, col2 = st.columns(2)
    with col1:
        plt.figure(figsize=(8,7)) 
        plt.rcParams.update({'font.size': 12})
        ax = sns.barplot(x='cholesterol', y='cardio', data=df, palette='muted')
        ax.set_xticks([0, 1, 2])
        ax.set_xticklabels(['Normal', 'Above Normal', 'Well Above Normal'])
        ax.set_xlabel('Cholesterol')
        ax.set_ylabel('Mean of Cardio Disease')
        ax.set_title('Distribuition of Cardio Disease by Cholesterol Level')
        st.pyplot(plt)
    with col2:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        st.markdown('#### **SIM**. Há uma relação direta entre o nível de colesterol e a média de acometidos por Doença Cardiovascular')
        
    st.markdown('---')
    
    
    




