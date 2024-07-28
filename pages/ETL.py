import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

st.title('Extração de bases:')
st.divider()

with st.sidebar:
    filtro_cidade = st.selectbox("Curso",['Guarujá','São Paulo','Campinas','Todas'])
    filtro_periodo = st.select_slider("Período", options=[30,60,90])
    
st.subheader(f'Filtrando pela cidade: {filtro_cidade}')  
df = pd.DataFrame(
    [
       {"Data e Hora": "27/07/24 - 21:58", "Item": 'Chocolate Nestlé', "Quantidade": 1, 'Valor':4.32},
       {"Data e Hora": "27/07/24 - 22:02", "Item": 'Escova de Cabelo', "Quantidade": 1, 'Valor':12.10},
       {"Data e Hora": "27/07/24 - 22:04", "Item": 'Cigarro Marlboro', "Quantidade": 2, 'Valor':24.80},
       {"Data e Hora": "27/07/24 - 22:10", "Item": 'Sorvete Kibon', "Quantidade": 1, 'Valor':18.40},
       {"Data e Hora": "27/07/24 - 22:12", "Item": 'Panela de Aço', "Quantidade": 1, 'Valor':55.90},
       {"Data e Hora": "27/07/24 - 22:12", "Item": 'Detergente Oba', "Quantidade": 1, 'Valor':8.90},
       {"Data e Hora": "27/07/24 - 22:16", "Item": 'Óleo de canola', "Quantidade": 2, 'Valor':16.70},
       {"Data e Hora": "27/07/24 - 22:22", "Item": 'Coca Cola', "Quantidade": 4, 'Valor':32.40},
       {"Data e Hora": "27/07/24 - 22:23", "Item": 'Cx. Cerveja Heineken', "Quantidade": 1, 'Valor':55.00},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

st.download_button(
    label="Download data as CSV",
    data=df.to_csv().encode("utf-8"),
    file_name="large_df.csv",
    mime="text/csv",
)
