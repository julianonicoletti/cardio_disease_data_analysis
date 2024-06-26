import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import base64
import numpy as np
from sklearn.neural_network import MLPClassifier


#carregando o modelo
st.set_page_config(layout='wide')
model = joblib.load('notebooks/grad_boost.pkl')
df_transformed = pd.read_csv("data/processed/df_pronto.csv")
df_original = pd.read_csv("data/raw/cardio_train.csv")
csv_transformed = df_transformed.to_csv(index=False).encode('utf-8')
csv_original = df_original.to_csv(index=False).encode('utf-8')
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
    
# CORPO DO SITE

st.title('Modelo de Predição.')   
st.markdown('### Insira os valores dos parâmetros')
col1, col2 = st.columns(2)
with col1: 
    age = st.number_input('Idade', 0, 100, 40, help='Entre com a idade do paciente.' )
    height = st.number_input('Altura (em cm)', 60, 210, 160, help='Entre com a altura do Paciente.' )
    ap_hi = st.number_input('Pressão Sistólica (em mmHg) ', 90, 200, 120, help='Entre com a pressão sistólica do paciente')
    cholesterol_select = st.selectbox("Nível de Colesterol", ['Normal', 'Alto', 'Muito Alto'], help='Entre com o nível do colesterol sanguíneo')
    smoke_select = st.selectbox("Fumante", ['Sim', 'Não'], help='Escolha se o paciente fuma ou não' )



with col2:
    gender = st.selectbox("Sexo", ['Masculino', 'Feminino'], help='Entre com o Sexo do paciente.' )
    weight = st.number_input('Peso (em Kg)', 30, 160, 70, help='Entre com a Altura do Paciente.' )
    ap_lo = st.number_input('Pressão Diastólica (em mmHg)', 50, 120, 80, help='Entre com a pressão diastólica do paciente' )
    gluc_select = st.selectbox("Glicemia", ['Normal', 'Alto', 'Muito Alto'], help='Entre com nível de glicemia do paciente.' )
    alco_select = st.selectbox("Ingere bebida alcólica? ", ['Sim', 'Não'], help='O paciente ingere bebida alcólica regularmente?' )

# transformações
map1 = {'Normal': 0, 'Alto': 1, 'Muito Alto': 2}
cholesterol = map1(cholesterol_select)
st.write(cholesterol)
gluc = map1(gluc_select)

resultado = " "
porcentagem = 0
calculado = False
if st.button(" 🔍 CALCULAR"):
    input_values = np.array([idade, bmi, glucose, insulin, homa, leptin, adiponectin, resistin, mcp1])
    processed_values = preprocess_input_values(input_values)
    # feat_log = []
    # features = [idade, bmi, glucose, insulin, homa, leptin, adiponectin, resistin, mcp1]
    # for i in features:
    #     feat_log.append(np.log(i))
    # x_pred = np.array([feat_log])
    previsao = model.predict(processed_values)
    proba = model.predict_proba(processed_values)
    print("Dados de entrada antes do pré-processamento:")
    print(input_values)
    print("Dados de entrada após o pré-processamento:")
    print(processed_values)

    # Depuração dos limites dos valores de entrada
    print("Valores dos dados de entrada:")
    print(input_values)

    # Depuração da verificação do modelo
    print("Informações sobre o modelo:")
    print(model)

    # Depuração da saída do modelo
    print("Saída do modelo:")
    print("Previsão:", previsao)
    print("Probabilidade:", proba)
            
    if previsao == 0:
        resultado = "BENIGNO"
        probabilidade = proba[0][0]
    else:
        resultado = "MALIGNO"
        probabilidade = proba[0][1]

    porcentagem = probabilidade * 100
    calculado = True
        
col1, col2 = st.columns([1.5,2])
with col1:
    st.image('image_breast_cancer.jpg', use_column_width='always'  )
with col2: 
    st.title("Modelo de Cálculo da malignidade de Cancer de Mama com Biomarcadores. ")
    st.markdown('----------------------------------------------------')
    st.markdown('## Modo de Usar:')
    st.markdown('### Insira o resultado dos marcadores bioquímicos na barra lateral e clique em "Calcular".')
    
    with st.container(border=True):
        if calculado:
            st.markdown(f'''#### Para os dados inseridos o resultado é {resultado} e a probabilidade desse resultado ser verdadeiro é de {round(porcentagem, 2)}% ''')
            
    st.markdown('---------')
    with st.container(border=True):
        st.markdown(
            '''⚠️ ATENÇÃO: Este modelo não tem a pretensão de servir como diagnótico, ele foi desenvolvido
            com base em uma Pesquisa realizada em 2018 que tentou estabelecer uma relação entre marcadores
            bioquímicos e a incidência de malignidade para Cancer de Mama. O artigo científico pode ser 
            acessado no portal PubMed através do link: https://pubmed.ncbi.nlm.nih.gov/32436139/
            '''
            )

