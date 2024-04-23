import streamlit as st
import joblib
import pickle
import numpy as np
from sklearn.neural_network import MLPClassifier


#carregando o modelo
st.set_page_config(layout='wide')
model = joblib.load('notebooks/grad_boost.pkl')
def preprocess_input_values(values):
    

with st.sidebar:
    
    st.write('Insira os valores dos parâmetros')
    idade = st.number_input('Idade', 0, 100, 40, help='Entre com a idade do Paciente.' )
    bmi = st.number_input('IMC', 15, 50, 25, help='Entre com o IMC do Paciente.' )
    glucose = st.number_input('Glicemia', 40, 600, 85, help='Entre com a glicemia do Paciente.' )
    insulin = st.number_input('Insulina', 1, 70, 10, help='Entre com a Insulinemia do Paciente.' )
    homa = st.number_input('HOMA-IR', 0, 50, 4, help='Entre com o valor do HOMA-IR (marcador para avaliar resistência a insulina)') 
    leptin = st.number_input('Leptin', 0, 120, 25, help='Entre com o valor da Leptin (marcador para avaliar estado metabólico e obesidade)' )
    adiponectin = st.number_input('Adiponectin', 0, 85, 10, help='Entre o valor da Adiponectin (marcador e estado metabólico, sensibilidade a insulina e metabolismo lipídico) do Paciente.' )
    resistin = st.number_input('Resistin', 0, 120, 40, help='Entre com o valor da Resistin (marcador para regulação de metabolismo)' )
    mcp1 = st.number_input('MCP-1', 25, 2000, 550, help='Entre com o valor de MCP-1 (marcador para processos inflamatórios).')
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

