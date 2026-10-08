from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    livros = session.scalars(select(Livro)).all()

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"{livro.titulo} - {livro.autor.nome} - {status}")

    return livros


def listar_livros_disponiveis(session):
    livros = session.scalars(select(Livro).where(Livro.disponivel == True)).all()

    for livro in livros:
        print(f"{livro.titulo} - {livro.autor.nome}")

    return livros


def buscar_livros_por_titulo(session, trecho):
    livros = session.scalars(select(Livro).where(Livro.titulo.contains(trecho))).all()

    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"{livro.titulo} - {livro.autor.nome} - {status}")

    return livros


def listar_livros_por_autor(session, nome_autor):
    autor = session.scalar(select(Autor).where(Autor.nome == nome_autor))

    if autor is None:
        print("Autor não encontrado.")
        return []

    for livro in autor.livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"{livro.titulo} - {status}")

    return autor.livros