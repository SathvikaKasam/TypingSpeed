from time import time


#now to calculate the accuracy of input promt
def tperror(prompt):
    global inwords
    
    words = prompt.split()
    errors = 0
    
    for i in range(len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if inwords[i] == words[i]:
                if (inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors +=1
                    
            else:
                errors +=1
    return errors

#now to calculate the speed of typing words per minute
def speed(inprompt, stime ,etime):
    global time
    global inwords
    
    inwords = inprompt.split()
    twords =len(inwords)
    speed = twords /time
    
    return speed

#calculate the total elapsed time

def elapsedtime(stime,etime):
    time = etime - stime
    return time

if __name__ == '__main__':
    prompt = "Python is a high-level, general-purpose programming language. "
    print("Type this:- '",prompt,'"')
    
    input("Press Enter when you are ready to check your speed!!!")
    
    
    stime = time()
    inprompt = input()
    etime = time()
    
    time = round(elapsedtime(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)
    
    if len(inprompt.split()) != len(prompt.split()):
        print("The number of words in the given prompt are not equal to the number of words the user provided ,Hence the speed cannot be calculated")
    else:
    
        print("Total time elapsed: ",time, "seconds")
        print("Your Average Typing speed was ", speed, "words per minute (w/m)")
        
        print("with the total of ",errors, "errors")
    