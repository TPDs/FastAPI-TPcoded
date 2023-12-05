import fitz
import pandas as pd
import re


def get_pdf_data(file_path):
    docs = fitz.open(file_path)  # type: ignore
    with docs as doc:  # type: ignore
        textlist = chr(12).join([page.get_text() for page in doc])
    textlist = textlist.split(sep='\x0c')
    textlist = [t.split('\n') for t in textlist]    
    print(textlist[0:5])
    removelist = ['SE MERE PÅ SIDE', 'GÆLDER FRA LØRDAG DEN',
                  'Spotvarer fås kun så længe lager haves. Nogle butikker fører ikke spotvarer og nonfoodvarer', '-FÅ DE 100 DAGLIGVARER,DU KØBER MEST AF',
                  '10. NOVEMBERUGENS', 'Rema1000', '*Prissammenligningen er foretaget',  "FÅ DE 100 DAGLIGVARER,",
                  "DU KØBER MEST AF, BILLIGST HOS OS",
                  "Hvis en konkurrent sænker normalprisen*",
                  "NU ER ",
                  "PRISERNE ",
                  "SAT ENDNU ",
                  "MERE NED!",
                  "Prisen på 100 varer er pr.",
                  "sænket yderligere sammenlignet ",
                  "med den trykte avis.",
                  " Spotvarer fås kun så længe lager haves. Nogle butikker fører ikke spotvarer og nonfoodvarer.",
                  "*Prissammenligningen er foretaget på 100 udvalgte dagligvarer. Vi sammenligner priser én gang om ugen, hver tirsdag, med Rema1000, Lidl, SuperBrugsen ",
                  "og Coop365s normalpriser og sænker priserne hurtigst muligt og senest inden for 4 dage. Der sammenlignes med normalpriser på identiske eller sammenlignelige varer, ",
                  "der opfylder samme behov hos kunderne ud fra bl.a. sammensætning, kvalitet, mængde og indhold hos konkurrenterne. Der sammenlignes ikke med konkurrenternes ",
                  "avispriser, andre kampagne-, lokal-, merkøbs- eller medlemspriser. Læs mere om indløsning på netto.dk/priskrig, hvis du imod forventning finder en ",
                  "vare billigere ved en konkurrent. Kig efter Priskrig-skiltet på hylderne i Netto. Ikke alle varer føres i alle butikker.",]
    textlist = [[t for t in lst if not any(r in t for r in removelist)] for lst in textlist]
    page1 = ''
    for x in textlist[0:5]:
        for y in x:
            page1 += y + ''
    page1 = re.split(r"\.(?=-)", page1)
    page1 = [x.strip() for x in page1 if len(x.strip()) >= 4]  # remove items with less than 3 characters
    return [f"{i}{s[1:]}" if s.startswith("-") else s for i, s in enumerate(page1)]
    
   

