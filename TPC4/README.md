# Analisador léxico

## Autor

Jéssica Cristina Lima da Cunha, A100901

## Implementação

Este TPC tinha por objetivo implementar uma análise léxica para uma consulta SQL. Desta forma, foi codificado um programa que usa expressões regulares para identificar diferentes tokens, como palavras-chave (`SELECT`, `FROM`, `WHERE`), identificadores (por exemplo: `id`, `nome`, `salario`, `empregado`), números inteiros e operadores de comparação (`>=`, `<=`, `>`, `<`, `=`, `!=`). A função `analisar_lexico` realiza a análise léxica, retornando uma lista de tokens encontrados na consulta SQL fornecida. O resultado é impresso no final.
