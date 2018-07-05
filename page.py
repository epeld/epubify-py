import block as blockm
import xml.etree.ElementTree as ET

# Page transformations

def concatenate_chars(page):
    fonts = page.findall('.//font')
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
    elif name == 'CMCSC10':
        return 'h2'
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


def remove_header(page):
    # "First block is typically a header with pagenr"
    if not page:
        return
    el = page[0]
    dump = str(ET.tostring(el))
    if "HOW TO WRITE MATHEMATICS" in dump:
        page.remove(el)
    elif "PAUL R. HALMOS" in dump:
        page.remove(el)



def remove_footer(page):
    if not page:
        return
    el = page[-1]
    font = el.find('.//*/font')
    dump = str(font.text)
    if dump.isnumeric():
        page.remove(el)


def unwind_blocks(page):
    if page:
        first = page[0]
        if first:
            first[0].attrib['first'] = 'true'
        last = page[-1]
        if last:
            last[-1].attrib['last'] = 'true'
    blocks = page.findall('block')
    for b in blocks:
        page.remove(b)
        for c in b:
            page.append(c)

def transform(page):
    concatenate_chars(page)
    transform_blocks(page)
    identify_fonts(page)
    remove_header(page)
    remove_footer(page)
    unwind_blocks(page)
