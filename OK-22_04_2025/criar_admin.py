from models import session, Usuario
import streamlit_authenticator as stauth

senhas_criptografadas = stauth.Hasher(['123456']).generate()[0]
usuario = Usuario(nome='Giane', senha=senhas_criptografadas, email='giane@gmail.com', admin=False)
session.add(usuario)
session.commit()

#senhas_criptografadas = stauth.Hasher(['123456']).generate()[0]
#usuario = Usuario(nome='Edison', senha=senhas_criptografadas, email='edison@gmail.com', admin=True)
#session.add(usuario)
#session.commit()

