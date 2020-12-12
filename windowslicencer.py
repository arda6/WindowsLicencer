import os
import webbrowser
print("""


coded by Arda 6
Windows Licecer

""")
webbrowser.open("https://www.github.com/arda6/")
surum = str(input("Which Windows Editions Home / Professional : "))
if surum == 'home':
	os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q9")
	os.system("slmgr /skms kms8.msguides.com")
	os.system("slmgr /ato")
elif surum == 'professional':
	os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
	os.system("slmgr /skms kms8.msguides.com")
	os.system("slmgr /ato")
else :
	print("Quitting...")