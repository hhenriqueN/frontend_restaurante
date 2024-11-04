import streamlit as st

# Configuração da página
st.set_page_config(page_title="Painel de Controle Restaurante", layout="wide")

st.markdown("<h1 style='text-align: center;'>Painel de Controle Restaurante</h1>", unsafe_allow_html=True)

# Inicializa o estado da sessão para pedidos se não existir
if 'pedidos_recebidos' not in st.session_state:
    st.session_state.pedidos_recebidos = ["Pedido 1: Pizza", "Pedido 2: Salada", "Pedido 3: Batata Frita"]
if 'pedidos_em_andamento' not in st.session_state:
    st.session_state.pedidos_em_andamento = ["Pedido 4: Hambúrguer"]
if 'pedidos_prontos' not in st.session_state:
    st.session_state.pedidos_prontos = ["Pedido 5: Espaguete", "Pedido 6: Sushi"]

# Função para criar uma caixa com borda para pedidos e gerenciar os botões de atualização de status
def create_box(pedidos, button_text, action_func):
    for pedido in pedidos:
        with st.container():
            st.markdown(f"""
                <div style="border: 1px solid black;border-radius: 10px; padding: 10px; margin: 5px;">
                    <div style="min-height: 50px;">{pedido}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(button_text, key=f"{pedido}_{button_text}"):
                action_func(pedido)

# Funções para atualizar o status dos pedidos
def mover_para_em_andamento(pedido):
    st.session_state.pedidos_recebidos.remove(pedido)
    st.session_state.pedidos_em_andamento.append(pedido)

def mover_para_pronto(pedido):
    st.session_state.pedidos_em_andamento.remove(pedido)
    st.session_state.pedidos_prontos.append(pedido)

def concluir_pedido(pedido):
    st.session_state.pedidos_prontos.remove(pedido)

# Colunas para os pedidos
col1, col2, col3 = st.columns(3)

# Seções dos pedidos com subheaders
with col1:
    st.markdown("<h3 style='text-align: center;'>Pedidos recebidos</h3>", unsafe_allow_html=True)
    create_box(st.session_state.pedidos_recebidos, 'Atualizar para "Em andamento"', mover_para_em_andamento)

with col2:
    st.markdown("<h3 style='text-align: center;'>Pedidos em andamento</h3>", unsafe_allow_html=True)
    create_box(st.session_state.pedidos_em_andamento, 'Atualizar para "Pronto"', mover_para_pronto)

with col3:
    st.markdown("<h3 style='text-align: center;'>Pedidos prontos</h3>", unsafe_allow_html=True)
    create_box(st.session_state.pedidos_prontos, "Concluir pedido", concluir_pedido)
