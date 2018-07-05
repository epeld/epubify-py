# Epubify All the Things!
Well, not really.

This tool translates PDFs to HTML.

It
- removes annoying footers and headers
- identifies different font sizes (so that they can later be styled with CSS)
- merges lines into paragraphs and (merges paragraphs across pages)

## Running it
Try

        python main.py

to see some usage.

Typically you want to run

          python main.py mypdf.pdf 1-10

to convert pages 1-10 of the file *mypdf.pdf* into *index.html*.

## Configuration
This is still WIP. For now, you will have to edit the source code!

## How It Works
It wraps the *mupdf* tools and parses the XML output, translating it to look more like proper HTML.

## Requirements
Just python3 really. Oh, and the *mupdf* suite.