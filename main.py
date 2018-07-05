import sys
import subprocess
import tempfile
import xml.etree.ElementTree as ET

import document as doc

def print_usage():
    print("Usage: epubify [input.pdf]")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    filename = sys.argv[1]
    document = parse(filename)
    document2 = doc.transform(document)
    # print("-------------------START---------------")
    ET.ElementTree(document2).write('index.html',
                                    'utf-8',
                                    False,
                                    None,
                                    'html')
    # ET.dump(document2)


def parse(filename):
    args = ["mutool", "draw", "-X", "-Fstext", filename]
    with tempfile.TemporaryFile() as tmp:
        subprocess.call(args, stdout=tmp)
        tmp.seek(0, 0)
        tree = ET.parse(tmp)
        return tree.getroot()


if __name__ == "__main__":
    main()
