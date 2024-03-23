import re

def somador_onOff(texto):
    somar = True
    soma_atual = 0
    
    padrao = re.compile(r'([Oo][Nn]|[Oo][Ff]{2}|=|\b(?:\w*\d+\w*|\d+)\b)', re.IGNORECASE)
    matches = padrao.finditer(texto)

    for match in matches:
        type = match.group()

        if 'on' == type.lower():
            somar = True
            
        if 'off' == type.lower():
            somar = False
            
        if re.search(r'\b\d+\b', type) and somar:
            soma_atual += int(type)
            
        if '=' == type:         
            print(f'soma: {soma_atual}')

# Exemplo de texto
text = '''on 
        isto é para testar =
        3, 5 off 1. =
        Onsó mais -4 alguns 
        no meio de pa10vrasOFF 2
        ='''   

somador_onOff(text)