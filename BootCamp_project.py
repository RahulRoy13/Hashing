import hashlib
def salt(passalt):
    passalt = "@".join(reversed(passalt))
    passalt = "@h@3@j@8@h@g@V@N@m@" + passalt + "@6@f@t@H@6@b@f@0@S@"
    return passalt

passcod1 = input("enter the password= ")
hashcod = salt(passcod1)
x = 0
while x < 10000:
    hashcod1 = hashlib.md5(str.encode(hashcod)).hexdigest()
    hashcod2 = hashlib.sha256(str.encode(hashcod1)).hexdigest()
    hashcod = hashlib.sha512(str.encode(hashcod2)).hexdigest()
    x += 1

print(hashcod)