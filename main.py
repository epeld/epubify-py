import subprocess
import tempfile
import xml.etree.ElementTree as ET

import document as doc


def main():
    filename = "/home/erik/Downloads/halmos.pdf"
    document = parse(filename)
    document2 = doc.transform(document)
    ET.dump(document2)


def parse(filename):
    args = ["mutool", "draw", "-X", "-Fstext", filename]
    with tempfile.TemporaryFile() as tmp:
        subprocess.call(args, stdout=tmp)
        tmp.seek(0, 0)
        tree = ET.parse(tmp)
        return tree.getroot()


if __name__ == "__main__":
    main()
