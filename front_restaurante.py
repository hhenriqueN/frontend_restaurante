import streamlit as st
import requests

# Base URL da API do backend (Flask)
BASE_URL = "https://insper-food-w886.onrender.com/"

# Função genérica para fazer requisições ao backend
def fazer_requisicao(endpoint, method="GET", params=None, data=None):
    url = f"{BASE_URL}/{endpoint}"

    try:
        if method == "GET":
            response = requests.get(url, params=params)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url, params=params)
        else:
            st.error("Método HTTP não suportado.")
            return None

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 201:
            st.success("Operação realizada com sucesso!")
            return response.json()
        elif response.status_code == 404:
            st.warning("⚠️ Recurso não encontrado.")
        elif response.status_code == 500:
            st.error("⚠️ Erro interno do servidor.")
        else:
            st.error(f"⚠️ Erro: {response.status_code} - {response.text}")

        return None

    except Exception as e:
        st.error(f"⚠️ Erro de conexão: {e}")
        return None

# Configuração da página
st.set_page_config(page_title="Painel de Controle Restaurante", layout="wide")

st.markdown("<h1 style='text-align: center;'>Painel de Controle Restaurante</h1>", unsafe_allow_html=True)
st.write('')

# Inicializa o estado da sessão para pedidos se não existir
if 'pedidos_recebidos' not in st.session_state:
    resposta = fazer_requisicao('/pedidos', method="GET")
    if resposta and "pedidos_em_andamento" in resposta:
        st.session_state.pedidos_recebidos = [
            {
                "senha": pedido['senha'],
                "descricao": f"Senha {pedido['senha']}: Itens {pedido['codigos_itens']}"
            }
            for pedido in resposta["pedidos_em_andamento"]
        ]
    else:
        st.session_state.pedidos_recebidos = []
if 'pedidos_em_andamento' not in st.session_state:
    st.session_state.pedidos_em_andamento = []
if 'pedidos_prontos' not in st.session_state:
    st.session_state.pedidos_prontos = []

# Função para criar uma caixa com borda para pedidos e gerenciar os botões de atualização de status
def create_box(pedidos, button_text, action_func):
    for pedido in pedidos:
        with st.container():
            st.markdown(f"""
                <div style="border: 1px solid black;border-radius: 10px; padding: 10px; margin: 5px;">
                    <div style="min-height: 50px;">{pedido['descricao']}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(button_text, key=f"{pedido['senha']}_{button_text}"):
                action_func(pedido)
                st.rerun()  # Força a re-execução do script para atualizar a interface

# Funções para atualizar o status dos pedidos
def mover_para_em_andamento(pedido):
    st.session_state.pedidos_recebidos.remove(pedido)
    st.session_state.pedidos_em_andamento.append(pedido)

def mover_para_pronto(pedido):
    st.session_state.pedidos_em_andamento.remove(pedido)
    st.session_state.pedidos_prontos.append(pedido)

def concluir_pedido(pedido):
    senha = pedido['senha']
    st.session_state.pedidos_prontos.remove(pedido)
    fazer_requisicao(f'pedidos/{senha}', method="DELETE")

# Colunas para os pedidos
col1, col2, col3 = st.columns(3)

# Seções dos pedidos com subheaders
with col1:
    st.markdown("<h3 style='text-align: center;'>Pedidos recebidos</h3>", unsafe_allow_html=True)
    if st.session_state.pedidos_recebidos:

        create_box(st.session_state.pedidos_recebidos, 'Atualizar para "Em andamento"', mover_para_em_andamento)
    else:
        st.markdown("<h5 style='text-align: center;'>Nenhum pedido recebido.</h5>", unsafe_allow_html=True)
with col2:
    st.markdown("<h3 style='text-align: center;'>Pedidos em andamento</h3>", unsafe_allow_html=True)
    if st.session_state.pedidos_em_andamento:

        create_box(st.session_state.pedidos_em_andamento, 'Atualizar para "Pronto"', mover_para_pronto)
    else:
        st.markdown("<h5 style='text-align: center;'>Nenhum pedido em andamento.</h5>", unsafe_allow_html=True)

with col3:
    st.markdown("<h3 style='text-align: center;'>Pedidos prontos</h3>", unsafe_allow_html=True)
    if st.session_state.pedidos_prontos:
        create_box(st.session_state.pedidos_prontos, "Concluir pedido", concluir_pedido)
    else:
        st.markdown("<h5 style='text-align: center;'>Nenhum pedido pronto para retirada.</h5>", unsafe_allow_html=True)


left, l_c, center, r_c, right = st.columns(5)

with center:
    st.image('insper.svg', use_column_width="auto")
