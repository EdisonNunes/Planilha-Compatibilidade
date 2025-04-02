import streamlit as st
import pandas as pd
#import streamlit_authenticator as stauth
from ModelSAS import *
##### Aula https://portalhashtag.com/cursos/1728736353758x643060883862200700

# -------- Banco de dados compartilhado --------- st.secrets['sqlite']
# [sqlite]
# database/SASOLUTION.db
# https://discuss.streamlit.io/t/help-with-accessing-sqlite-database-in-github-repo/16661
# lista_usuarios = session.query(Usuario).all()


# senhas_criptografadas = stauth.Hasher(['123456','123123','456456']).generate()

# credenciais = { 'usernames':{
#    'leandro@gmail.com': {'name': 'Leandro', 'password': senhas_criptografadas[0]},
#    'edison@gmail.com': {'name': 'Edison', 'password': senhas_criptografadas[1]},
#    'giane@gmail.com': {'name': 'Giane', 'password': senhas_criptografadas[2]},
# }
# }

# # credenciais = {'usernames': 
# #                {
# #                    usuario.email: {'name': usuario.nome, 'password': usuario.senha} for usuario in lista_usuarios
# #                }

# # }

# # autenticador (credenciais, nome do cookie no navegador, chave secreta, n° dias sem precisar reautenticar )
# autenticator =stauth.Authenticate(credenciais, 'credenciais_hashco', 'fsyfus%$67fs76AH7', cookie_expiry_days=30)

# def autenticar_usuario(autenticator):
#     nome, status_autenticacao, username = autenticator.login()
    
#     if status_autenticacao:
#         return {'nome': nome, 'username': username}
#     elif status_autenticacao == False:
#         st.error('Usuário ou senha inválidos')
#     else:
#         st.error('Preencha o formulário para fazer login')    


# def logout():
#     autenticator.logout()


# # autenticar usuário
# # 
# dados_usuario = autenticar_usuario(autenticator)    

dict_dados = {}
dados_usuario = {
    'username' : 'Edison'

}

#if dados_usuario:

    
    # email_usuario = dados_usuario['username']
    # usuario =  session.query(Usuario).filter_by(email=email_usuario).first()

# if usuario.admin:
pg = st.navigation(
    {   #     st.Page([ pagina/função, titulo])           
        'Home': [st.Page('homepage.py', title='Compatibilidade Química')],
        'Planilhas': [st.Page('compatibilidade_quimica.py', title='Planilhas'), 
                    st.Page('relat_compatibilidade.py', title='Prévia Relatório')
                    ],
        'Clientes': [st.Page('clientes.py', title='Clientes Cadastrados')],            
        # 'Conta': [st.Page(logout, title='Sair'),
        #         st.Page('criar_conta.py', title='Criar Conta')
        #         ]
        #'Conta': [st.Page('criar_conta.py', title='Criar Conta')
        #        ]        
    }
)
# else:
#     pg = st.navigation(
#     {   #     st.Page([ pagina/função, titulo])           
#         'Home': [st.Page('homepage.py', title='Hash&Co')],
#         'Dashboards': [st.Page('dashboard.py', title='Dashboard'), 
#                        st.Page('indicadores.py', title='Indicadores')
#                        ],
#         'Conta': [st.Page(logout, title='Sair')
#                   ]
#     }
# )    

pg.run()
