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
    head = ET.SubElement(clone, 'head')
    body = ET.SubElement(clone, 'body')
    for p in ps:
        body.append(p)

    head.append(ET.fromstring('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>'))

    for p in clone.findall('.//*/p'):
        fs = p.findall(".//font")
        for f in fs:
            if f.attrib['type'] == 'h2':
                p.tag = 'h2'
                p.attrib['converted'] = 'true'
                for c in p:
                    c.tag = 'span'
                break

    return clone


def join_page(document, page):
    ps = page.findall('.//p')
    for p in ps:
        document.append(p)
