# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
    O campo disponivel serve para indicar se um livro está disponível para empréstimo.
    Quando o valor é True, o livro está disponível. Quando é False, o livro está emprestado.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
    O session.commit() serve para salvar no banco de dados as alterações realizadas.
    Ele é necessário após emprestar ou devolver um livro para que a alteração no campo disponivel seja persistida.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
    O relacionamento entre Livro e Autor é usado nas consultas. Em listar_livros(), por exemplo, usamos livro.autor.nome para acessar o nome do autor de cada livro.
    Também usamos autor.livros em listar_livros_por_autor() para acessar os livros relacionados a um autor.