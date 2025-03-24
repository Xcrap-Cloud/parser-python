from spy_parser import HtmlParsingModel, HtmlParser

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

parser = HtmlParser(html)

title = parser.parse_first("title::text")
headings = parser.parse_many("h1::text")

print(f"Title: {title}")
print(f"Headings: {headings}")