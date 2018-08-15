import lxml.html

dataToWrite = ""
listOfUrls = ["http://www.kyokushinkaikan.org/en/branch/asia.html",
              "http://www.kyokushinkaikan.org/en/branch/southpacific.html",
              "http://www.kyokushinkaikan.org/en/branch/russia.html",
              "http://www.kyokushinkaikan.org/en/branch/middleeast.html",
              "http://www.kyokushinkaikan.org/en/branch/europe.html",
              "http://www.kyokushinkaikan.org/en/branch/africa.html",
              "http://www.kyokushinkaikan.org/en/branch/northamerica.html",
              "http://www.kyokushinkaikan.org/en/branch/southamerica.html"]


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
