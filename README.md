to start the attack you need too:
1. first go to the target and go to inspect
2. you put random data on the login page, then press f12 go to the network tab, then you make the request and go to the file that has the post method and scroll down untill you see the form data (if the target has an id, token, rechaptcha token or anything else the attack will not work)
3. you paste what it is in the form data, then go into the program and paste the form data in to the variable named data like this: data = {'rcr_authenticate': '1', 'rcr_user': 'dfssf', 'rcr_pass': 'sdfsfs', 'rcr_submit': 'Conectare'} (this is an example)
4. You run the app, you put the url you saw on the network which will be the target url, you put how many threads you want for the attack and start it:)
