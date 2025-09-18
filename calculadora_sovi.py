import streamlit as st
import pandas as pd

# Estrutura fixa de categorias e produtos na ordem do Excel
categories = {
    "Craft": ["Baden Baden", "Praya Clássica", "Lagunitas", "Blue Moon"],
    "Premium": ["Heineken", "Heineken 0.0", "Praya Lager", "Amstel Ultra"],
    "Mainstream": ["Amstel"]
}

# Metas fixas (%)
metas = {
    "Craft": 26,
    "Premium": 40,
    "Mainstream": 30
}

# Função para exibir uma loja
def show_store(default_name):
    store_name = st.text_input("Nome da loja:", value=default_name, key=f"name_{default_name}")
    st.subheader(f"{store_name}")

    # Guardar totais da loja
    total_widths = {}
    category_totals = {}

    # Primeiro pass: calcular ocupação de cada categoria
    for category, products in categories.items():
        st.markdown(f"### {category}")
        total = st.number_input(
            f"Tamanho total da prateleira ({category}) em cm:",
            min_value=1,
            value=1000,
            key=f"{store_name}_{category}_total"
        )
        widths = {}
        for product in products:
            widths[product] = st.number_input(
