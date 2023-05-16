import re
letra = "c"
regex = f"([a-{letra}A-C1-5]+$)"
if re.match(regex, "a"):
 print("Ok match")
else:
 print("NO OK match")