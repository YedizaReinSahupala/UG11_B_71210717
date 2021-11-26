#a = kalimat awal
#b = kata untuk disisipkan
#c = index

a= input("Masukan kalimat awal:")
b= input("Masukan kata yang disisipkan:")
c= int(input("Masukan index:"))

def sisip(a,b,c):
    split1= a[:c-1]
    split2= a[c-1:]
    string= split1 + b + split2
    print(string)

sisip(a,b,c)

