import random, string,pyperclip
def pwgen():
	pas = ''
	for x in range(random.randrange(8,12)):
	     pas += random.choice(string.ascii_letters + string.digits)
	pyperclip.copy(pas)
	pas = pyperclip.paste()
	return (pas)
pwgen()