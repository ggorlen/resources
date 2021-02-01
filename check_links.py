import os
import re
import requests
from concurrent.futures import ThreadPoolExecutor
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
headers["Upgrade-Insecure-Requests"] = "1"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Language"] = "en-US,en;q=0.5"
headers["Accept-Encoding"] = "gzip, deflate"

def check_links(line):
    for link in re.findall(r"https?://[^\s\"><]+", line):
        try:
            response = requests.get(link, headers=headers)
            response.raise_for_status()
        except requests.exceptions.SSLError:
            print(f"bad certificate: {link}")
        except requests.exceptions.ConnectionError:
            print(f"connection error: {link}")
        except:
            print(f"status {response.status_code}: {link}")

if __name__ == "__main__":
    with open("programming-resources.md", "r") as f:
        with ThreadPoolExecutor(max_workers=16) as pool:
            pool.map(check_links, f.readlines())
