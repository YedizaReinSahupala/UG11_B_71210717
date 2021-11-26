
def check_data_type(word,type):
    a= "str"
    b= "int"
    if isinstance(word, str) and type.casefold() == a.casefold():
        print("jawaban anda benar\nTrue")
    elif isinstance(word, str) and type.casefold() == b.casefold():
        print("Jawaban  Anda salah, seharusnya adalah: str\nFalse")
    elif isinstance(word, int) and type.casefold() == b.casefold():
        print("Jawaban Anda benar\nTrue")
    elif isinstance(word,  int) and type.casefold() == a.casefold():
        print("Jawaban  Anda salah, seharusnya adalah: int\nFalse")
    else:
        print()
print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))

