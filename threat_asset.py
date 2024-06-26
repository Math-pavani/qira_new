import streamlit as st
import pandas as pd

def run():

    st.subheader('Vinculação de Eventos de Ameaça a Ativos')

    if 'threat_data' not in st.session_state or st.session_state.threat_data.empty:
        st.error('Não há dados de eventos ameaça registrados. Certifique-se de que os eventos de ameaça foram registrados.')
        return

    if 'data' not in st.session_state or st.session_state.data.empty:
        st.error('Não há dados de assets registrados. Certifique-se de que os ativos foram registrados.')
        return

    eventos_ameaca = st.session_state.threat_data[['ID', 'Evento de Ameaça']]
    nomes_assets = st.session_state.data['Nome'].tolist()

    # Criar um DataFrame para relacionar eventos e assets se não existir
    if 'threat_asset_data' not in st.session_state:
        st.session_state.threat_asset_data = pd.DataFrame(columns=[
            'ID do evento de ameaça', 'Evento de ameaça', 'Asset afetado'
        ])

    # Interface para vincular Assets a Eventos de Ameaça
    for index, row in eventos_ameaca.iterrows():
        with st.expander(f"Evento de Ameaça: {row['Evento de Ameaça']}"):
            selected_assets = st.multiselect(f"Escolha os assets afetados pelo evento '{row['Evento de Ameaça']}'", 
                                             nomes_assets, 
                                             key=f"ms{row['ID']}")
            update = st.button(f"Atualizar Associação", key=f"btn{row['ID']}")
            
            if update:
                # Atualizar o DataFrame com as novas relações
                st.session_state.threat_asset_data = st.session_state.threat_asset_data.append({
                    'ID do evento de ameaça': row['ID'],
                    'Evento de ameaça': row['Evento de Ameaça'],
                    'Asset afetado': ', '.join(selected_assets)
                }, ignore_index=True)

    # Mostrar o DataFrame atualizado de associações
    st.write("Vinculações de Eventos de Ameaça a Assets:")
    st.dataframe(st.session_state.threat_asset_data)