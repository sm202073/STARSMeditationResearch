import os
from striprtf.striprtf import rtf_to_text

file_names = os.listdir("/Users/anushree/Desktop/STARSMeditationResearch/AnxietyMeditations")
file_name_and_text = {}
file_data = ""

for file in file_names:
    if (file == ".ipynb_checkpoints"):
        continue
    try:
        f = open('/Users/anushree/Desktop/STARSMeditationResearch/AnxietyMeditations/' + file, 'r',
                encoding='unicode_escape')
        
        Lines = f.readlines()
        str = ""
        
        for line in Lines:
            if line.endswith('\n'):
                substr = line[0:line.length()-2]
            str = substr + line
        
        file_data += "0 " + str + '\n'
    except Exception as e:
        continue

f = open("format_Anxiety.txt", "a")
f.write(file_data)
f.close()


file_data = ""
file_names = os.listdir("/Users/anushree/Desktop/STARSMeditationResearch/SleepMeditations")
# file_name_and_text = {}

for file in file_names:
    if (file == ".ipynb_checkpoints"):
        continue
    try:
        with open('/Users/anushree/Desktop/STARSMeditationResearch/SleepMeditations/' + file, 'r',
                encoding='unicode_escape') as infile:
            content = infile.read()
            text = rtf_to_text(content)
        file_data += "1 " + text + '\n'
    except Exception as e:
        # print(e.errno, e.strerror)
        continue

f = open("format_Sleep.txt", "a")
f.write(file_data)
f.close()


f1 = open("format_Anxiety.txt", 'a+')
f2 = open("format_Sleep.txt", 'r')

f1.write(f2.read())