
import oracledb
from datetime import datetime, timedelta


ultima_captura = datetime.now() - timedelta(hours=3) 


def obter_conexao():
    conexao = None
    try:
        conexao = oracledb.connect(user="admin", password="123", dsn="mock_dsn")

        print("Conexão estabelecida com sucesso.")
    
    except oracledb.Error as e:
        print(f"Erro técnico detectado: {e}")

    #finally:
        #print("Encerrando operação de arquivo.")
        #if conexao is not None:
            #conexao.close()
    return conexao


conexao_ativa = obter_conexao()
try:
    if conexao_ativa is not None:
        print("Simulando execução de query DQL")
    else:
        print("Sistema operando em modo degradado. Banco offline.")

finally:
    if conexao_ativa is not None:
        conexao_ativa.close()
        print("Conexão encerrada. Recursos liberados.")
