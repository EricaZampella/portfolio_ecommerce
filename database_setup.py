import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Carica variabili d'ambiente (se presenti)
load_dotenv()

# Configurazione - MODIFICA QUESTI VALORI o usa un file .env
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")  # Inserisci la tua password qui
DB_NAME = "olist_ecommerce"

def setup_database():
    print(f"--- Inizio Setup Database: {DB_NAME} ---")
    
    # 1. Connessione iniziale per creare il database
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print(f"Database '{DB_NAME}' verificato/creato.")
        conn.close()
    except Exception as e:
        print(f"Errore nella creazione del database: {e}")
        return

    # 2. Esecuzione dello Schema SQL
    engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
    
    try:
        with open("schema.sql", "r") as f:
            schema_sql = f.read()
            # Dividiamo il file in singole query
            with engine.connect() as connection:
                for statement in schema_sql.split(";"):
                    if statement.strip():
                        connection.execute(text(statement))
                connection.commit()
        print("Schema SQL applicato correttamente.")
    except Exception as e:
        print(f"Errore nell'applicazione dello schema: {e}")
        return

    # 3. Importazione dei CSV
    # Mappatura File CSV -> Nome Tabella
    csv_mapping = {
        "olist_customers_dataset.csv": "customers",
        "olist_sellers_dataset.csv": "sellers",
        "olist_products_dataset.csv": "products",
        "olist_orders_dataset.csv": "orders",
        "olist_order_items_dataset.csv": "order_items",
        "olist_order_payments_dataset.csv": "order_payments",
        "olist_order_reviews_dataset.csv": "order_reviews",
        "olist_geolocation_dataset.csv": "geolocation",
        "product_category_name_translation.csv": "product_category_name_translation"
    }

    data_path = "data/"
    
    for filename, table_name in csv_mapping.items():
        file_full_path = os.path.join(data_path, filename)
        if os.path.exists(file_full_path):
            print(f"Importazione di {filename} nella tabella {table_name}...")
            try:
                # Carichiamo i dati con Pandas
                df = pd.read_csv(file_full_path)
                
                # Pulizia nomi colonne (opzionale ma consigliato)
                df.columns = [c.strip() for c in df.columns]
                
                # Importazione su SQL
                # Usiamo 'append' per non distruggere lo schema creato manualmente
                df.to_sql(table_name, con=engine, if_exists='append', index=False, chunksize=1000)
                print(f"OK: {len(df)} righe caricate.")
            except Exception as e:
                print(f"Errore durante l'importazione di {filename}: {e}")
        else:
            print(f"ATTENZIONE: File {file_full_path} non trovato. Salto...")

    print("--- Setup Completato! ---")

if __name__ == "__main__":
    setup_database()
