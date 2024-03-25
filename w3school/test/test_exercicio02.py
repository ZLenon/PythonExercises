from exercicios import exercicio02


def test_comentario_hastagh_comun():
    classe = exercicio02.ClasseComentarios()
    result = classe.metodo_comentario_hashtag()
    assert result == "Esse é um comentario com hashtag"


def test_comentario_aspas_tripla():
    classe = exercicio02.ClasseComentarios()
    result = classe.metodo_comentario_aspas_tripla()
    assert result == "\nEsse é um comentario com tres aspas\n"
