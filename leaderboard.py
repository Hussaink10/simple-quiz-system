import json
from datetime import datetime
 
def save_result(name,score):
 f=open("data/leaderboard.json","r")
 leaderboard=json.load(f)
 f.close()
 now=datetime.now()
 entry={"name":name,"score":score,"time":str(now)}
 leaderboard=leaderboard+[entry]

 for i in range(len(leaderboard)):
  for j in range(i+1,len(leaderboard)):
   if leaderboard[j]["score"]>leaderboard[i]["score"]:
    temp=leaderboard[i]
    leaderboard[i]=leaderboard[j]
    leaderboard[j]=temp
    
 leaderboard=leaderboard[:10]
 f=open("data/leaderboard.json","w")
 json.dump(leaderboard,f)
 f.close()
 
def view_leaderboard():
 f=open("data/leaderboard.json","r")
 leaderboard=json.load(f)
 f.close()
 print("Leaderboard:")
 print()
 for i in range(len(leaderboard)):
  entry=leaderboard[i]
  print(i+1,entry["name"],"| Score:",entry["score"],"| Time:",entry["time"])
print()
