#! python3
# mcb.pw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcd.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard. 
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

