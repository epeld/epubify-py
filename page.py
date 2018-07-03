import block as blockm

# Page transformations

def concatenate_chars(page):
    fonts = page.findall('.//*font')
    for f in fonts:
        size = f.attrib['size']
        name = f.attrib['name']
        text = "".join(c.attrib['c'] for c in f)

        f.clear()
        f.text = text
        f.attrib['size'] = size
        f.attrib['name'] = name


def transform_blocks(page):
    for b in page:
        blockm.transform(b)

def transform(page):
    concatenate_chars(page)
    transform_blocks(page)
