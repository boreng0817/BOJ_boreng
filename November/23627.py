"""
Python
23627번 driip
String
"""
string = input().strip()

if len(string) >= 5 and string[-5:] == "driip":
    print("cute")
else:
    print("not cute")
