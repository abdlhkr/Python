import re
text = "BTK Akademi ile Python kurs tarihleri 15-May-2025 15/May/2025 15.05.2025. Telefon numaralarımız +90-530-999-9999 +90 530 999 9999. Mail adreslerimiz abc@gmail.com abc@gmail.co.tr"


pattern = r"\d{2}[-./][a-zA-Z]{3}[-./]\d{4}"
pattern = r"\d{2}[-./]\d{2}[-./]\d{4}"
pattern = r"\w+@[a-z]+(\.[a-z]{2,3})+"
pattern = r"\+\d{2}.\d{3}.\d{3}.\d{4}"
matches = re.finditer(pattern,text)
for character in matches:
    print(character)    