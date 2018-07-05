import xml.etree.ElementTree as ET

import page as pagem
import block as blockm

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
    head.append(ET.fromstring('<style>p { border-top: solid 2px red }</style>'))

    convert_headings(clone)
    join_paragraphs(document)

    return clone


def convert_headings(document):
    for p in document.findall('.//*/p'):
        fs = p.findall(".//font")
        for f in fs:
            if f.attrib['type'] == 'h2':
                p.tag = 'h2'
                p.attrib['converted'] = 'true'
                for c in p:
                    c.tag = 'span'
                break


def join_page(document, page):
    ps = page.findall('.//p')
    for p in ps:
        document.append(p)

def join_paragraphs(document):
    ps = document.findall('.//p')
    if not ps:
        return
    prev = ps[0]
    for p in ps[1:]:
        if prev.attrib.get('last', None) and p.attrib.get('first'):
            # print(prev.attrib)
            x1 = float(prev.attrib.get('x'))
            x2 = float(p.attrib.get('x'))
            if not blockm.less_than(x1, x2):
                for c in p:
                    prev.append(c)
                p.clear()
                p.attrib['merged'] = 'true'
                p.tag = 'span'
                continue
        prev = p
