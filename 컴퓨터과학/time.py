import time
start = time.time()
score = [70,60,50,80,90,40]
maxi = score[0]

for i in score:
    if maxi <i:
        maxi = i;
        
print(f"{max(score)}\nTime1 : {time.time()-start}")
print(maxi)
print("Time2 :",time.time()-start)
