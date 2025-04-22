In mutool convert, how can i pass in raster options
From the docs they just say
uPDF 1.26.0 documentation
Toggle Light / Dark / Auto color theme
Light Logo
MuPDF 1.26.0 documentation
Search
USER GUIDE

Quick Start Guide
Using MuPDF with C
Using MuPDF WASM
The MuPDF Coordinate System
API REFERENCE

MuPDF on the command line
mutool draw
mutool convert
mutool trace
mutool show
mutool extract
mutool clean
mutool merge
mutool poster
mutool create
mutool sign
mutool info
mutool pages
mutool trim
mutool audit
mutool run
C API
MuPDF & Javascript
Language Bindings
OTHER

Progressive Loading
Android Library
Changes
Third Party Libraries Used by MuPDF
Search
Find #mupdf on Discord
Do you have any feedback on this page?
mutool convert
The convert command converts an input file into another format.

mutool convert [options] file [pages]
Note

Command line parameters within square brackets [] are optional.

[options]
Options are as follows:

-p password
Use the specified password if the file is encrypted.

-o output
The output file name. The output format is inferred from the output filename. Embed %d in the name to indicate the page number (for example: “page%d.png”). Printf modifiers are supported, for example “%03d”. If no output is specified, the output will go to stdout.

-F output format (default inferred from output file name)
raster: cbz, png, pnm, pgm, ppm, pam, pbm, pkm.

print-raster: pcl, pclm, ps, pwg.

vector: pdf, svg.

text: html, xhtml, text, stext.

-A bits
Specify how many bits of anti-aliasing to use. The default is 8.

-W width
Page width in points for EPUB layout.

-H height
Page height in points for EPUB layout.

-S size
Font size in points for EPUB layout.

-U filename
User CSS stylesheet for EPUB layout.

-X
Disable document styles for EPUB layout.

-O comma separated list of options for output format.

Raster output options:
rotate=N Rotate rendered pages N degrees counterclockwise.

resolution=N Set both X and Y resolution in pixels per inch.

x-resolution=N X resolution of rendered pages in pixels per inch.

y-resolution=N Y resolution of rendered pages in pixels per inch.

width=N Render pages to fit N pixels wide (ignore resolution option).

height=N Render pages to fit N pixels tall (ignore resolution option).

colorspace=(gray|rgb|cmyk) Render using specified colorspace.

alpha Render pages with alpha channel and transparent background.

graphics=(aaN|cop|app) Set the rasterizer to use for graphics.