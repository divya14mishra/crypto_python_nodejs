from Crypto.Cipher import AES
from base64 import b64decode, b64encode
from decouple import config

def encryptionDecryption(flag, input_cmd):
    try:
        # INITVECTOR = hNhPs2Z5UM2OSEFV
        # SECURITYKEY = 7OCK32X80BheN67EZs03bMLClFSWwjDB
        # ALGORITHM = aes-256-cbc
        
        # #iv= get_random_bytes(16)
        iv = config('INITVECTOR').encode("utf8") 
        key = config('SECURITYKEY').encode("utf8")
        # value = "The quick brown fox jumps over the lazy dog"
        strValue= str.encode(input_cmd)
        data = strValue
        cipher = AES.new(key, AES.MODE_CBC, iv)

        if flag==0:
            # #Encryption
            data = b64encode(data)
            pad =data + b"\0" * (AES.block_size - len(data) % AES.block_size)
            ciphertext= cipher.encrypt(pad)
            print(b64encode(ciphertext).decode("utf-8"))
            return b64encode(ciphertext).decode("utf-8")
        else:
            # Decryption
            data = cipher.decrypt(ciphertext)
            print(b64decode(data))
            return b64decode(data)
    
    except Exception as e:
        print(e)
        return 0

