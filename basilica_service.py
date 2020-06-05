import requests
import basilica
from credentials import Credentials


if __name__ == '__main__':

    with basilica.Connection(Credentials.basilica_key) as c:
        embeddings = c.embed_sentences(["Hello world!", "How are you?"])
        print(list(embeddings))
