import re

sql_query = "select id, nome, salary from empregado where salario>=820"

# Definindo padrões de expressões regulares para tokens SQL
regex_patterns = [
    r'\bselect\b',     # SELECT
    r'\bfrom\b',       # FROM
    r'\bwhere\b',      # WHERE
    r'\b\w+\b',        # Identificadores (por exemplo: id, nome, salary, empregado)
    r'\b\d+\b',        # Números inteiros
    r'>=|<=|>|<|=|!=',  # Operadores de comparação
]

# Função para realizar a análise léxica
def analisar_lexico(query):
    tokens = set()

    # Iterar sobre as padrões de expressões regulares
    for pattern in regex_patterns:
        matches = re.finditer(pattern, query, re.IGNORECASE)

        if matches:
            tokens.update(match.group() for match in matches)

    return list(tokens)

# Executar a análise léxica
resultado_lexico = analisar_lexico(sql_query)
print(resultado_lexico)
