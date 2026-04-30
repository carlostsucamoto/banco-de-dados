from datetime import datetime, timedelta
from dotenv import load_dotenv
import oracledb
import os 


load_dotenv()
def obter_conexao():
    conexao = None
    try:
        conexao = oracledb.connect(user = os.getenv('DB_USER'), password = os.getenv('DB_PASSWORD'), dsn = os.getenv('DB_DSN'))

        print("Conexão estabelecida com sucesso.")
    
    except oracledb.Error as e:
        print(f"Erro técnico detectado: {e}")
    return conexao

jogador_logado = 1
conexao_ativa = obter_conexao()
try:
    if conexao_ativa is not None:
        meu_cursor = conexao_ativa.cursor()
        meu_cursor.execute("SELECT MAX(HORA_CAPTURA) FROM ALMASPASSAGEIRO WHERE ID_PASSAGEIRO =:id_passageiro",[jogador_logado])
        resultado = meu_cursor.fetchone()


        if resultado[0] is not None:
            data_ultima_captura = resultado[0]
            tempo_passado = datetime.now() - data_ultima_captura
            tempo_faltando = timedelta(hours=3) - tempo_passado

            if tempo_passado < timedelta(hours=3):
                print(f"Acesso Negado: Alma ainda não está aqui para ser capturada espere mais {tempo_faltando} horas.")
            else:
                print("Alma pronta para ser capturada.")

        else:
            print ("Alma pronta para ser capturada.")
        
        meu_cursor.close()       
    else:
        print("Sistema operando em modo degradado. Banco offline.")

    

finally:
    if conexao_ativa is not None:
        conexao_ativa.close()
        print("Conexão encerrada. Recursos liberados.")
