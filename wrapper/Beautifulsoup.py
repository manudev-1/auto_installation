from typing import Any, Sequence, Union, IO
from bs4 import BeautifulSoup as BS
from bs4.builder import TreeBuilder
from bs4.element import PageElement as PageElement, SoupStrainer as SoupStrainer

class BeautifulSoup(BS):
    def __init__(self, 
                 markup: Union[str, bytes, IO[str], IO[bytes]] = "", 
                 features: Union[str, Sequence[str], None] = None, 
                 builder: Union[TreeBuilder, type[TreeBuilder], None] = None, 
                 parse_only: Union[SoupStrainer, None] = None, 
                 from_encoding: Union[str, None] = None, 
                 exclude_encodings: Union[Sequence[str], None] = None, 
                 element_classes: Union[dict[type[PageElement], type[Any]], None] = None, 
                 **kwargs) -> None:
        super().__init__(markup, features, builder, parse_only, from_encoding, exclude_encodings, element_classes, **kwargs)