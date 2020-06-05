from basilica_service import con


if __name__ == '__main__':
    print(*con.embed_sentences(["Hello world!", "How are you?"]))
