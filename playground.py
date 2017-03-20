import time
e = 5
n = 299
d = 53

def encrypt_message(msg):
    ecrypted_msg = "" 
    for i in msg:
        numerize = ord(i)
        encrypt = pow(numerize, e, n) # power of e and mod-ing it to n
        ecrypted_msg += unichr(encrypt)
    return ecrypted_msg

def decrypt_message(msg):
    decrypted_msg = ""
    for i in msg:
        numerize = ord(i)
        decrypt = pow(numerize, d, n)
        decrypted_msg += unichr(decrypt)
    return decrypted_msg


message = "school"


#start = time.time()
final_ecrypted_message = encrypt_message(message)
print final_ecrypted_message
print decrypt_message(final_ecrypted_message)
#end = time.time()
#print(end-start)