import json

ADMIN_PASSWORD="bic1114"
QUESTIONS_FILE="data/questions.json"

def save(questions):
 with open(QUESTIONS_FILE,"w")as f:json.dump(questions,f)
 
def load():
 with open(QUESTIONS_FILE,"r")as f:return json.load(f)
 
def add_question(questions):
 q=input("Question: ")
 opts=[]
 
 print("Enter the options:")
 opts.append(input("A: "))
 opts.append(input("B: "))
 opts.append(input("C: "))
 opts.append(input("D: "))
 ans=input("the Correct answer (A/B/C/D): ").upper()
 
 if ans not in["A","B","C","D"]:
  print("Invalid.");return
 questions.append({"question":q,"options":opts,"correct_answer":ans})
 save(questions)
 print("Added.")
 
def search_edit_delete(questions):
 k=input("enter the Keyword: ").lower()
 found=False
 for i in range(len(questions)):
  q=questions[i]
  if k in q["question"].lower():
   print(q["question"])
   print("A:",q["options"][0])
   print("B:",q["options"][1])
   print("C:",q["options"][2])
   print("D:",q["options"][3])
   print("Correct:",q["correct_answer"])
   act=input("[E] to edit, [D]to delete, [Enter] to Cancel: ").upper()
   
   if act=="E":
    new_q=input("New Question (leave to skip): ")
    
    if new_q:q["question"]=new_q
    
    for n in range(4):
     v=input(f"New {['option A','option B','option C','option D'][n]} (leave to skip): ")
     if v:q["options"][n]=v
     
    a=input("New Answer (A/B/C/D, leave to skip): ").upper()
    if a in["A","B","C","D"]:q["correct_answer"]=a
    print("Updated.")
    
   elif act=="D":
    if input("Confirm delete (Y): ").upper()=="Y":
     questions.pop(i)
     print("Deleted.")
     
   save(questions)
   found=True
   break

 if not found:print("Not found.")
 
def admin_menu():
 if input("Admin password: ")!=ADMIN_PASSWORD:
  print("Wrong password.");return
 questions=load()
 while True:
  print("\n1) Add\n2) Search/Edit/Delete\n3) Exit")
  c=input("Choice: ")
  if c=="1":add_question(questions)
  elif c=="2":search_edit_delete(questions)
  elif c=="3":break
  else:print("Wrong input.")
