def check_string(x):
    if x.isalpha():
        return True
    else:
        return False








x=["a","b","c",",1","2"]
string=list(filter(check_string,x))
print(string)
