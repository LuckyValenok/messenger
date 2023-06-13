from datetime import datetime

from schemas.message import MessageWithUserOutScheme
from schemas.user import UserWithoutPassword

print(MessageWithUserOutScheme(id=1, text='123', edited=False, read=False,
                         created_date=datetime(2023, 6, 13, 8, 4, 41, 942199),
                         user=UserWithoutPassword(id=1, login='fdfsa', name='fkdjaf', deleted=False)).json())
