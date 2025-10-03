import json
def load_questions():
    f=open("data/questions.json", "r")
    questions=json.load(f)
    f.close()
    return questions  
