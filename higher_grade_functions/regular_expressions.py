import re
# regular expressions bi metinin bi formata uyup uymadığını yada pdf lerde bi şey aratmak için kullandığımız şey arama kontrol 
""" findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string """

# \d sayı içeriyırsa \D içermiyorsa 
# \s boşluk içeriyırsa \S boşluk içermiyorsa
# \w eger a-z A-Z rakamlar ve alt çizgi varsa
# \A aranan kelşme yazının başındaysa
# \Z aranan kelime sondaysa 

text = "BTK akademi python dersleri BTK"
pattern = "BTK"
match = re.search(pattern,text) #  nerde arıyorsun , neyi arıyorsun 
sonuc = match
# metin içindeki konumu döner
# re.search yerine re.findall() kullanırsan bitane yerine hepsinin kelime olarak liste olarak döner index vermiyor bu
""" all_match = re.findall(pattern,text) """


text = "abc 123 ABC 456 XYZ 789 ASDF A32456 fewısovbngr #$@}][]$z 1B2B 34RT98"
pattern = r"\d\d\d"
pattern = r"\w\w\w"
pattern = r"\d+" # bir ve birden çok basamaklı sayılar 
pattern = r"\d{3,8}" # minimum 3  maimum 8 basamaklı sayılar 
pattern = r"\d{3,}" # minimum 3  maimum sonsuz basamaklı sayılar 
pattern = r"\d{,4}" # minimum 0  maixmum 4 basamaklı sayılar min 0 olduğu için boşluklarda geliyor
pattern = r"\d.\d" # iki rakam arasındaki önemli değil demek
pattern = r"[a-zA-Z0-9]"
pattern = r"\d|[a-z]" #bi rakam yada a-z arası bişeyler boşluk bırakma bunlarda srun oluyor 
pattern = r"^A\d+" # ^ karakteri stringin başını temsil eder 
pattern = r"^#.*z$" # $ karakteri stringin sonunu temsil eder
match = re.findall(pattern,text)
for character in match:
    print(character)

