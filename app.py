
import oracledb
from datetime import datetime, timedelta


ultima_captura = datetime.now() - timedelta(hours=3) 

try:
    conexao = oracledb.connect(
        user="admin", 
        password="123", 
        dsn="mock_dsn"
    )
    print("Conexão estabelecida com sucesso.")
    
except oracledb.Error as e:
    
    print(f"Erro técnico detectado: {e}")

horario_liberacao = ultima_captura + timedelta(hours=2)
agora = datetime.now()

if agora >= horario_liberacao:
    print("Captura Liberada")
else:
    print("Habilidade em recarga")