import os  
  
header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">"
header += "\n<plist version=\"1.0\">"
header += "\n<dict>"
header += "\n<key>Books</key>"
header += "\n<array>\n"

before_loop = "<dict>\n"
before_loop += "<key>Inserted-By-iBooks</key>\n"
before_loop += "<false/>\n"
before_loop += "<key>Name</key>\n"
before_loop += "<string>"

inner_loop = "</string>\n"
inner_loop += "<key>Page Progression Direction</key>\n"
inner_loop += "<string>default</string>\n"
inner_loop += "<key>Path</key>\n<string>"

after_loop = "</string>\n<key>s</key>\n<string>0</string>\n</dict>\n"

footer = "</array>\n"
footer += "</dict>\n</plist>"

bodystr = ""

for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		sttmp = os.path.join(root, name)[2:]
		if not ".pdf" in sttmp:
			continue
		bodystr += before_loop
		bodystr += sttmp[:-4]
		bodystr += inner_loop
		bodystr += sttmp
		bodystr += after_loop

# print bodystr
# os._exit(1)

file = open("Managed.plist", "w")
file.write(header);
file.write(bodystr);
file.write(footer);
file.close();
