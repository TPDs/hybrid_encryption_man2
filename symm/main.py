import nacl
import nacl.secret
import nacl.utils
import nacl.pwhash

# åbner ciphertext.bin og laver en read så vi kan gemme binary værdi.
cipher = open("ciphertext.bin", "rb").read()
key = open("key.bin", "rb").read()


def opgave_1():
    # vi opretter en "box" og sætter Key argumentet i Box opjektet og kan efterfølgende anvende dette box objekt til at decrypte eller encrypte
    box = nacl.secret.SecretBox(key=key)
    print(f'\nCiphertext:\n{cipher}\n')
    print(f'Symmetric key:\n{key}\n')
    secret_msg = box.decrypt(ciphertext=cipher)
    print(f'Decoded Ciphertext:\n{secret_msg.decode("utf-8")}\n')
    secret_msg = b"I have a secret"
    with open("secret.bin", "w") as f:
        encrypted = box.encrypt(secret_msg)
        f.write(encrypted.decode())
    print(f'Ciphertext:\n{encrypted}\n')
    secret_msg = box.decrypt(ciphertext=encrypted)
    print(f'Decoded Ciphertext:\n{secret_msg.decode("utf-8")}')


if __name__ == "__main__":
    opgave_1()
