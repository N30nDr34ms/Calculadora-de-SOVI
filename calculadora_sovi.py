import streamlit as st
import datetime

# Configuração da página
st.set_page_config(page_title="Calculadora SOVI", layout="centered")

st.title("📏 Calculadora de Ocupação de Prateleira - SOVI")

# Seleção da loja
loja = st.selectbox("Selecione a loja:", ["Loja A", "Loja B", "Loja C"])

# Categorias e produtos
categorias = {
    "Craft": ["Baden-Baden", "Praia Clássica", "Lagunitas", "Blue Moon"],
    "Premium": ["Heineken", "Heineken Zero"],
    "Mainstream": ["Praia Lager", "Amstel Ultra", "Amstel"]
}

# Entrada de dados e cálculos
st.subheader(f"🏬 {loja}")

for categoria, produtos in categorias.items():
    st.markdown(f"### {categoria}")
    total = st.number_input(f"Total da prateleira de {categoria} (cm):", min_value=1, value=1000)

    soma = 0
    dados = {}

    for produto in produtos:
        valor = st.number_input(f"{produto} (cm):", min_value=0, value=0, step=10)
        soma += valor
        dados[produto] = valor

    st.markdown(f"**Total preenchido:** {soma} cm / {total} cm")
    
    if soma > 0:
        for produto, valor in dados.items():
            perc = (valor / total) * 100
            st.write(f"- {produto}: {valor} cm → {perc:.1f}%")

# Data do registro
st.markdown("---")
st.caption(f"Registro feito em: {datetime.date.today().strftime('%d/%m/%Y')}")

