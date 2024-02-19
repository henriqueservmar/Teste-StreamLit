import hashlib
import pickle

def hash_password(password):
    # Criar um objeto de hash SHA-256
    sha256 = hashlib.sha256()

    # Adicionar a senha ao objeto de hash
    sha256.update(password.encode('utf-8'))

    # Retornar o hash resultante como uma string hexadecimal
    return sha256.hexdigest()

hashed_passwords = {
    "henrique.canhadas": hash_password("senha1"),
    "vitor.lucas": hash_password("senha2")
}

with open("hashed_pwq.txt", "wb") as file:
    pickle.dump(hashed_passwords, file)