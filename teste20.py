from crypto.Cipher import AES
from crypto.Random import get_random_bytes

# Chave precisa ter 16, 24 ou 32 bytes
chave = get_random_bytes(16)

def criptografar(texto):
    cifra = AES.new(chave, AES.MODE_EAX)
    nonce = cifra.nonce
    texto_cifrado, tag = cifra.encrypt_and_digest(texto.encode('utf-8'))
    return nonce, texto_cifrado, tag

def descriptografar(nonce, texto_cifrado, tag):
    cifra = AES.new(chave, AES.MODE_EAX, nonce=nonce)
    texto_plano = cifra.decrypt_and_verify(texto_cifrado, tag)
    return texto_plano.decode('utf-8')

nonce, texto_cifrado, tag = criptografar('Texto a ser criptografado')
print(f'Texto cifrado: {texto_cifrado}')

texto_plano = descriptografar(nonce, texto_cifrado, tag)
print(f'Texto plano: {texto_plano}')