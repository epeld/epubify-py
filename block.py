import xml.etree.ElementTree as ET

# Block transformations
def detect_paragraphs(block):
    prev_x = None
    p = ET.Element('p', {'first': "true"})
    ps = [p]
    for l in block:
        bbox = l.attrib['bbox'].split()
        x = float(bbox[0])
        x2 = float(bbox[2])
        if prev_x and prev_x < x:
            p = ET.Element('p')
            ps.append(p)
        prev_x = x
        for f in l:
            p.append(f)
    if ps:
        ps[-1].attrib['last'] = "true"
    return ps


def transform(block):
    ps = detect_paragraphs(block)
    block.clear()
    for p in ps:
        block.append(p)
