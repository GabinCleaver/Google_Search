from googlesearch import search

choice = input("Entrez le mot clé que vous souhaitez rechercher: ")
lang = input("Entrez la langue dans laquelle vous souhaitez rechercher: ")
how_many = int(input("Entrez le nombre de résultats voulus: "))

try:
    for url in search(choice,tld='com.pk',lang=lang, stop=how_many):
        print(url)
except:
    print("Erreur")