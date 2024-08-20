# Imports BeautifulSoup and regular expressions for use below
from bs4 import BeautifulSoup as bs
import re

# Creates tei_header and tei_body variables for writing into the TEI file below,
# with title, author, and release year strings added into the header
tei_header = f"""<teiHeader>
  <fileDesc>
    <titleStmt>
      <title>title</title>
      <author>author</author>
    </titleStmt>
    <publicationStmt>
      <publisher>publisher</publisher>
      <date>date</date>
    </publicationStmt> 
  </fileDesc>
</teiHeader>"""

# These titles are samples from the corpus
txt_files = ["Tricks.txt", "This_book_is_gay.txt", "The_perks_of_being_a_wallflower.txt", 
             "The_color_purple.txt", "The_chocolate_war.txt", 
             "The_absolutely_true_diary_of_a_part_time_indian.txt", "The_57_bus.txt", 
             "Queer_ultimate_guide.txt", "Out_of_darkness.txt", "More_happy_than_not.txt", 
             "Me_and_Earl_and_the_dying_girl.txt", "Looking_for_Alaska.txt", "It.txt", 
             "I_am_not_your_perfect_Mexican_daughter.txt", "Go_ask_Alice.txt", "Forever.txt", 
             "Catcher_in_the_rye.txt", "Beyond_magenta.txt", "Beloved.txt", 
             "Being_Jazz_my_life_as_a_(transgender)_teen.txt", 
             "Aristotle_and_Dante_discover_the_secrets.txt", "A_court_of_mist_and_fury.txt"]

for text in txt_files:
  print(f"Processing {text}...")
  tei_body = "<text>"
  with open(f"TXT_files/{text}", encoding="utf8") as input_file:
    # Creates state variables to keep track of div structures for the TEI file
    in_body = False
    in_paragraph = False
    tei_body += f"<body>"

    # Iterating through the text file
    for line in input_file:
      # Detects paragraphs in the text and inserts paragraphs tags in the text
      if re.search(r"\w", line):
        if in_paragraph is False:
          line = f"<p>\n{line}"
          in_paragraph = True
          tei_body += line
      elif not re.search(r"\w", line) and in_paragraph is True:
        tei_body += "</p>\n"
        in_paragraph = False

  # Converts the accumulated TEI components to BeautifulSoup object and writes the 
  # prettified version of the object to a TEI file
  tei = f"<?xml version = '1.0' encoding='utf8'?><TEI>{tei_header}{tei_body}</body></text></TEI>"
  soup = bs(tei, "xml")

  with open(f"new_TEI_files/{text.replace('.txt', '')}.tei", "w", encoding="utf8") as tei_output:
    tei_output.write(tei)