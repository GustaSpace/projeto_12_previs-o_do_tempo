import streamlit as st
from dados_api import previsao_temperatura

st.set_page_config(layout='wide')

# Cidades
cidades = {
    "Londres": [51.51399980366155, -0.12839004089645853],
    "Florença": [43.771252128304376, 11.257443855733237],
    "Atenas": [37.986230082223095, 23.726322094203873],
    "Gramado": [-29.373418156410427, -50.88329507606586],
    "Guadalaraja": [20.67610472122916, -103.36080836272122],
    "Sydney": [-33.862630965770975, 151.1997064432956],
    "Punta cana": [18.561662012112592, -68.36739573361503]
}

# ------------------------- SIDEBAR
st.sidebar.title("previsão do tempo")
#st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude , longitude = cidades[cidade]


# ---------------------- BODY
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():
    # st.write(d['dia'], d['mes'], d['temperatura_media'])
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}°")

        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"
            
            elif d['temperatura_media'] < 18:
                temp = "cool.png"
            
            elif d['temperatura_media'] < 25:
                temp = "comfort.png"
            
            else:
                temp = "warm.png"
            
            st.image(temp, width=40)
            