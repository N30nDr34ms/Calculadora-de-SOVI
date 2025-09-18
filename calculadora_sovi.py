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
                f"{product} (cm)",
                min_value=0,
                value=0,
                key=f"{store_name}_{category}_{product}"
            )
        total_widths[category] = total
        category_totals[category] = sum(widths.values())

        # Mostrar tabela resumo de produtos
        df = pd.DataFrame({
            "Produto": list(widths.keys()),
            "Ocupação (cm)": list(widths.values()),
            "% na categoria": [round((w / total) * 100, 2) if total > 0 else 0 for w in widths.values()]
        })
        st.dataframe(df, use_container_width=True)

    # Calcular totais gerais para Real %
    total_geral = sum(category_totals.values())

    # Segundo pass: mostrar metas vs real por categoria
    for category in categories.keys():
        meta = metas[category]
        real = (category_totals[category] / total_geral * 100) if total_geral > 0 else 0
        diff = real - meta

        resumo_df = pd.DataFrame({
            "Categoria": [category],
            "Meta (%)": [meta],
            "Real (%)": [round(real, 2)],
            "Diferença (%)": [round(diff, 2)]
        })
        st.dataframe(resumo_df, use_container_width=True)

# Tabs para as lojas
tab1, tab2, tab3 = st.tabs(["Loja A", "Loja B", "Loja C"])

with tab1:
    show_store("Loja A")

with tab2:
    show_store("Loja B")

with tab3:
    show_store("Loja C")
