"""
add a table of contents to markdown

references:
- https://meta.stackexchange.com/questions/189749/

could also use: 

- https://about.gitlab.com/handbook/markdown-guide/#table-of-contents-toc
- https://stackoverflow.com/questions/9721944/automatic-toc-in-github-flavoured-markdown
"""

import re
from collections import defaultdict
from sys import argv

def add_toc(lines, placeholder="<!-- TOC -->\n"):
    seen = defaultdict(int)
    toc = []
    
    for line in lines:
        if m := re.match(r"## (.+)$", line):
            link = m.group(1).lower()
            link = "#" + re.sub(r"[^A-Za-z\d_-]", "", re.sub(r"\s+", "-", link))
            seen[link] += 1
            
            if seen[link] > 1:
                link = link + f"-{seen[link] - 1}"

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

