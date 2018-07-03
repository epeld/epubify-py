import subprocess
import tempfile
from xml.dom import minidom

def main():
    parse("/home/erik/Downloads/halmos.pdf")


def parse(filename):
    args = ["mutool", "draw", "-X", "-Fstext", filename]
    with tempfile.TemporaryFile() as tmp:
        subprocess.call(args, stdout=tmp)
        tmp.seek(0, 0)
        xmldoc = minidom.parse(tmp)
        print(xmldoc)


if __name__ == "__main__":
    main()
