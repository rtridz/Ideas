import googl,clipboard
client=googl.Googl("MyAPIAccessKey")
result=client.shorten(clipboard.get())
clipboard.set(result['id'])