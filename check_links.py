import re
import requests

with open("programming-resources.md") as f:
    for line in f:
        for link in re.findall(r"https?://[^\s]+", line):
            try:
                if requests.get(link).status_code != 200:
                    print("dead link: " + link)
            except requests.exceptions.SSLError:
                print("bad certificate: " + link)
            except requests.exceptions.ConnectionError:
                print("connection error: " + link)
