import streamlit as st
import pandas as pd
from ModelSAS import *

# @st.cache_data
def load_clientes(database):
    with Session(database) as session:
            result = session.execute(text("SELECT * FROM Clientes"))
        
            df = result.fetchall()
            df = pd.DataFrame(df)
            return df



    