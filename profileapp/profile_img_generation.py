import hashlib
import pydenticon
from django.core.files.base import ContentFile

def profile_img_generator(username,user_email):
    generator = pydenticon.Generator(
    10,10,
    hashlib.sha256,
    ['#657BA8','#cc4e4e','#cc6e3f','#c29313','#57a630','#29cc57','#8647ad','#bf2ca4','#a10d57','#000000'],
    '#FAF0E6')
    hash_value = f'{username}_{user_email}'
    generate_profile_img = generator.generate(hash_value, 120, 120)
    return ContentFile(generate_profile_img,name=f'{username}_profile_img.png')