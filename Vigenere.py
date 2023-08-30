def Vigenere_Sifrele(key, text, bool):

    alfabe = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l",
              "m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
    lowerText = text.lower()
    anahtarNums = []
    textNums = []
    newTextNums = []
    newText = ""


    #Anahtarın sayısal değerini, metinin sayısal değerine
    # eklemek için çıkaracağız.
    for key_harf in key:
        if key_harf in alfabe:
            for harf in range(0, len(alfabe)):
                if key_harf == alfabe[harf]:
                    anahtarNums.append(harf)
        else:
            anahtarNums = anahtarNums
            print("Anahtarda harf dışında bir şey olamaz '" + key_harf +
                  "' tolare edilmeyecektir")

    for sifre_harf in lowerText:
        if sifre_harf in alfabe:
            for harf in range(0, len(alfabe)):
                if sifre_harf == alfabe[harf]:
                    textNums.append(harf)
        else:
            textNums.append(sifre_harf + ".")

    #Anahtarın değeri ile metininkini topluyoruz.
    for i in range(len(textNums)):
        if textNums[i] in range(len(alfabe)):
            newTextNums.append(
                (int(textNums[i]) + (int(bool) *
                    (int(anahtarNums[i % len(anahtarNums)]))))
                        % len(alfabe))
        else:
            newTextNums.append(textNums[i])

    #Yeni metnin sayısal değerini harflere çeviriyoruz.
    for i in range(len(newTextNums)):
        if newTextNums[i] in range(len(alfabe)):
            if text[i] == lowerText[i]:
                newText += alfabe[newTextNums[i]]
            else:
                newText += alfabe[newTextNums[i]].upper()
        else:
            newText += newTextNums[i][0]

    return newText

i = "true"
while i == "true":
    bool = input("Şifrele ya da çöz "
                 "(Şifrelemek için '1' çözmek için '-1' giriniz.):")
    if bool == "1" or bool == "-1":
        text = input("Cümle : ")
        anahtar = input("Anahtar : ")
        i = "false"
        print(Vigenere_Sifrele(anahtar,text,int(bool)))
    else:
        print("Ya bunu da düzgün yap be!")
        i = "true"
input("Programı kapatmak için enter'a basın.")