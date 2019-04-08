def main():
    n = int(input("Digite o valor N: \n"))
    piramide(n)

def piramide(n):
    asterisco = 1    
    underscore = -1   

    for  n in range(n): 
        underscore = underscore+2
        
    underscore = int((underscore)/2) 

    for n in range(n+1):             
        print("_"*underscore+"*"*asterisco+"_"*underscore)
        asterisco = asterisco + 2    
                                     
        underscore = underscore - 1
        
if __name__ == '__main__':
        main()

    
        

