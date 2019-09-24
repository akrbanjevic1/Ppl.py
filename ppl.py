import webbrowser
import pycurl
import subprocess

#These lines ask for the user to give a first and last name
first_name = input("What's the first name of the person you're looking for? ")
last_name = input("\nWhat's the last name of the person you're looking for? ")
#These are the URL's that open once the user has given a name
URL1 = 'https://www.whitepages.com/name/'+first_name+'-'+last_name
#URL2 = 'https://nuwber.com/search?SearchForm%5Bname%5D='+first_name+"+"+last_name+'+&SearchForm%5Bcity%5D=chicago&SearchForm%5Bstate%5D=il'
URL3 = 'https://www.facebook.com/search/top/?q='+first_name+" "+last_name
URL4 = 'https://imggra.com/search'+first_name+" "+last_name

if first_name != str:
	input("If address is known OR has been found, please input here: ")
#This is where the DEFAULT browser opens the url PLUS the given name,
#and a query is run for the name simultaneously 
webbrowser.get('windows-default').open(URL1);
webbrowser.open_new_tab(URL2);
webbrowser.open_new_tab(URL3);
webbrowser.open_new_tab(URL4);
