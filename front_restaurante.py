import streamlit as st

# Configuração da página
st.set_page_config(page_title="Painel de Controle Restaurante", layout="wide")

st.markdown("<h1 style='text-align: center;'>Painel de Controle Restaurante</h1>", unsafe_allow_html=True)
st.title('')

# Função para criar uma caixa com borda para pedidos
def create_box(pedidos):
    with st.container():
        for pedido in pedidos:
            st.markdown(f"""
                <div style="border: 1px solid black; padding: 10px; margin: 5px;">
                    <div style="min-height: 50px;">{pedido}</div>
                    <button style="padding: 10px; font-size: 16px;">Atualizar Status</button>
                </div>
            """, unsafe_allow_html=True)

# Colunas para os pedidos
col1, col2, col3 = st.columns(3)

# Exemplo de pedidos
pedidos_recebidos = ["Pedido 1: Pizza", "Pedido 2: Salada", 'pedido', 'pedido']
pedidos_em_andamento = ["Pedido 3: Hambúrguer"]
pedidos_prontos = ["Pedido 4: Espaguete", "Pedido 5: Sushi"]

# Seções dos pedidos com subheaders
with col1:
    st.markdown("<h3 style='text-align: center;'>Pedidos recebidos</h3>", unsafe_allow_html=True)
    create_box(pedidos_recebidos)

with col2:
    st.markdown("<h3 style='text-align: center;'>Pedidos em andamento</h3>", unsafe_allow_html=True)
    create_box(pedidos_em_andamento)

with col3:
    st.markdown("<h3 style='text-align: center;'>Pedidos prontos</h3>", unsafe_allow_html=True)
    create_box(pedidos_prontos)
