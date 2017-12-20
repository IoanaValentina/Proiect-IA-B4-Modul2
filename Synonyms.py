import json
import random
with open(r'C:\Users\uidn7090\Desktop\medicina\fisier1_subiecte.txt',  'r' , encoding = "utf-8-sig") as data_file:
    json_data_subiecte = data_file.read()
with open(r'C:\Users\uidn7090\Desktop\medicina\fisier2_proprietati.txt', 'r' , encoding = "utf-8-sig") as data_file:
    json_data_proprietati = data_file.read()
subjects = json.loads(json_data_subiecte)
properties = json.loads(json_data_proprietati)
question_id = 0
answer_id = 0
question_id_file = open(r'C:\Users\uidn7090\Desktop\medicina\questions_vm.txt','w', encoding = "utf8")
answer_id_file =  open(r'C:\Users\uidn7090\Desktop\medicina\answers_vm.txt','w', encoding = "utf8")
for inst in subjects:
    if len(inst["sinonime"])>0:
            question_id = question_id + 1
            question = [question_id,inst["domeniu"],"0","Care dintre urmatoarele variante poate fi sinonim pentru termenul: " + inst["nume"],"0"]
            question_domeniu=inst["domeniu"]
            question_id_file.write(str(question))
            question_id_file.write("\n")
            bool = True
            nr_raspunsuri_corecte = 0
            nr_raspunsuri_totale = 0
            if nr_raspunsuri_corecte < 1:
               bool = True
               nr_raspunsuri_corecte = nr_raspunsuri_corecte + 1
               nr_raspunsuri_totale = nr_raspunsuri_totale + 1
               answer_id = answer_id + 1
               answer = [answer_id, question_id,inst["sinonime"],bool ]
               answer_id_file.write(str(answer))
               answer_id_file.write("\n")
            while (nr_raspunsuri_totale <= 3):
                bool = False
                x = [i for i in subjects if i["sinonime"] != inst["sinonime"] and len(i["sinonime"])>0 and inst["domeniu"]==i["domeniu"]]
                random.shuffle(x)
                if x!=None :
                    x= x[0]
                    nr_raspunsuri_totale = nr_raspunsuri_totale + 1
                    answer_id = answer_id + 1
                    answer = [answer_id,question_id,x["sinonime"],bool]
                    answer_id_file.write(str(answer))
                    answer_id_file.write("\n")

for inst in subjects:
    if len(inst["sinonime"])>0:
            question_id = question_id + 1
            question = [question_id,inst["domeniu"],"1","Care dintre urmatoarele variante poate fi sinonim pentru termenul: " + inst["nume"],"0"]
            question_domeniu=inst["domeniu"]
            question_id_file.write(str(question))
            question_id_file.write("\n")
            bool = True
            nr_raspunsuri_corecte = 0
            nr_raspunsuri_totale = 0
            if nr_raspunsuri_corecte < 1:
               bool = True
               nr_raspunsuri_corecte = nr_raspunsuri_corecte + 1
               nr_raspunsuri_totale = nr_raspunsuri_totale + 1
               answer_id = answer_id + 1
               answer = [answer_id, question_id,inst["sinonime"],bool ]
               answer_id_file.write(str(answer))
               answer_id_file.write("\n")
            while (nr_raspunsuri_totale <= 3):
                bool = False
                x = [i for i in subjects if i["sinonime"] != inst["sinonime"] and len(i["sinonime"])>0 ]
                random.shuffle(x)
                if x!=None :
                    x= x[0]
                    nr_raspunsuri_totale = nr_raspunsuri_totale + 1
                    answer_id = answer_id + 1
                    answer = [answer_id,question_id,x["sinonime"],bool]
                    answer_id_file.write(str(answer))
                    answer_id_file.write("\n")

question_id_file.close()
answer_id_file.close()

















