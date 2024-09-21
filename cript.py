import os
from rich import print
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def Encryption(OrigFile):
    # Открытие изображения в бинарном режиме
    with open(OrigFile, "rb") as img_file:
        binary_data = img_file.read()

    # Преобразование байтов в двоичный код
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)

    # Запись бинарного представления в новый файл
    with open("binary_output.txt", "w") as output_file:
        output_file.write(binary_string)

    # Генерация случайного ключа и IV для AES
    key = os.urandom(32)  # 256-битный ключ
    iv = os.urandom(16)   # 128-битный IV

    # Извлечение расширения файла
    file_extension = os.path.splitext(OrigFile)[1].encode()

    # Сохранение ключа и расширения в файл
    with open("key.bin", "wb") as key_file:
        # Запись расширения файла
        key_file.write(file_extension + b'\n')
        # Запись ключа
        key_file.write(key)

    # Создание объекта шифрования
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Паддинг для данных
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    # Чтение данных из файла для шифрования
    with open("binary_output.txt", "rb") as f:
        data = f.read()

    # Добавление паддинга и шифрование
    padded_data = padder.update(data) + padder.finalize()
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Сохранение зашифрованных данных в новый файл
    with open("encrypted.txt", "wb") as f:
        f.write(iv + encrypted_data)

    print("[bold green]Encryption successful! Encrypted data saved to[/bold green] [italic yellow]encrypted.txt[/italic yellow]")

    # Удаление файла binary_output.txt
    os.remove("binary_output.txt")
