from spy_parser import HtmlParsingModel

print("Parsing HTML")

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