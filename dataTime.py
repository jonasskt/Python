from datetime import datetime
from datetime import timedelta, timezone
import time
import os


dia = datetime.now()
diferenca = timedelta(hours=-3)
hora = timezone(diferenca)
hora_att = dia.astimezone(hora)
hora_at = hora_att.strftime('%H:%M:%S')


        