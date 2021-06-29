
# pdf file directory here
pdfDir = ":/Users/DELL/Downloads/Compressed/Skill Portal/CVS/"

# text file directory where you want to put
txtDir = "C:/Users/DELL/Downloads/Compressed/Skill Portal/text/"
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

# converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    print(pdfDir)
    if pdfDir == "": pdfDir = os.getcwd() + "\\"  # if no pdfDir passed in
    for pdf in os.listdir(pdfDir):  # iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename)  # get string of text content of pdf
            textFilename = txtDir + pdf.split(".")[0] + ".txt"
            textFile = open(textFilename, "w", encoding="utf-8")  # make text file
            textFile.write(text)  # write text to text file
    return textFile



for txt in os.listdir(txtDir):
    print(txt)
    fileName = open(txtDir + txt, 'r', encoding="utf8")
    lineList = list()
    with fileName as f:
        for line in f:
            lineList.append(line.lower().replace(',', '\n').rstrip('\n'))

    keyword = ["technical skills", "top skills", "skills", "special skills", "education", "academic qualification",
               "academic", "experience", "work experience"]
    keywordSkill = ["technical Skills", "top skills", "skills"]
    keywordEducation = ["education", "academic qualification", "academic"]
    keywordExperience = ["experience", "work experience"]
    ListOfSkill = []
    indexValue = []
    topicName = []
    for i in lineList:
        for m in keyword:
            if i == m:
                topicName.append(i)

                indexValue.append(lineList.index(i))

    merged = dict(zip(topicName, indexValue))  # merged topicName and its Index value

    def next_value(dictionary, current_key):

        # Get the list of keys from the OrderedDict
        keys = list(dictionary.keys())

        # Get an index of the current key and offset it by -1
        index = keys.index(current_key) + 1

        # return the previous key's value
        return dictionary[keys[index]]

    skill = []
    for i in merged:
        try:
            second = next_value(merged, i)
        except IndexError:
            second = None
        read = lineList[merged[i] + 1:second]
        merged[i] = read

    skill = []
    education = []
    experience = []
    for i in merged:
        for j in keywordSkill:
            if i == j:
                skill = (merged[i])
                skillName = i
                break
        for m in keywordEducation:
            if i == m:
                education = merged[i]
                educationName = i
                break
        for n in keywordExperience:
            if i == n:
                experience = merged[i]
                experienceName = i
                break
    ListSkill = []

    for i in skill:
        ListSkill += i.split()
    print(skillName, ':', ListSkill)

    ListEducation = []
    for i in education:
        ListEducation += i.split()
    print(educationName, ':', ListEducation)

    print(experienceName, ':', experience)

    SkillWords = ['cobra','javascript','jscript','julia','matlab','numpy','r','sas','access','excel','outlook','powerpoint','Access','Excel','Outlook','powerpoint','databases','sap','SciPy','matplotlib','sckit-learn','graphlab','image processing','html','css','php','python','c','c++','java']
    FilteredSkill = []
    for i in SkillWords:
        if i in ListSkill:
            FilteredSkill.append(i)

    print("Filtered Skill of Cv:", FilteredSkill)

    EducationWords = ['bachelor\'s', 'bachelor', 'master', 'engineering', 'diploma', 'computer', 'science']
    FilteredEducation = []
    for i in EducationWords:
        if i in ListEducation:
            FilteredEducation.append(i)

    print("Filtered Education of Cv:", FilteredEducation)

    # skill that is in job_description
    job_description_skill = ['css', 'php']
    # eduction that is in job_description
    job_description_education = ['bachelor']
    print('skill from job desciption', job_description_skill)
    print('education from job description', job_description_education)

    SkillCount = 0
    for i in FilteredSkill:
        if i in job_description_skill:
            SkillCount += 1
    print('NO. of Matched Skill', SkillCount)
    EducationCount = 0
    for i in FilteredEducation:
        if i in job_description_education:
            EducationCount += 1
    print('NO. of Matched Education', EducationCount)
    print('\n')
    bestScore=0

if __name__ == '__main__':
    print("file")
    convertMultiple(pdfDir, txtDir);
