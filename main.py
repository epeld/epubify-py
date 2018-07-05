import sys
import subprocess
import tempfile
import xml.etree.ElementTree as ET

import document as doc

def print_usage():
    print("Usage: epubify [input.pdf] [page(s)]?")
    print("OR")
    print("Usage: epubify xml [input.pdf] [page(s)]?")
    print("Example: epubify my.pdf 3-4")

def xml_mode():
    args = sys.argv[2:]
    if len(args) == 2:
        [filename, pages] = args
    else:
        pages = None
        [filename] = args
    xmlout('output.xml', filename, pages)


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    if sys.argv[1] == "xml":
        xml_mode()
        return
    if len(sys.argv) == 3:
        [_, filename, pages] = sys.argv
    else:
        pages = None
        [_, filename] = sys.argv
    document = parse(filename, pages)
    document2 = doc.transform(document)
    # print("-------------------START---------------")
    ET.ElementTree(document2).write('index.html',
                                    'utf-8',
                                    False,
                                    None,
                                    'html')
    # ET.dump(document2)


def parse(filename, pages):
    args = ["mutool", "draw", "-X", "-Fstext", filename]
    if pages:
        args.append(str(pages))
    with tempfile.TemporaryFile() as tmp:
        subprocess.call(args, stdout=tmp)
        tmp.seek(0, 0)
        tree = ET.parse(tmp)
        return tree.getroot()


def xmlout(output, filename, pages):
    args = ["mutool", "draw", "-X", "-Fstext", filename]
    if pages:
        args.append(str(pages))
    with open(output, "w") as f:
        subprocess.call(args, stdout=f)


if __name__ == "__main__":
    main()
