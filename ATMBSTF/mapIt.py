import webbrowser, sys, pyperclip
 
if len(sys.argv) > 1:
    print("Getting address from command line..........")
    address = ' '.join(sys.argv[1:]) #stores a list of the program filename and command line arguments
else:
    address = pyperclip.paste()

webbrowser.open('https://earth.google.com/web/search/' + address)


