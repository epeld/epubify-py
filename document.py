import xml.etree.ElementTree as ET

import page as pagem

def transform(document):
    for page in document:
        pagem.transform(page)
    # reduce(join_page, list(document), document)


def join_page(document, page):
    pass
