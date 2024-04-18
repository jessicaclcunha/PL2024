# Gramática Independente de Contexto

## Autor

Jéssica Cristina Lima da Cunha, A100901

## Implementação

### Terminais
    T = {'?', var, '=', '*', num, '/', '(', ')', '-', '!'}

### Não-terminais
    N = {S, Atribuição, Expressão, Termo, Fator}

### Símbolo Inicial
    S

### Produções
    S -> '?' Atribuição          | LA = {'?'}
        | '!' Expressão          | LA = {'!'}
        | var '=' Expressão      | LA = {var}


    Atribuição -> var '=' Expressão


    Expressão -> ε               | LA = {')'}
        | '+' Termo              | LA = {'+'}
        | '-' Termo              | LA = {'-'}


    Termo -> ε                   |  LA = {'+', '-', ')'}
        | '*' Fator              |  LA = {'*''}
        | '/' Fator              |  LA = {'/''}


    Fator -> '(' Expressão ')'   |  LA = {'('}
        | var                    |  LA = {var}
        | num                    |  LA = {num}

## Frase exemplo
    ?a 
    b=a*2/(27-3)
    !a+b
    c=a*b/(a/b)