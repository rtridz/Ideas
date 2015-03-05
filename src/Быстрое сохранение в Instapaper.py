import webbrowser,clipboard
addnew='x-callback-instapaper://x-callback-url/add?url='+clipboard.get()
webbrowser.open(addnew)