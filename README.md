# Spy Parser

Spy Parser é um Parser declarativo orientado a modelos para extração de dados de arquivos HTML e JSON podendo intercalar os dois para extrair mais dados.

Ele é inspirado do parser que vem embutido do Xcrap Framework que está disponível pra Node.js, foi construido utilizando o Parsel para parsing de HTML e JMESPath para parsing de JSON.

## Instalação

```cmd
pip install spy-parser
```

## Uso simples

```python
from spy_parser import HtmlParsingModel

html = "<html><title>Title</title><body><h1>Heading</h1></body></html>"

root_parsing_model = HtmlParsingModel({
    "title": {
        "query": "title::text"
    },
    "heading": {
        "query": "h1::text"
    }
})

data = root_parsing_model.parse(html)

print(data)
```