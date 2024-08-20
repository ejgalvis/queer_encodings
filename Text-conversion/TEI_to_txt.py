import os
from bs4 import BeautifulSoup as bs

os.chdir("Corpus Texts")

for file in os.scandir("TEI files"):
    if ".tei" in str(file):
        with open(file, encoding="utf8") as inputfile:
            input = inputfile.read()
        soup = bs(input, "xml")

        raw_text = soup.title.text.strip()
        raw_text += f"\n\n\n{soup.body.text}"

        txt_name = str(file.name).replace("tei", "txt")
        os.chdir("../Corpus Texts/new_txts")
        with open(f"{txt_name}", "w", encoding="utf8") as new_txt:
            new_txt.write(raw_text)
        os.chdir("../")
