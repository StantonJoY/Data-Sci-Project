import spacy
import pdfplumber
if __name__=='__main__':
    nlp=spacy.load("en_core_web_lg")
    filename1="C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\odoo\\odoo words.txt"
    pdf="C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\GDPR\\GDPR.pdf"
    pdfwords="C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\GDPR\\GDPR.txt"
    results="C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\GDPR\\results of GDPR.txt"#results
    # with open(pdfwords, mode='a+', encoding='utf-8') as pdfwords:#pdf2txt
    #     pdfwords.truncate(0)
    #     with pdfplumber.open(pdf) as pdf:
    #         for page in pdf.pages:
    #             text = page.extract_text()  # extract text
    #             pdfwords.write(text)
    with open(filename1,'r',encoding='utf-8') as oddoWords:
        oddowords=oddoWords.readlines()
        with open(pdfwords,mode='r',encoding='utf-8') as pdfwords:
            with open(results,mode='a+',encoding='utf-8')as results:
                results.truncate(0)
                for words0 in oddowords:
                    for words1 in pdfwords:
                        if(nlp(words0).similarity(nlp(words1))>=0.5):
                            results.write(words1)
    print("finished!")




