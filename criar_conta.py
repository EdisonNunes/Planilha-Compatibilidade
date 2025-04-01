import streamlit as st

st.write('Criar Conta')
# import streamlit as st
# from models import session, Usuario
# import streamlit_authenticator as stauth

# st.title('Criar Conta')

# form = st.form('form_criar_conta')
# nome_usuario = form.text_input('Nome do usuário')
# email_usuario = form.text_input('Email do usuário')
# senha_usuario = form.text_input('Senha do usuário', type='password')
# admin_usuario = form.checkbox('É um admin?')
# botao_submit = form.form_submit_button('Enviar')

# if botao_submit:
#     lista_usuarios_existentes = session.query(Usuario).filter_by(email=email_usuario).all()
#     if len(lista_usuarios_existentes) > 0:
#         st.write('Já existe um usuário com esse email cadastrado!')
#     elif len(email_usuario) < 5 or len(senha_usuario) < 3:
#         st.write('Preencha o campo de email e senha corretamente')
#     else:        
#         # Criar conta do usuário
#         senhas_criptografadas = stauth.Hasher([senha_usuario]).generate()[0]
#         usuario = Usuario(nome=nome_usuario, senha=senhas_criptografadas, email=email_usuario, admin=admin_usuario)
#         session.add(usuario)
#         session.commit()
#         st.write('Usuário criado com sucesso')
#         st.switch_page('homepage.py')


