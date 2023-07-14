from cryptography.fernet import Fernet
import os
import argparse

def generate_key():
    key = Fernet.generate_key()
    with open('master.key', 'wb') as key_file:
        key_file.write(key)

def get_key():
    return open('master.key', 'rb').read()

def decrypt(items, key):
     f = Fernet(key)
     for item in items:
         item_orig = item.rsplit('.', 1)[0]
         print(item)
         os.rename(item, item_orig)
         item = item_orig
         with open(item, 'rb') as  file:
             encrypted_data = file.read()

         decrypted_data = f.decrypt(encrypted_data)

         with open(item, 'wb') as file:
             file.write(decrypted_data)
             
def encript(items, key, ex):
    f = Fernet(key)

    for item in items:
        with open(items, 'rb') as files:
            file_data = files.read()
    
    encrypted_data = f.encrypt(file_data)

    with open(item, 'wb') as file:
        file.write(encrypted_data)
    
    os.rename(items, ex)

    if FileExistsError:
        os.system("clear")
        os.system("cls")

parser = argparse.ArgumentParser(
    "Encrypt and decryt files", usage="python enc.py <File> <Mode> <-e (Extension) (optional)>"
)

parser.add_argument(
    "File", help="The file will be decrypt or encrypt"
)

parser.add_argument(
    "Mode", help="You will decrypt or encrypt?"
)

parser.add_argument(
    "-e","--Extension", help="The text after the .", required=False, default=".encrypted"
)

args = parser.parse_args()
extension = args.Extension
print(args.File)
print(args.Mode)
print(args.Extension)

if args.Mode == "encrypt":
      generate_key()
      k = get_key()
      encript(args.File, k, extension)

if args.Mode=="decrypt":
    k = get_key()
    decrypt(args.File, k)
