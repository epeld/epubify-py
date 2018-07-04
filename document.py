import xml.etree.ElementTree as ET

import page as pagem

def transform(document):
    for page in document:
        pagem.transform(page)

    for page in document:
        document.remove(page)
        for c in page:
            document.append(c)

    return document


def join_page(document, page):
    ps = page.findall('p')
    for p in ps:
        document.append(p)
