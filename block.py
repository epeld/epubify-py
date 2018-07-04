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
        if len(l):
            last = None
            for f in l.findall('.//font'):
                last = f
                p.append(f)

            # Try to remove trailing '-'s
            if last is not None:
                # print(last.text)
                if last.text[-1].strip() == "-":
                    # print(last.text)
                    last.text = last.text.strip()[:-1]
    if ps:
        ps[-1].attrib['last'] = "true"
    return ps


def transform(block):
    ps = detect_paragraphs(block)
    block.clear()
    for p in ps:
        block.append(p)
