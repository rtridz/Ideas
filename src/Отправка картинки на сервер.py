import ftplib, clipboard
a=clipboard.get_image()
filename='out.jpg'
a.save(filename)
con=ftplib.FTP('Host','Login','Password')
f=open(filename,'rb')
send=con.storbinary(filename,f)
con.close()