import streamlit as st
import pandas as pd

def run():

    st.title('Inventário de Ameaças')

    # Inicialização de sessão para armazenar os dados temporariamente
    if 'threat_data' not in st.session_state:
        st.session_state.threat_data = pd.DataFrame(columns=[
            'ID', 'Grupo de Ameaça', 'Evento de Ameaça', 'Descrição', 'No Escopo'
        ])

    with st.form("form_threats"):
        st.write("Preencha as informações da ameaça a seguir:")

        # Entrada de dados para um novo evento de ameaça
        grupo_ameaca = st.selectbox("Grupo de Ameaça", ['Adversarial', 'Accidental', 'Environmental'])
        evento_ameaca = st.text_input("Evento de Ameaça")
        descricao = st.text_area("Descrição")
        no_escopo = st.selectbox("No Escopo", ['Sim', 'Não'])

        # Botão de submissão do formulário
        submitted = st.form_submit_button("Registrar Ameaça")
        if submitted:
            new_threat = {
                'ID': len(st.session_state.threat_data) + 1,  # ID automático baseado no tamanho do DataFrame existente
                'Grupo de Ameaça': grupo_ameaca,
                'Evento de Ameaça': evento_ameaca,
                'Descrição': descricao,
                'No Escopo': no_escopo
            }
            # Acréscimo do novo evento ao DataFrame
            st.session_state.threat_data = st.session_state.threat_data.concat(new_threat, ignore_index=True)

    # Exibindo o DataFrame completo
    st.write("Inventário de Ameaças Registradas:")
    st.write(st.session_state.threat_data)
