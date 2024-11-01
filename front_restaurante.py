import streamlit as st
from datetime import datetime
# Input para escolher o restaurante
# restaurante = st.selectbox("Escolha o restaurante", ["Restaurante A", "Restaurante B", "Restaurante C"])
# Ajuste da largura para expandir o conteúdo na página
st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 90%;  /* Aumenta a largura da área de conteúdo */
        padding-top: 1rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título do painel de controle
st.title("Painel de Controle de Pedidos do Restaurante")

# Dividindo a página em três colunas
col1, col2, col3 = st.columns(3)

# Dados fictícios de pedidos
pedidos_recebidos = ["Pedido #1", "Pedido #2", "Pedido #3", "Pedido #7", "Pedido #8"]
pedidos_andamento = ["Pedido #4", "Pedido #5"]
pedidos_prontos = ["Pedido #6"]

# Coluna de Pedidos Recebidos
with col1:
    st.header("Pedidos Recebidos")
    if pedidos_recebidos:
        for pedido in pedidos_recebidos:
            st.write(pedido)
            if st.button(f"Enviar {pedido} para Andamento", key=f"{pedido}_recebido"):
                # Lógica para mover o pedido para "Pedidos em Andamento"
                pedidos_recebidos.remove(pedido)
                pedidos_andamento.append(pedido)
    else:
        st.write("Nenhum pedido recebido")

# Coluna de Pedidos em Andamento
with col2:
    st.header("Pedidos em Andamento")
    if pedidos_andamento:
        for pedido in pedidos_andamento:
            st.write(pedido)
            if st.button(f"Marcar {pedido} como Pronto", key=f"{pedido}_andamento"):
                # Lógica para mover o pedido para "Pedidos Prontos"
                pedidos_andamento.remove(pedido)
                pedidos_prontos.append(pedido)
    else:
        st.write("Nenhum pedido em andamento")

# Coluna de Pedidos Prontos
with col3:
    st.header("Pedidos Prontos")
    if pedidos_prontos:
        for pedido in pedidos_prontos:
            st.write(pedido)
            if st.button(f"Pedido {pedido} Retirado", key=f"{pedido}_pronto"):
                # Lógica para remover o pedido da lista de prontos
                pedidos_prontos.remove(pedido)
    else:
        st.write("Nenhum pedido pronto")