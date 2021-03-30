"""
add a table of contents to markdown

references:
- https://meta.stackexchange.com/questions/189749/

could also use: https://stackoverflow.com/questions/9721944/automatic-toc-in-github-flavoured-markdown
"""

import re
from sys import argv

def add_toc(lines, placeholder="<!-- TOC -->\n"):
    toc = []
    
    for line in lines:
        if m := re.match(r"## (.+)$", line):
            link = "#" + re.sub(r"\W", "", m.group(1).lower())
            toc.append(f"{len(toc) + 1}. [{m.group(1)}]({link})\n")
    
    for i, line in enumerate(lines):
        if line == placeholder:
            lines[i:i+1] = toc

    return lines

if __name__ == "__main__":
    input_filename = argv[1] if len(argv) > 1 else "programming-resources.md"
    output_filename = argv[2] if len(argv) > 2 else "README.md"

    with (open(input_filename, "r") as fi, 
          open(output_filename, "w") as fo):
        fo.writelines(add_toc(fi.readlines()))

