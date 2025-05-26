import streamlit as st



pg = st.navigation(
    {              
        'SA SOLUTION':      [st.Page('homepage.py',         title='Home',                    icon=':material/filter_alt:')],
        'Planilhas': [st.Page('comp_quimica.py',            title='Inserir Planilhas',       icon=':material/thumb_up:'), 
                      st.Page('relat_compatibilidade.py',   title='Prévia Relatório',        icon=':material/visibility:')
                     ],
        'Clientes':  [st.Page('clientes.py',                title='Clientes Cadastrados',    icon=':material/groups:')],   


    }
)
pg.run()

# #Estilizando com style.css 
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


