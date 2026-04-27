from dotenv import load_dotenv
import oracledb
import os 
load_dotenv()
from datetime import datetime, timedelta


ultima_captura = datetime.now() - timedelta(hours=3) 


def obter_conexao():
    conexao = None
    try:
        conexao = oracledb.connect(user = os.getenv('DB_USER'), password = os.getenv('DB_PASSWORD'), dsn = os.getenv('DB_DSN'))

        print("Conexão estabelecida com sucesso.")
    
    except oracledb.Error as e:
        print(f"Erro técnico detectado: {e}")
    return conexao


conexao_ativa = obter_conexao()
try:
    if conexao_ativa is not None:
        meu_cursor = conexao_ativa.cursor()
        meu_cursor.execute("SELECT MAX(HORA_CAPTURA) FROM ALMASPASSAGEIRO WHERE ID_PASSAGEIRO = 1")
        resultado = meu_cursor.fetchone()
        print(resultado)
        meu_cursor.close()
        
    else:
        print("Sistema operando em modo degradado. Banco offline.")

finally:
    if conexao_ativa is not None:
        conexao_ativa.close()
        print("Conexão encerrada. Recursos liberados.")
