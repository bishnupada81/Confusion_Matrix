TP,FP,FN,TN=input("Enter the value of TP,FP,FN,TN=").split()
tp=int(TP)
fp=int(FP)
fn=int(FN)
tn=int(TN)


def accuracy():
    result=((tp+tn)/(tp+tn+fp+fn))*100
    return result

def Precision():
    result=(tp/(tp+fp))*100
    return result

def Sencitivity():
    result=(tp/(tp+fn))*100
    return result

def secificity():
    result=(tn/(fp+tn))*100
    return result

def F_score():
    result=((2*tp)/((2*tp)+fp+fn))*100
    return result


print("Accuracy=",accuracy(),"%\n")
print("Precision=",Precision(),"%\n")
print("Sencitivity=",Sencitivity(),"%\n")
print("specificity=",secificity(),"%\n")
print("F-score=",F_score(),"%\n")