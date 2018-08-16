import lxml.html
import pyperclip

dataToWrite = ""
listOfUrls = list()

listOfKeys = ["A", "S", "R", "M", "E", "F", "N", "U"]
countriesDict = {listOfKeys[0]: "asia", listOfKeys[1]: "southpacific", listOfKeys[2]: "russia",
                 listOfKeys[3]: "middleeast", listOfKeys[4]: "europe", listOfKeys[5]: "africa",
                 listOfKeys[6]: "northamerica", listOfKeys[7]: "southamerica"}
inputStr = input("Unesite sifru koja predstavlja spisak regija iz kojih zelite mejlove Branch Chief-ova\n" +
                 "mejlovi ce biti eksportovani u 'emails.txt' fajl i kopirani na clipboard \n\n" +
                 "~~~~~ konstrukcija sifre: jedno slovo- jedna regija, bez razmaka, velicina slova nije bitna," +
                 " otkucate zeljenu sifru i lupite enter ~~~~~ \n\n" +
                 "~~~ A - Azija, S - Juzni Pacifik, R - Rusija, M - Bliski Istok, E - Evropa, F - Afrika, " +
                 "N - Severna Amerika, U - Juzna Amerika ~~~ \n")

for key in list(inputStr):
    if key.upper() in listOfKeys:
        listOfUrls.append("http://www.kyokushinkaikan.org/en/branch/" + countriesDict[key.upper()] + ".html")


for url in listOfUrls:
    textToWrite = ''
    tree = lxml.html.parse(url)
    extractedContent = [td.text_content() for td in tree.xpath('//td')]

    for i in extractedContent:
        divTag = str(i)
        foo = divTag.split("\n")
        for j in foo:
            if "e-mail:" in j:
                bar = j.split(" ")
                for k in bar:
                    if "@" in k:
                        textToWrite += k + ";"
    textToWrite = textToWrite.replace(",", "")
    dataToWrite += textToWrite

f = open("emails.txt", "w")
f.write(dataToWrite)
pyperclip.copy(dataToWrite)
