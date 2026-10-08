from models import Autor, Livro


def popular_banco(session):
    autores = [
        Autor(nome="J.K. Rowling", pais="Reino Unido"),
        Autor(nome="Machado de Assis", pais="Brasil"),
        Autor(nome="George Orwell", pais="Reino Unido")
    ]

    session.add_all(autores)
    session.commit()

    livros = [
        Livro(
            titulo="Harry Potter e a Pedra Filosofal",
            ano=1997,
            autor=autores[0],
            disponivel=True
        ),
        Livro(
            titulo="Harry Potter e a Câmara Secreta",
            ano=1998,
            autor=autores[0],
            disponivel=False
        ),
        Livro(
            titulo="Harry Potter e o Prisioneiro de Azkaban",
            ano=1999,
            autor=autores[0],
            disponivel=True
        ),
        Livro(
            titulo="Dom Casmurro",
            ano=1899,
            autor=autores[1],
            disponivel=True
        ),
        Livro(
            titulo="Memórias Póstumas de Brás Cubas",
            ano=1881,
            autor=autores[1],
            disponivel=False
        ),
        Livro(
            titulo="1984",
            ano=1949,
            autor=autores[2],
            disponivel=True
        )
    ]

    session.add_all(livros)
    session.commit()