import os
import queue
import re
import requests
import threading

def check_links(line):
    for link in re.findall(r"https?://[^\s\"><]+", line):
        try:
            if requests.get(link).status_code != 200:
                print("dead link: " + link)
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
    number_of_threads = os.cpu_count()
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
