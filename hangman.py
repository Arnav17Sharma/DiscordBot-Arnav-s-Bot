def check(answer,ans,score,bool,attempts):
    r = []
    if bool==True:
        while ans.lower() in answer.lower():
            a=list(answer.lower())
            a.remove(ans.lower())
        d="".join(a)
        score+=1
    else:
        attempts+=1
    
    