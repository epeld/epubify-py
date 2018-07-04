import xml.etree.ElementTree as ET

import page as pagem

def transform(document):
    if False:
        for page in document[5:]:
            document.remove(page)

    for page in document:
        pagem.transform(page)

    ps = document.findall('.//p')
    clone = ET.Element('html')
    body = ET.SubElement(clone, 'body')
    for p in ps:
        body.append(p)

    return clone


def join_page(document, page):
    ps = page.findall('.//p')
    for p in ps:
        document.append(p)
