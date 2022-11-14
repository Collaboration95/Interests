import hashlib
string  = 123
string1 = "123"
encoded = string1.encode()
result = hashlib.sha256(encoded)
print("The string sha256ed is {}".format(result.hexdigest()))

# result1  = hashlib.sha256(bytes(string,encoding='utf-8')).hexdigest()
# print(" I hope this works : {}".format(result1))