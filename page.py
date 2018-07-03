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


def identify_fonts(page):
    fonts = page.findall('.//*font')
    for f in fonts:
        name = f.attrib['name']
        size = f.attrib['size']
        f.attrib = {'type': identify_font(name, size)}

def identify_font(name, size):
    if name == 'CMR10':
        return 'regular'
    elif name == 'CMTI10':
        return 'italic'
    elif name == 'CMTI8':
        return 'reference'
    elif name == 'CMR8':
        return 'small'
    elif name == 'CMR7':
        return 'x-small'
    else:
        return name + "-" + str(size)
        
def transform(page):
    concatenate_chars(page)
    transform_blocks(page)
    identify_fonts(page)
