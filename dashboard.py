import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Page Config
st.set_page_config(page_title="Olist BI Dashboard",
                   layout="wide", initial_sidebar_state="expanded")

# Load CSS for better styling
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    /* Estetica Premium per i Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 28px;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")


@st.cache_resource
def get_engine():
    try:
        return create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
    except Exception as e:
        st.error(f"Errore connessione DB: {e}")
        return None


engine = get_engine()

# --- Sidebar ---
st.sidebar.title("🛠️ Olist BI")
st.sidebar.write("Monitoraggio Performance")

# --- Top Row: KPIs ---
st.title("📊 Business Intelligence Dashboard")
st.markdown("---")

if engine:
    try:
        # --- Top Row: KPIs ---
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            res = pd.read_sql(
                "SELECT COUNT(order_id) as c FROM orders", engine)
            val = res['c'][0] if not res.empty else 0
            st.metric("Ordini Totali", f"{val:,}".replace(",", "."))

        with col2:
            res = pd.read_sql(
                "SELECT SUM(payment_value) as s FROM order_payments", engine)
            val = res['s'][0] if not res.empty and res['s'][0] is not None else 0
            val_m = val / 1_000_000
            st.metric("Fatturato Lordo", f"R$ {val_m:,.2f}".replace(
                ",", "X").replace(".", ",").replace("X", ".") + " M")

        with col3:
            res = pd.read_sql(
                "SELECT AVG(review_score) as a FROM order_reviews", engine)
            val = res['a'][0] if not res.empty and res['a'][0] is not None else 0
            st.metric("Rating Medio", f"{val:.2f}".replace(".", ",") + " / 5")

        with col4:
            res = pd.read_sql(
                "SELECT COUNT(DISTINCT customer_unique_id) as c FROM customers", engine)
            val = res['c'][0] if not res.empty else 0
            st.metric("Clienti Unici", f"{val:,}".replace(",", "."))

        # --- Second Row: Sales & Logistics ---
        st.markdown("### 📈 Trend e Logistica")
        c1, c2 = st.columns(2)

        with c1:
            df_sales = pd.read_sql("""
                SELECT DATE_FORMAT(order_purchase_timestamp, '%Y-%m-01') as month, SUM(payment_value) as revenue
                FROM orders o JOIN order_payments op ON o.order_id = op.order_id
                GROUP BY month ORDER BY month
            """, engine)
            if not df_sales.empty:
                fig_sales = px.area(df_sales, x='month', y='revenue',
                                    title="Evoluzione Fatturato Mensile", color_discrete_sequence=['#2ecc71'])
                st.plotly_chart(fig_sales, use_container_width=True)
            else:
                st.info("Nessun dato di vendita trovato.")

        with c2:
            df_delivery = pd.read_sql("""
                SELECT customer_state, AVG(DATEDIFF(order_delivered_customer_date, order_purchase_timestamp)) as days
                FROM orders o JOIN customers c ON o.customer_id = c.customer_id
                WHERE order_status = 'delivered'
                GROUP BY customer_state ORDER BY days ASC
            """, engine)
            if not df_delivery.empty:
                fig_del = px.bar(df_delivery, x='customer_state', y='days',
                                 title="Tempi Consegna Medi per Stato", color='days', color_continuous_scale='Viridis')
                st.plotly_chart(fig_del, use_container_width=True)
            else:
                st.info("Nessun dato logistico trovato.")

        # --- Third Row: Categories ---
        st.subheader("📦 Top Categorie per Vendite")
        df_cat = pd.read_sql("""
            SELECT p.product_category_name, COUNT(oi.order_id) as orders
            FROM order_items oi JOIN products p ON oi.product_id = p.product_id
            GROUP BY 1 ORDER BY 2 DESC LIMIT 10
        """, engine)
        if not df_cat.empty:
            fig_cat = px.pie(df_cat, names='product_category_name', values='orders',
                             hole=0.3, color_discrete_sequence=px.colors.sequential.RdBu)
            fig_cat.update_layout(
                legend=dict(
                    font=dict(size=18),
                    x=0.8,
                    xanchor='left'
                )
            )
            st.plotly_chart(fig_cat, use_container_width=True)
        else:
            st.info("Nessun dato sulle categorie trovato.")

    except Exception as e:
        st.error(
            f"Si è verificato un errore durante il caricamento dei dati: {e}")
else:
    st.warning(
        "Connessione al database non inizializzata. Controlla il file .env.")

st.sidebar.markdown("---")
if st.sidebar.button("🔄 Forza Aggiornamento"):
    st.cache_resource.clear()
    st.rerun()

st.info("La dashboard si aggiorna automaticamente ad ogni modifica dei dati nel database.")
