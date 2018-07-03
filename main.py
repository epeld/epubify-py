import subprocess
import tempfile
import xml.etree.ElementTree as ET


def main():
    document = parse("/home/erik/Downloads/halmos.pdf")
    overview(document)


def overview(document):
    for page in document:
        print(page.tag, page.attrib)
        for block in page:
            print("  ", block.tag, block.attrib)
            for line in block:
                print("    ", line.tag, line.attrib)
                for font in line:
                    print("      ", font.tag, font.attrib, "".join([c.attrib['c'] for c in font]))

def parse(filename):
    args = ["mutool", "draw", "-X", "-Fstext", filename]
    with tempfile.TemporaryFile() as tmp:
        subprocess.call(args, stdout=tmp)
        tmp.seek(0, 0)
        tree = ET.parse(tmp)
        return tree.getroot()


if __name__ == "__main__":
    main()
