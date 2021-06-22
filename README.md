to start the attack you need to:
1. first go to the target and go to inspect
2. you put random data on the login page and you will se on the network tab (at that post request) the url and the form data
3. you go into the program and paste the form data in to the variable data like this:
data = {'rcr_authenticate': '1', 'rcr_user': 'dfssf', 'rcr_pass': 'sdfsfs', 'rcr_submit': 'Conectare'} (this is an example)
4. you run the app, you put the url you saw on the network which will be the target url, you put the threads and the attack will run:)
