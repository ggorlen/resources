'''
keeps my programming resources markdown neat

references:
https://meta.stackexchange.com/questions/189749/
'''

import re
from sys import argv


def md_link(desc, url):
   return '<a href="%s">%s</a>' % (url, desc)
    

input_filename = argv[1] if len(argv) > 1 else "programming-resources.md"
output_filename = argv[2] if len(argv) > 2 else "README.md"

with open(input_filename) as f:
    text = [x.rstrip() for x in f.readlines()]
    
result = []
toc = []

for line in text:
    m = re.compile(r"^## (.+)$").search(line)

    if m:
        link = "#" + m.group(1).lower().replace(" ", "-")
        toc.append("%s. [%s](%s)" % (len(toc), m.group(1), link))
        result.append(line)
    else:
        m = re.compile(r"^( *\+ +)([^:]+): *(https?://[^ ]+)(.*)$").search(line)
        
        if m: 
            result.append(m.group(1) + md_link(m.group(2), m.group(3)))

            if m.group(4):
                result[-1] += " " + m.group(4)
        else:
            m = re.compile(r"^( *\+ +) *(https?://[^ ]+)(.*)$").search(line)
        
            if m:
                result.append(m.group(1) + md_link(m.group(2), m.group(2)))

                if m.group(3):
                    result[-1] += " " + m.group(3)
            else:
                result.append(line)

with open(output_filename, "w") as f:
    f.write("\n".join(result[:4] + toc[1:] + result[4:]))
