import streamlit as st
import pandas as pd

# Estrutura fixa de categorias e produtos na ordem do Excel
categories = {
    "Craft": ["Baden Baden", "Praya Clássica", "Lagunitas", "Blue Moon"],
    "Premium": ["Heineken", "Heineken 0.0", "Praya Lager", "Amstel Ultra"],
    "Mainstream": ["Amstel"]
}

# Função para exibir uma loja
def show_store(default_name):
    store_name = st.text_input("Nome da loja:", value=default_name, key=f"name_{default_name}")
    st.subheader(f"{store_name}")

    total_widths = {}
    percentages = {}

    for category, products in categories.items():
        st.markdown(f"### {category}")
        total = st.number_input(f"Tamanho total da prateleira ({category}) em cm:", min_value=1, value=1000, key=f"{store_name}_{category}_total")
        widths = {}
        for product in products:
            widths[product] = st.number_input(
                f"{product} (cm)",
                min_value=0,
                value=0,
                key=f"{store_name}_{category}_{product}"
            )
        total_widths[category] = total
        percentages[category] = {p: (w / total) * 100 if total > 0 else 0 for p, w in widths.items()}

        # Mostrar tabela resumo
        df = pd.DataFrame({
            "Produto": list(widths.keys()),
            "Ocupação (cm)": list(widths.values()),
            "% na categoria": [round(percentages[category][p], 2) for p in widths.keys()]
        })
        st.dataframe(df, use_container_width=True)

# Tabs para as lojas
tab1, tab2, tab3 = st.tabs(["Loja A", "Loja B", "Loja C"])

with tab1:
    show_store("Loja A")

with tab2:
    show_store("Loja B")

with tab3:
    show_store("Loja C")
        for produto, valor in dados.items():
            perc = (valor / total) * 100
            st.write(f"- {produto}: {valor} cm → {perc:.1f}%")

# Data do registro
st.markdown("---")
st.caption(f"Registro feito em: {datetime.date.today().strftime('%d/%m/%Y')}")

