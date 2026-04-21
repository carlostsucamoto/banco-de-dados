import oracledb
from datetime import datetime, timedelta
horario_liberacao = ultima_captura + timedelta(hours=2)
agora = datetime.now()
if horario_liberacao >= agora:
    print("Habilidade em recarga")
else:
    print("Captura Liberada")