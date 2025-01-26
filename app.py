import streamlit as st
import pandas as pd

# Função para carregar os dados do arquivo XLS
def load_data(file_path):
    data = pd.read_excel(r'C:\Users\jcass\Desktop\App\occurences2.xls.xlsx')
    return data

# Função para buscar o status do protocolo e calcular o progresso
def get_protocol_status(data, protocol_number):
    status = data.loc[data['Protocol'] == protocol_number, 'After Sales Status'].values
    if len(status) > 0:
        if pd.isna(status[0]) or status[0] == "SEM ESTOQUE":
            return "Processando", 10
        elif status[0] == "Concluído":
            return "Concluído", 100
        else:
            return status[0], 75
    else:
        return "Protocolo não encontrado", 0

# Interface do Streamlit
st.set_page_config(page_title="SolisTrack")
st.title("Visualizador de Protocolo")

# Carregar o arquivo XLS uma vez
file_path = 'caminho/para/seu/arquivo.xlsx'
data = load_data(r'C:\Users\jcass\Desktop\App\occurences2.xls.xlsx')

# Barra lateral
#st.sidebar.header("Navegação")
#st.sidebar.write("Use a barra lateral para navegar")

# Entrada do número do protocolo
protocol_number = st.text_input("Digite o número do protocolo")

if protocol_number:
    status, progress = get_protocol_status(data, protocol_number)
    st.write(f"Status do Protocolo {protocol_number}: {status}")
    #st.progress(progress)

    progress_bar = f"""
    <div style="width: 100%; background-color: transparent; border-radius: 5px;">
        <div style="width: {progress}%; background-color: #FFA12C; height: 14px; border-radius: 5px;"></div>
    </div>
    <div><br><div>
    """
    st.markdown(progress_bar, unsafe_allow_html=True)

    if status == "Protocolo não encontrado":
        st.success("Protocolo não encontrado. Verifique o número e tente novamente.")
    elif status == "Concluído":
        st.success("Protocolo concluído com sucesso!")
    elif status == "Processando":
        st.warning("Protocolo em processamento. Por favor, aguarde.")
