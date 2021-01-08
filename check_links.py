import os
import queue
import re
import requests
import threading
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

            if not response.ok:
                print(f"status {response.status_code}: {link}")
        except requests.exceptions.SSLError:
            print("bad certificate: " + link)
        except requests.exceptions.ConnectionError:
            print("connection error: " + link)

def do_thread_work(task_queue):
    while True:
        task = task_queue.get()

        if task is None:
            break

        check_links(*task)
        task_queue.task_done()

def main():
    number_of_threads = max(os.cpu_count(), 8)
    task_queue = queue.Queue()
    
    with open("programming-resources.md", "r") as f:
        for line in f:
            task_queue.put((line,)) 
        
        threads = [threading.Thread(target=do_thread_work, args=(task_queue,)) 
                   for i in range(number_of_threads)]
        
        for t in threads:
            t.start()
        
        task_queue.join()
    
        for i in range(number_of_threads):
            task_queue.put(None)
    
        for t in threads:
            t.join()

if __name__ == "__main__":
    main()

