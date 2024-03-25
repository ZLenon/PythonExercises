class ClasseComentarios:
    def metodo_comentario_hashtag(self):
        # comentario simples com hashtag
        return "Esse é um comentario com hashtag"

    def metodo_comentario_aspas_tripla(self):
        return """
Esse é um comentario com tres aspas
"""


# ---------------------------------------------------
classe = ClasseComentarios()
# ---------------------------------------------------
metodo_um = classe.metodo_comentario_hashtag()
print(metodo_um)
# ---------------------------------------------------
metodo_dois = classe.metodo_comentario_aspas_tripla()
print(metodo_dois)
