import streamlit as st
import pandas as pd

def run():

    st.title('Inventário de Assets')

    # Inicialização de sessão para armazenar os dados temporariamente
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame(columns=[
            'ID', 'Nome', 'Descrição', 'Local', 'Responsável', 'Valor para o negócio',
            'Custo de reposição', 'Criticidade', 'Usuários', 'Ambiente Alvo'
        ])

    with st.form("form_assets"):
        st.write("Preencha as informações do asset a seguir:")

        # Entrada de dados para um novo asset
        nome = st.text_input("Nome")
        descricao = st.text_area("Descrição")
        local = st.text_input("Local")
        responsavel = st.text_input("Responsável")
        valor_negocio = st.number_input("Valor para o negócio", min_value=0.0, format='%f')
        custo_reposicao = st.number_input("Custo de reposição", min_value=0.0, format='%f')
        criticidade = st.selectbox("Criticidade", ['Alta', 'Média', 'Baixa'])
        usuarios = st.text_input("Usuários")
        ambiente_alvo = st.text_input("Ambiente Alvo")

        # Botão de submissão do formulário
        submitted = st.form_submit_button("Registrar Asset")
        if submitted:
            new_asset = {
                'ID': len(st.session_state.data) + 1,  # ID automático baseado no tamanho do DataFrame existente
                'Nome': nome, 
                'Descrição': descricao,
                'Local': local,
                'Responsável': responsavel,
                'Valor para o negócio': valor_negocio,
                'Custo de reposição': custo_reposicao,
                'Criticidade': criticidade,
                'Usuários': usuarios,
                'Ambiente Alvo': ambiente_alvo
            }
            # Acréscimo do novo asset ao DataFrame
            st.session_state.data = st.session_state.data.append(new_asset, ignore_index=True)

    # Exibindo o DataFrame completo
    st.write("Inventário de Assets Registrados:")
    st.write(st.session_state.data)