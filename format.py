import os

file_names = os.listdir("/Users/anushree/Desktop/STARSMeditationResearch/AnxietyMeditations")
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
                str += substr
            else:
                str += line
        
        file_data += "0 " + str + '\n'
    except Exception as e:
        continue

f = open("format_Anxiety.txt", "a")
f.write(file_data)
f.close()


file_data = ""
file_names = os.listdir("/Users/anushree/Desktop/STARSMeditationResearch/SleepMeditations")

for file in file_names:
    if (file == ".ipynb_checkpoints"):
        continue
    try:
        f = open('/Users/anushree/Desktop/STARSMeditationResearch/SleepMeditations/' + file, 'r',
                encoding='unicode_escape')
        Lines = f.readlines()
        str = ""
        
        for line in Lines:
            if line.endswith('\n'):
                substr = line[0:line.length()-2]
                str += substr
            else:
                str += line
            # str += line
        
        file_data += "1 " + str + '\n'
    except Exception as e:
        continue

f = open("format_Sleep.txt", "a")
f.write(file_data)
f.close()


f1 = open("format_Anxiety.txt", 'a+')
f2 = open("format_Sleep.txt", 'r')

f = open("format_cclda.txt", "a")
f.write(f1.read())
f.write(f2.read())