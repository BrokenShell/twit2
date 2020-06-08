import basilica
from credentials import Credentials


with basilica.Connection(Credentials.basilica_key) as con:
    pass
