# Purpose: Encriptar una contraseña con passlib
# https://www.youtube.com/watch?v=mgDIP46LEUo

from passlib.context import CryptContext

contexto=CryptContext(schemes=["pbkdf2_sha256"],default="pbkdf2_sha256",pbkdf2_sha256__default_rounds=30000)

texto = "CarlosAle98**"

texto_encriptado = contexto.encrypt(texto)
print(texto_encriptado)
print(contexto.verify(texto,texto_encriptado))