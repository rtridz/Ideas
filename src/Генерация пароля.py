import random, string,clipboard
pass = ''
for x in range(random.randrange(8,12)):
     pass += random.choice(string.ascii_letters + string.digits)
clipboard.set(pass)