from rich import print
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def Decryption(CryptFile, Keyfile):
    # Чтение ключа и расширения из файла
    with open(Keyfile, "rb") as key_file:
        # Чтение расширения
        file_extension = key_file.readline().strip().decode()
        # Чтение ключа
        key = key_file.read()

    # Чтение зашифрованного файла
    with open(CryptFile, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Извлечение IV (первые 16 байт) и зашифрованных данных
    iv = encrypted_data[:16]
    encrypted_content = encrypted_data[16:]

    # Создание объекта шифрования с использованием AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Расшифровка данных
    decrypted_padded_data = decryptor.update(encrypted_content) + decryptor.finalize()

    # Удаление паддинга
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Запись расшифрованных данных в временный бинарный файл
    with open("binary_output_restored.txt", "wb") as restored_file:
        restored_file.write(decrypted_data)

    print("[bold green]File[/bold green] [italic yellow]binary_output_restored.txt[/italic yellow] [bold green]has been successfully restored from the encrypted file.[/bold green]")

    # Восстановление изображения из бинарного файла
    with open("binary_output_restored.txt", "r") as binary_file:
        binary_string = binary_file.read()

    # Преобразование бинарной строки в байты
    byte_data = bytearray(int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8))

    # Запись байтов в файл изображения с оригинальным расширением
    restored_image_filename = f"file{file_extension}"
    with open(restored_image_filename, "wb") as image_file:
        image_file.write(byte_data)

    print(f"[bold magenta]Image file has been successfully restored and saved as[/bold magenta] [italic yellow]{restored_image_filename}.[/italic yellow]")

    # Удаление файла binary_output_restored.txt
    os.remove("binary_output_restored.txt")
