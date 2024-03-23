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
    S -> '?' Atribuição 
        | '!' Expressão 
        | var '=' Expressão
    LA(S) = {'?', '!', var}


    Atribuição -> var '=' Expressão
    LA(Atribuição) = {var}


    Expressão -> Termo 
        | Expressão '+' Termo 
        | Expressão '-' Termo
    LA(Expressão) = {'(', var, num}


    Termo -> Fator 
        | Termo '*' Fator 
        | Termo '/' Fator
    LA(Termo) = {'(', var, num}


    Fator -> '(' Expressão ')' 
        | var 
        | num
    LA(Fator) = {'(', var, num}

## Frase exemplo
    ?a 
    b=a*2/(27-3)
    !a+b
    c=a*b/(a/b)

