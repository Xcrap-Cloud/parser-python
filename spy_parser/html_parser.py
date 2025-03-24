from typing import Optional, Any
from parsel import Selector

from .parser import Parser

class HtmlParser(Parser):
    root: Selector
    
    def __init__(self, source) -> None:
        super().__init__(source)
        
        self.root = Selector(source)
        
    def parse_first(
        self,
        query: str,
        default: Optional[Any] = None
    ) -> Optional[str]:
        selector_list = self.root.css(query)
        
        if len(selector_list) == 0:
            return default
        
        data = selector_list.get()
        
        return data or default
    
    def parse_many(
        self,
        query: str,
        limit: Optional[int] = None
    ) -> list[str]:
        selector_list = self.root.css(query)
        items = []
        
        for selector in selector_list:
            if not limit is None and len(items) >= limit: break
            data = selector.get()
            items.append(data)
            
        return items