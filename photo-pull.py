'''
photo-pull

1) login to fb (create session)
2) ask for url which comes up when you click on the first photo (e.g. https://www.facebook.com/photo.php?fbid=1173782052666925&set=a.1173781982666932.1073741846.100001054253047&type=3&theater)
3) 

note:
- image urls are STATIC (yay)
- <span class="mlm" id="fbPhotoSnowliftPositionAndCount">1&nbsp;of&nbsp;155</span> this span id shows the count

1 => https://www.facebook.com/photo.php?fbid=1173782052666925&set=a.1173781982666932.1073741846.100001054253047&type=3&theater
2 => https://www.facebook.com/photo.php?fbid=1173782056000258&set=a.1173781982666932.1073741846.100001054253047&type=3&theater
'''

from robobrowser import RoboBrowser;
import requests;
import os;

'''
FUNCTIONS
'''
def error(msg="..."):
	print("ERROR: "+msg);

def printHeaders(headers):
	for header in headers.keys():
		print(header+" : "+headers[header]+"\n");

def login(username,password):
	browser = RoboBrowser(history=True);
	browser.open("https://www.facebook.com/login.php?login_attempt=1&lwv=110");
	form = browser.get_form(id="login_form");
	form["email"]=username;
	form["pass"]=password;
	browser.submit_form(form);
	print(browser.url);
	'''
	form_data = dict();
	form_data["lsd"] = "AVonbkpt";
	form_data["email"]=username;
	form_data["pass"]=password;
	form_data["persistent"]="";
	form_data["default_persistent"]="1";
	form_data["timezone"]="-330";
	form_data["lgndim"] = "eyJ3IjoxMzY2LCJoIjo3NjgsImF3IjoxMzY2LCJhaCI6NzQzLCJjIjoyNH0=";
	form_data["lgnrnd"]="030621_hVD6";
	form_data["lgnjs"]="1462097182";
	form_data["locale"]="en_GB";
	form_data["qsstamp"]="W1tbNTcsOTgsMTE0LDEzMywxMzUsMTU2LDE1OSwxNjAsMTg4LDIyMiwyMjQsMjI4LDI0MiwyNjIsMjY4LDI5MCwyOTcsMzAxLDMwNCwzMDksMzMxLDM2NCwzNzYsMzc5LDM4MiwzOTEsMzk5LDQwNCw0MjAsNDMwLDQ2Miw0NzAsNDc3LDQ4OCw0OTIsNTAxLDUwNiw1MDgsNTMwLDUzNyw2NzEsODg0XV0sIkFabHhrREVSLTJuZkdaTHpZa1BXelVkaVVlbFJKTUFzZjcxOU1aNEZDM0RqZ0ZoV2FnOHEzR2VhZGJmMVNJVjlrUDRrRE9ITUZqWW5aUjM4VGZtMWxXVjM1T3hIUUtCaENmNElpaHQ2Y1l5UVdRQi1YX0hETGRFX2d5TTc5aGNBYUZZZnVxVklZd1JhTXhuNTViY2U2SEdIS1VwUDlFTkJEcmwtMkZtRXRYMVNZRFdZbjRya1lPSjhXZEhyVzdTYmkyaXdyNWNtdjNGX1dzVWN4ZVVJck4zQl8xQ2trYjJQY3diRml3ajQ2cS1EMkEiXQ==";
	home = fb.post(url,data=form_data);
	if "login.php?login_attempt" in home.url:
		error("Bad login! URL: "+home.url);
		return(None);
	else:
		print("Login success! URL: "+home.url);
		return(fb);
	'''
	return(None);	


'''
MAIN
'''
if __name__ == "__main__":
	#os.system("clear");
	user_sess = None;
	while user_sess is None:
		username = input("Enter your email id: ");
		password = input("Enter your password: ");
		user_sess = login(username,password);
	print("Click on the first photo of the album, click on the \"next\"/right arrow and copy the url...");
	url = input("URL: ");
	
