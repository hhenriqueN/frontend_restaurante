import streamlit as st

# Configuração da página
st.set_page_config(page_title="Painel de Controle Restaurante", layout="wide")

st.markdown("<h1 style='text-align: center;'>Painel de Controle Restaurante</h1>", unsafe_allow_html=True)
st.title('')


# Título do painel


# Função para criar uma caixa com borda
def create_box(content):
    with st.container():
        st.markdown(f"""
            <div style="border: 2px solid black; padding: 10px; margin: 10px;">
                <div style="min-height: 50px;">{content}</div>  <!-- Placeholder para conteúdo -->
            </div>
        """, unsafe_allow_html=True)

# Colunas para os pedidos
col1, col2, col3 = st.columns(3)

# Exemplo de pedidos
pedidos_recebidos = ["Pedido 1: Pizza", "Pedido 2: Salada"]
pedidos_em_andamento = ["Pedido 3: Hambúrguer"]
pedidos_prontos = ["Pedido 4: Espaguete", "Pedido 5: Sushi"]

# Seções dos pedidos com subheaders
with col1:
    st.markdown("<h3 style='text-align: center;'>Pedidos recebidos</h3>", unsafe_allow_html=True)
    
    create_box("<br>".join(pedidos_recebidos))

with col2:
    st.markdown("<h3 style='text-align: center;'>Pedidos em andamento</h3>", unsafe_allow_html=True)
    create_box("<br>".join(pedidos_em_andamento))

with col3:
    st.markdown("<h3 style='text-align: center;'>Pedidos prontos</h3>", unsafe_allow_html=True)
    create_box("<br>".join(pedidos_prontos))

