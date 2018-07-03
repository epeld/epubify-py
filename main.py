import subprocess
import tempfile
import xml.etree.ElementTree as ET


def main():
    document = parse("/home/erik/Downloads/halmos.pdf")
    for page in document:
        print(page.tag, page.attrib)


def parse(filename):
    args = ["mutool", "draw", "-X", "-Fstext", filename]
    with tempfile.TemporaryFile() as tmp:
        subprocess.call(args, stdout=tmp)
        tmp.seek(0, 0)
        tree = ET.parse(tmp)
        return tree.getroot()


if __name__ == "__main__":
    main()
