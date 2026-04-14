from mcp.server.fastmcp import FastMCP
import mysql.connector
import os
from dotenv import load_dotenv

# Carichiamo le credenziali dal file .env
load_dotenv()

# Inizializziamo il server MCP
mcp = FastMCP("Portfolio-MySQL-Server")

# Configurazione database (usa l'utente mcp_user creato in precedenza)
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER_MCP", "mcp_user"),
        password=os.getenv("DB_PASS_MCP", ""),
        database=os.getenv("DB_NAME", "olist_ecommerce")
    )

@mcp.tool()
def list_tables() -> str:
    \"\"\"Elenca tutte le tabelle disponibili nel database e-commerce.\"\"\"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]
        conn.close()
        return f"Tabelle nel database: {', '.join(tables)}"
    except Exception as e:
        return f"Errore nel recupero delle tabelle: {str(e)}"

@mcp.tool()
def describe_table(table_name: str) -> str:
    \"\"\"Mostra la struttura (colonne e tipi) di una tabella specifica.\"\"\"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        conn.close()
        
        desc = f"Struttura di {table_name}:\n"
        for col in columns:
            desc += f"- {col[0]}: {col[1]}\n"
        return desc
    except Exception as e:
        return f"Errore: {str(e)}"

@mcp.tool()
def run_query(sql: str) -> str:
    \"\"\"Esegue una query SQL SELECT e restituisce i risultati in formato leggibile.\"\"\"
    # Sicurezza: blocchiamo query che non sono SELECT
    if not sql.strip().upper().startswith("SELECT"):
        return "Errore: Per motivi di sicurezza, sono permesse solo query SELECT."
        
    try:
        conn = get_db_connection()
        # Usiamo dictionary=True per avere risultati più chiari
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        
        if not results:
            return "Query completata. Nessun risultato trovato."
            
        # Formattazione semplice in tabella (primi 10 record)
        output = f"Risultati (primi {min(len(results), 10)} di {len(results)}):\n"
        for row in results[:10]:
            output += str(row) + "\n"
        return output
    except Exception as e:
        return f"Errore nell'esecuzione della query: {str(e)}"

if __name__ == "__main__":
    mcp.run()
