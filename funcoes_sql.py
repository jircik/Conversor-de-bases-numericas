import sqlite3

def conectar_banco():
    try:
        return sqlite3.connect("hisoricoDeConversoes.db")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def criar_tabela():
    conn = None
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL,
            from_base INTEGER NOT NULL,
            to_base INTEGER NOT NULL,
            result TEXT NOT NULL
        )
        """)
        conn.commit()
        #print("Tabela 'historico' criada com sucesso ou já existe.")
    except sqlite3.Error as e:
        print(f"Erro ao criar ou acessar tabela: {e}")
    finally:
        if conn:
            conn.close()

def adicionar_conversao(number, from_base, to_base, result):
    conn = None
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO historico (number, from_base, to_base, result)
            VALUES (?, ?, ?, ?)
        """, (number, from_base, to_base, result))
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Erro ao adicionar conversão: {e}")
    finally:
        if conn:
            conn.close()

def listar_conversoes():
    conn = None
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM historico")
        historico = cursor.fetchall() 
        return historico
    except sqlite3.Error as e:
        print(f"Erro ao listar conversões: {e}")
        return []
    finally:
        if conn:
            conn.close()


def buscar_conversao_existente(number, from_base, to_base):
    conn = None
    try:
        conn = sqlite3.connect("hisoricoDeConversoes.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT result FROM historico 
            WHERE number = ? AND from_base = ? AND to_base = ?
        """, (number, from_base, to_base))
        conversao = cursor.fetchone()
        return conversao[0] if conversao else None
    except sqlite3.Error as e:
        print(f"Erro ao buscar conversão: {e}")
        return None
    finally:
        if conn:
            conn.close()

def limpar_historico():
    conn = None
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM historico")
        conn.commit()
        print("Histórico de conversões limpo com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao limpar histórico: {e}")
    finally:
        if conn:
            conn.close()