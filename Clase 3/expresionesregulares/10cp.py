import re
cp = "1444"
test = re.match('^[0-9]{4}$',cp)
if (test):
    print("Ok")
else:
    print("NO Ok")