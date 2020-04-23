'''
keeps my programming resources markdown neat

references:
https://meta.stackexchange.com/questions/189749/
'''

import re
from sys import argv


def fmt_md_link(desc, url):
    return '<a href="%s">%s</a>' % (url, desc)

def add_toc_entry(m, result, line, toc):
    link = "#" + m.group(1).lower().replace(" ", "-")
    toc.append("%s. [%s](%s)" % (len(toc), m.group(1), link))
    result.append(line)

def add_resource(m, result):
    parts = m.groupdict()
    label = re.sub(r":\s*$", "", parts["label"]) if parts["label"] else parts["url"]
    result.append(parts["whitesp"] + fmt_md_link(label, parts["url"]) + parts["tail"])

if __name__ == "__main__":
    input_filename = argv[1] if len(argv) > 1 else "programming-resources.md"
    output_filename = argv[2] if len(argv) > 2 else "README.md"
    result = []
    toc = []
    
    with open(input_filename, "r") as f:
        for line in f:
            line = line.rstrip()
    
            patterns = (
                (r"## (.+)$", lambda m, result: add_toc_entry(m, result, line, toc)),
                (r"(?P<whitesp> *[-+] +)(?P<label>.+: *)?(?P<url>https?://[^ ]+)(?P<tail>.*)$", add_resource),
            )
            
            for pattern, fn in patterns:
                if m := re.match(pattern, line):
                    fn(m, result)
    
            if not any([re.match(pattern[0], line) for pattern in patterns]):
                result.append(line)
    
    with open(output_filename, "w") as f:
        f.write("\n".join(result[:4] + toc[1:] + result[4:]))
