from stegano import lsb
from PIL import Image
import os

def get_text_size_and_changed_bits(text, container_path):
    text_size_bytes = len(text.encode('utf-8'))

    # Отримання розміру контейнера в байтах
    container_size_bytes = os.path.getsize(container_path)

    # Отримання кількості змінених бітів
    secret = lsb.hide(container_path, text)
    secret_size_bits = secret.size[0] * secret.size[1] * 3 * 8

    return text_size_bytes, container_size_bytes, secret_size_bits

# Перетворення картинки
secret_text = ("Kostenko Dmytro\n"
               "21.09.2002 Dnipro\n"
               "12345678")
container_image_path = "img/1.png"

text_size, container_size_bytes, secret_size_bits = get_text_size_and_changed_bits(secret_text, container_image_path)

print(f"Розмір тексту у байтах: {text_size} байт")
print(f"Розмір контейнера у байтах: {container_size_bytes} байт")
print(f"Кількість змінених бітів у контейнері: {secret_size_bits} біт")

# Зберігання зображення з прихованим текстом
secret = lsb.hide(container_image_path, secret_text)
secret.save("img/2.png")

# Виведення прихованого тексту
result = lsb.reveal("img/2.png")
print(result)
