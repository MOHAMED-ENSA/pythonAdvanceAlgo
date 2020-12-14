import time 
import multiprocessing 
import concurrent.futures 
import string 
letters = list(string.ascii_letters)


start = time.perf_counter()

 



def testpincode( match): 
    pincode = ["g","c","r","r","f"]
    if match == pincode : 
        return True 
    else : 
        return False

def process():
    done  = -1
    for x in letters :
        if done == 1 : 
            break 
        for a in letters :
            if done == 1 : 
                break 
            for b in letters: 
                if done == 1 : 
                    break 
                for c in letters:
                    if done == 1 : 
                        break 
                    for d in letters:
                        match = [x,a,b,c,d]
                        if testpincode(match) == True : 
                            print (f"Done ... the pin code is {match}")
                            done = 1 
                            break 
# process()
# end = time.perf_counter()
# print(f"done in {round(end - start , 2 )} seconds")


# if __name__ == "__main__" :
#     p1 = multiprocessing.Process(target = process)       
#     p1.start()  
#     p1.join()
#     end = time.perf_counter()
#     print(f"done in {round(end - start , 2 )} seconds")
# if __name__ == "__main__" : 
    
#     with concurrent.futures.ProcessPoolExecutor() as executer :
#         #x = list(range(10))
#         results = executer.map(process , letters)
#         for result in results : 
#             print(result)
#     end = time.perf_counter()
    
#     print(f"done in {round(end - start , 2 )} seconds")



#x = list(range(10))
# results = map(process , letters)
# for result in results : 
#     print(result)
# end = time.perf_counter()
# print(f"done in {round(end - start , 2 )} seconds")

# for i in x :
#     print(process(i))

# def calcul(a): 
#     for i in range(100000000): 
#         a = a + 1 
#     return a  
# if __name__ == "__main__" : 
#     with concurrent.futures.ProcessPoolExecutor() as Excecuter : 
#         results = Excecuter.map(calcul, [1,5,4,88])
#         for result in results : 
#             print(result)
#     end = time.perf_counter()

#     print(f"done in {round(end - start , 2 )} seconds")

# results = map(calcul, [1,5,4,88])
# for result in results : 
#     print(result)
# end = time.perf_counter()

# print(f"done in {round(end - start , 2 )} seconds")




