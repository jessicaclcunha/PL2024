import re

class MarkdownConverter:
    def __init__(self):
        self.html_output = []
        self.in_ordered_list = False
        self.in_unordered_list = False
        self.in_blockquote = False

    def md_to_html(self, text):
        for line in text.split('\n'):
            # Headers
            header_match = re.match(r'^(#{1,6})\s(.*)', line)
            if header_match:
                self.close_lists_and_blockquote()
                self.html_output.append(f'<h{len(header_match.group(1))}>{header_match.group(2)}</h{len(header_match.group(1))}>')
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
                self.close_lists_and_blockquote()
                self.html_output.append('<ol>')
                self.in_ordered_list = True
                self.html_output.append(f'<li>{ordered_list_match.group(2)}</li>')
            elif unordered_list_match:
                self.close_lists_and_blockquote()
                self.html_output.append('<ul>')
                self.in_unordered_list = True
                self.html_output.append(f'<li>{unordered_list_match.group(2)}</li>')
            elif line.startswith('</li>'):
                if self.in_ordered_list or self.in_unordered_list:
                    self.html_output.append('</li>')
            else:
                # Blockquote
                blockquote_match = re.match(r'^>\s(.*)', line)
                if blockquote_match:
                    self.close_lists_and_blockquote()
                    self.html_output.append('<blockquote>')
                    self.in_blockquote = True
                    self.html_output.append(f'<p>{blockquote_match.group(1)}</p>')
                elif self.in_blockquote:
                    self.in_blockquote = False
                    self.html_output.append('</blockquote>')
                    self.html_output.append(line)
                else:
                    self.html_output.append(line)

        self.close_lists_and_blockquote()
        return '\n'.join(self.html_output)

    def close_lists_and_blockquote(self):
        if self.in_ordered_list:
            self.html_output.append('</ol>')
            self.in_ordered_list = False
        elif self.in_unordered_list:
            self.html_output.append('</ul>')
            self.in_unordered_list = False
        elif self.in_blockquote:
            self.html_output.append('</blockquote>')
            self.in_blockquote = False

# Exemplo de uso
markdown_input = """
# Título
Este é um **exemplo** de conversor de Markdown para HTML.

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

converter = MarkdownConverter()
html_output = converter.md_to_html(markdown_input)
print(html_output)
