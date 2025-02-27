import re

def convert_to_list( match ):
    itens = match.group( 0 ).strip().split( '\n' )
    itens_html = ''.join( [f'<li>{ re.sub( r"^\d+\.\s*", "", item ) }</li>' for item in itens] )
    return f'<ol>{ itens_html }</ol>'

def markdown_to_html( text_markdown ):
    # header
    text_html = re.sub( r'### (.+)', r'<h3>\1</h3>', text_markdown )
    text_html = re.sub( r'## (.+)', r'<h2>\1</h2>', text_html )
    text_html = re.sub( r'# (.+)', r'<h1>\1</h1>', text_html )

    # bold
    text_html = re.sub( r'\*\*(.+?)\*\*', r'<b>\1</b>', text_html )

    # italic
    text_html = re.sub( r'\*(.+?)\*', r'<i>\1</i>', text_html )

    # list
    text_html = re.sub( r'(\d+\.\s.+(\n|$))+', convert_to_list, text_html, flags=re.MULTILINE )

    # links
    text_html = re.sub( r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text_html )

    # images
    text_html = re.sub( r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', text_html )

    return text_html

if __name__ == '__main__':
    file_path = "TPC3/test.md"
    with open( file_path, 'r') as file:
        markdown = file.read()
    
    html = markdown_to_html( markdown )
    with open( 'TPC3/test.html', 'w') as file:
        file.write( html )
