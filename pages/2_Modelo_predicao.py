import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import numpy as np



#carregando o modelo
st.set_page_config(layout='wide')
model = joblib.load('notebooks/grad_boost.pkl')
scaler = joblib.load('notebooks/robust_scaler.pkl')
df_transformed = pd.read_csv("data/processed/df_pronto.csv")
df_original = pd.read_csv("data/raw/cardio_train.csv")
csv_transformed = df_transformed.to_csv(index=False).encode('utf-8')
csv_original = df_original.to_csv(index=False).encode('utf-8')

# SIDEBAR

image= Image.open('pages/images/doencas-cardiovasculares-gTq50UO9DE.jpeg')

st.sidebar.image(image, width=350, use_column_width='always' )

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
    file_name='cardio_disease_original.csv',
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
    
# CORPO DO SITE

st.title('Modelo de Predição.')   
st.markdown('### Insira os valores dos parâmetros e clique em "Calcular"')
col1, col2 = st.columns(2)
with col1: 
    age = st.number_input('Idade', 0, 100, 40, help='Entre com a idade do paciente.' )
    height = st.number_input('Altura (em cm)', 60, 210, 160, help='Entre com a altura do Paciente.' )
    ap_hi = st.number_input('Pressão Sistólica (em mmHg) ', 90, 200, 120, help='Entre com a pressão sistólica do paciente')
    cholesterol_select = st.selectbox("Nível de Colesterol", ['Normal', 'Alto', 'Muito Alto'], help='Entre com o nível do colesterol sanguíneo')
    smoke_select = st.selectbox("Fumante", ['Nao', 'Sim'], help='Escolha se o paciente fuma ou não' )
    active_select = st.selectbox('Pratica Atividade Física', ['Sim', 'Nao'], help='Paciente pratica atividade física regularmente?')

with col2:
    gender_select = st.selectbox("Sexo", ['Masculino', 'Feminino'], help='Entre com o Sexo do paciente.' )
    weight = st.number_input('Peso (em Kg)', 30, 160, 70, help='Entre com a Altura do Paciente.' )
    ap_lo = st.number_input('Pressão Diastólica (em mmHg)', 50, 120, 80, help='Entre com a pressão diastólica do paciente' )
    gluc_select = st.selectbox("Glicemia", ['Normal', 'Alto', 'Muito Alto'], help='Entre com nível de glicemia do paciente.' )
    alco_select = st.selectbox("Ingere bebida alcólica? ", ['Nao', 'Sim'], help='O paciente ingere bebida alcólica regularmente?' )

# transformações
gender_map = {'Masculino': 1, 'Feminino': 0}
map1 = {'Normal': 0, 'Alto': 1, 'Muito Alto': 2}
map2 = {'Sim':1, 'Nao':0}
gender = gender_map[gender_select]
cholesterol = map1[cholesterol_select]
gluc = map1[gluc_select]
smoke = map2[smoke_select]
active = map2[active_select]
alco = map2[alco_select]
porcentagem = 0
calculado = False
bmi = weight/(height/100)**2

if st.button(" 🔍 CALCULAR"):
    input_values = np.array([age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi])
    feature_names = ['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'bmi']
    input_data = pd.DataFrame([input_values], columns=feature_names)
        
    proba = model.predict_proba(input_data)
                   
    probabilidade = proba[0][1] * 100
    calculado = True      
    
with st.container(border=True):
        if calculado:
            st.markdown(f'''### Para os dados inseridos as chances de desenvolver problemas cardiovasculares é de {round(probabilidade, 2)}% ''')
                   
with st.container(border=True):
    st.markdown(
        '''⚠️ ATENÇÃO: Este modelo não se destina a substituir um diagnóstico médico profissional.
        Ele foi desenvolvido com base em dados públicos que abordam fatores de predisposição a problemas cardíacos.
        Recomenda-se que qualquer decisão relacionada à saúde seja tomada em consulta com um profissional de saúde qualificado.

        '''
        )

