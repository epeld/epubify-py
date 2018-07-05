import xml.etree.ElementTree as ET

def less_than(a, b):
    return a < b and abs(a - b) > 1.0

# Block transformations
def detect_paragraphs(block):
    prev_x = None
    prev_y2 = None
    p = ET.Element('p')
    ps = [p]
    ix = 0
    for l in block:
        bbox = l.attrib['bbox'].split()
        x = float(bbox[0])
        x2 = float(bbox[2])
        y = float(bbox[1])
        y2 = float(bbox[1])
        if not p.attrib.get('x', None):
            p.attrib['x'] = str(x)
            p.attrib['y'] = str(y)
            # p.attrib['x2'] = str(x2)
        p.attrib['index'] = str(ix)
        if prev_x and less_than(prev_x, x) and less_than(prev_y2, y):
            p = ET.Element('p')
            p.attrib['diff'] = str(x - prev_x)
            p.attrib['x'] = str(x)
            p.attrib['y'] = str(y)
            ps.append(p)
            ix = ix + 1
        prev_x = x
        prev_y2 = y2
        if len(l):
            for f in l.findall('.//font'):
                last = f
                p.append(f)
    return ps


def join_fonts(paragraph):
    if not paragraph:
        return
    first = paragraph[0]
    first.text = first.text.strip()
    for f in paragraph[1:]:
        if not f.text.strip():
            continue
        f.text = f.text.strip()
        if first.text:
            c = first.text[-1]
        else:
            c = ''
        if c == '-':
            first.text = first.text[:-1]
        else:
            if first.attrib.get('type') == f.attrib.get('type'):
                first.text = " ".join([first.text, f.text])
                paragraph.remove(f)
                continue
            else:
                first.text = first.text + " "
        first = f


def remove_empty_fonts(p):
    for f in p:
        if not f.text.strip():
            p.tag = 'span'

def transform(block):
    ps = detect_paragraphs(block)
    block.clear()
    for p in ps:
        remove_empty_fonts(p)
        join_fonts(p)
        block.append(p)
