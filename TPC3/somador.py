import re

def somador_onOff(texto):
    somar = False
    soma_atual = 0

    padrao = re.compile(r'([Oo][Nn]|[Oo][Ff]{2}|=|\d+)', re.IGNORECASE)
    matches = padrao.finditer(texto)

    for match in matches:
        type = match.group()

        if 'on' == type.lower():
            somar = True
            
        if 'off' == type.lower():
            somar = False
            
        if type.isdigit() and somar:
            soma_atual += int(type)
            
        if '=' == type:         
            print(f'soma: {soma_atual}')
            

text = '''2 on 
        isto é para testar =
        3, 5 off 1. =
        Onsó mais 4 alguns OFF 2
        ='''   

somador_onOff(text)
