import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

st.title('Lojas Mari Dashboard')
st.divider()

with st.sidebar:
    filtro_cidade = st.selectbox("Curso",['Guarujá','São Paulo','Campinas','Geral'])
    filtro_periodo = st.select_slider("Período", options=[30,60,90])

col1, col2, col3 = st.columns(3)
rec_tot_cid=150
rec_med_cid=17.7
rec_dia_cid=18.5
st.subheader(f"Analise da loja: {filtro_cidade}")
col1.metric("Receita total", f"R$ {rec_tot_cid} mil", "4%")
col2.metric("Receita média", f"R$ {rec_med_cid} mil", "-8%")
col3.metric("Receita do dia", f"R$ {rec_dia_cid} mil", "4%")

colA, colB = st.columns(spec=[0.5,0.5])
with colA:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3), columns=["col1", "col2", "col3"]
    )
    st.area_chart(
        chart_data,
        x="col1",
        y=["col2", "col3"],
        color=["#FF0000", "#0000FF"],  # Optional
    )
with colB:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    
st.divider()
st.subheader("Itens vendidos por loja")
df_rd = pd.DataFrame({'lat': [26.24] * 100,'lon': [41.33] * 100})
df_sp = pd.DataFrame({'lat': [-23.54] * 400,'lon': [-46.62] * 400})
df_cp = pd.DataFrame({'lat': [-22.87] * 600,'lon': [-47.05] * 600})
df_gj = pd.DataFrame({'lat': [-23.97] * 500,'lon': [-46.21] * 500})
df_cid=pd.concat([df_rd,df_sp,df_cp,df_gj]).reset_index().drop(columns=['index'])
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-23.55,
            longitude=-46.63,
            zoom=8,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df_cid,
                get_position="[lon, lat]",
                radius=5000,
                elevation_scale=600,
                elevation_range=[0, 60],
                pickable=True,
                extruded=True,
            ),
            # pdk.Layer(
            #     "ScatterplotLayer",
            #     data=chart_data,
            #     get_position="[lon, lat]",
            #     get_color="[200, 30, 0, 160]",
            #     get_radius=200,
            # ),
        ]
    )
)