#!/usr/bin/env python3
"""
cria_autores.py
Gera arquivos de autores em src/content/autores/ baseado na lista de nomes.

Uso:
    python cria_autores.py
"""

import unicodedata
from pathlib import Path

AUTORES = [
    "Adolfo Guimarães",
    "Carol Cavaleiro",
    "Carolina Leslie",
    "Déborah Mesquita",
    "Elijah Meeks",
    "Eliza Fernandes",
    "Elmo Neto",
    "Fernando Barbalho",
    "Fernando Hannaka",
    "Gabriel Vaz de Melo",
    "Gabriela Momberg",
    "Gabriella S. de Macedo",
    "Glaudemias G. Junior",
    "Igor Falconieri",
    "Isabela Noronha",
    "Juliana Freitas",
    "Ligia Galvão",
    "Lucas Gomes",
    "Marck AI",
    "Mauro Pinheiro",
    "Olga Lopes",
    "Ricardo Brasileiro",
    "Ricardo Cunha Lima",
    "Rodolfo Almeida",
    "Rodrigo Menegat",
    "Salomé Esteves",
    "Stephanie Evergreen",
    "Tatyana Mendes",
    "Vinícius C. Barqueiro",
    "William R. Cordeiro",
]

def slugify(nome):
    """Converte nome em slug: minúsculas, sem acentos, espaços → hífens"""
    # remove acentos
    slug = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    # minúsculas
    slug = slug.lower()
    # espaços/pontos → hífens
    slug = slug.replace(" ", "-").replace(".", "")
    # remove hífens múltiplos
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")

def gerar_frontmatter(nome, slug):
    """Gera o frontmatter YAML pro arquivo do autor"""
    return f"""---
nome: {nome}
quem_e: Colaborador da comunidade datavizbr.
papel: recorrente
ativo: true
---

Contributor do datavizbr."""

def main():
    autores_dir = Path("src/content/autores")
    autores_dir.mkdir(parents=True, exist_ok=True)
    
    criados = []
    duplicados = []
    
    for nome in AUTORES:
        slug = slugify(nome)
        arquivo = autores_dir / f"{slug}.md"
        
        if arquivo.exists():
            duplicados.append(f"{nome} ({slug}.md já existe)")
            continue
        
        conteudo = gerar_frontmatter(nome, slug)
        arquivo.write_text(conteudo, encoding="utf-8")
        criados.append(f"{nome} → {slug}.md")
    
    print(f"✓ Criados: {len(criados)} arquivos")
    for c in criados:
        print(f"  {c}")
    
    if duplicados:
        print(f"\n⚠ Já existem: {len(duplicados)}")
        for d in duplicados:
            print(f"  {d}")
    
    print(f"\nPróximo passo: atualize seu frontmatter dos posts com os IDs (slugs) dos autores:")
    print("  autores:")
    print("    - adolfo-guimaraes")
    print("    - carol-cavaleiro")
    print("  etc...")

if __name__ == "__main__":
    main()