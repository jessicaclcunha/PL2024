import re

def mdToHTML(text):
    html_output = []
    in_ordered_list = False
    in_unordered_list = False
    in_blockquote = False

    def close_lists_and_blockquote():
        nonlocal in_ordered_list, in_unordered_list, in_blockquote
        if in_ordered_list:
            html_output.append('</ol>')
            in_ordered_list = False
        elif in_unordered_list:
            html_output.append('</ul>')
            in_unordered_list = False
        elif in_blockquote:
            html_output.append('</blockquote>')
            in_blockquote = False

    for line in text.split('\n'):
        # Headers
        header_match = re.match(r'^(#{1,6})\s(.*)', line)
        if header_match:
            close_lists_and_blockquote()
            html_output.append(f'<h{len(header_match.group(1))}>{header_match.group(2)}</h{len(header_match.group(1))}>')
            continue

        # Bold
        line = re.sub(r'\*\*(.*?)\*\*|__(.*?)__', r'<b>\1\2</b>', line)

        # Itálico
        line = re.sub(r'\*(.*?)\*|_(.*?)_', r'<i>\1\2</i>', line)

        # Image
        line = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', line)

        # Link
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)

        # Lists
        ordered_list_match = re.match(r'^(\d+\.\s)(.*)', line)
        unordered_list_match = re.match(r'^([*+-]\s)(.*)', line)

        if ordered_list_match:
            if not in_ordered_list:
                close_lists_and_blockquote()
                html_output.append('<ol>')
                in_ordered_list = True
            html_output.append(f'<li>{ordered_list_match.group(2)}</li>')
        elif unordered_list_match:
            if not in_unordered_list:
                close_lists_and_blockquote()
                html_output.append('<ul>')
                in_unordered_list = True
            html_output.append(f'<li>{unordered_list_match.group(2)}</li>')
        elif line.startswith('</li>'):
            if in_ordered_list or in_unordered_list:
                html_output.append('</li>')
        else:
            # Blockquote
            blockquote_match = re.match(r'^>\s(.*)', line)
            if blockquote_match:
                close_lists_and_blockquote()
                html_output.append('<blockquote>')
                in_blockquote = True
                html_output.append(f'<p>{blockquote_match.group(1)}</p>')
            elif in_blockquote:
                in_blockquote = False
                html_output.append('</blockquote>')
                html_output.append(line)
            else:
                html_output.append(line)

    close_lists_and_blockquote()
    return '\n'.join(html_output)

# Exemplo de uso
markdown_input = """
# Título
Este é um **exemplo** de conversor de *Markdown para HTML*.

## Lista Numerada
1. Primeiro item
2. Segundo item
3. Terceiro item

### Lista Não Numerada
* Item 1
* Item 2
* Item 3

#### Link e Imagem
Como pode ser consultado em [página da UC](http://www.uc.pt).

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com).

> Isto é um blockquote.

Outro parágrafo.
"""

html_output = mdToHTML(markdown_input)
print(html_output)
