import streamlit as st
import assets
import threat_asset
import threat_events
import frequency



def main():

    st.title('Sistema de Gerenciamento de Eventos de Ameaça e Ativos')
    
    st.write("""
    Bem-vindo ao Sistema de Gerenciamento de Eventos de Ameaça e Ativos! Este sistema permite:
    - Registrar eventos de ameaças potenciais.
    - Analisar a frequência com que esses eventos podem ocorrer.
    - Associar esses eventos a ativos específicos dentro da organização.
    Utilize a barra lateral para navegar entre as diferentes funcionalidades do aplicativo.
    """)

    PAGES = {
    "Inventário de Assets": assets,
    "Threat Event Catalogue": threat_events,
    "Frequency":frequency,
    "Threat Events & Assets": threat_asset
}
    st.sidebar.title('Navegação')
    selection = st.sidebar.radio("Ir para", list(PAGES.keys()))

    # Botão para resetar a sessão
    if st.sidebar.button('Restaurar Sessão'):
        # Limpar todos os dados salvos na sessão
        keys_to_remove = ['threat_data', 'freq_data', 'data', 'threat_asset_data']
        for key in keys_to_remove:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()  # Reinicia o aplicativo para refletir o estado limpo
    
    page = PAGES[selection]
    page.run()

if __name__ == "__main__":
    main()
