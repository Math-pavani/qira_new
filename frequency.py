import streamlit as st
import pandas as pd


def run():

    st.subheader('Análise de frequência de eventos de ameaça')

    if 'threat_data' in st.session_state and not st.session_state.threat_data.empty:
        # Criar ou atualizar o DataFrame freq_data com base nos eventos de ameaça registrados
        eventos_ameaca = st.session_state.threat_data['Evento de Ameaça'].tolist()
        
        # Iniciar ou atualizar o DataFrame de frequências
        if 'freq_data' not in st.session_state:
            st.session_state.freq_data = pd.DataFrame({
                'ID do evento de ameaça': pd.Series(range(1, len(eventos_ameaca) + 1)),
                'Evento de ameaça': eventos_ameaca,
                'Frequência mínima': pd.Series([0]*len(eventos_ameaca)),
                'Frequência máxima': pd.Series([0]*len(eventos_ameaca)),
                'Frequência mais comum (moda)': pd.Series([0]*len(eventos_ameaca)),
                'Informação de suporte': pd.Series([""]*len(eventos_ameaca))
            })
        else:
            # Atualiza o DataFrame caso novos eventos tenham sido adicionados
            existing_events = list(st.session_state.freq_data['Evento de ameaça'])
            new_events = [event for event in eventos_ameaca if event not in existing_events]
            for event in new_events:
                new_freq_row = {
                    'ID do evento de ameaça': len(st.session_state.freq_data) + 1,
                    'Evento de ameaça': event,
                    'Frequência mínima': 0,
                    'Frequência máxima': 0,
                    'Frequência mais comum (moda)': 0,
                    'Informação de suporte': ""
                }
                st.session_state.freq_data = st.session_state.freq_data.append(new_freq_row, ignore_index=True)

        # Interface para editar os valores de frequência
        for idx, row in st.session_state.freq_data.iterrows():
            with st.expander(f"Editar {row['Evento de ameaça']}"):
                f_min = st.number_input(f"Frequência Mínima ({row['Evento de ameaça']})", value=row['Frequência mínima'], key=f"min{idx}")
                f_max = st.number_input(f"Frequência Máxima ({row['Evento de ameaça']})", value=row['Frequência máxima'], key=f"max{idx}")
                f_moda = st.number_input(f"Frequência Mais Comum (Moda) ({row['Evento de ameaça']})", value=row['Frequência mais comum (moda)'], key=f"moda{idx}")
                supp_info = st.text_area(f"Informação de Suporte ({row['Evento de ameaça']})", value=row['Informação de suporte'], key=f"supp{idx}")
                if st.button(f"Atualizar {row['Evento de ameaça']}", key=f"update{idx}"):
                    st.session_state.freq_data.at[idx, 'Frequência mínima'] = f_min
                    st.session_state.freq_data.at[idx, 'Frequência máxima'] = f_max
                    st.session_state.freq_data.at[idx, 'Frequência mais comum (moda)'] = f_moda
                    st.session_state.freq_data.at[idx, 'Informação de suporte'] = supp_info
        st.write("Registro de Frequências de Eventos de Ameaça:")
        st.dataframe(st.session_state.freq_data)

    else:
        st.write("Por favor, registre eventos de ameaça na página de Registro de Ameaças antes de proceder.")