



import random

ug=1
pcg=1
while True:

    u=int(input())

    if(u==1):
        
        for i in range(1,4):
            l=['rock','scissor','paper']

            pc=random.choice(l)
            print("computer choice",pc)


            user=input("enter the user rock1 and scissor2 and paper3:")

            

            # if(user=='')


            if(user==pc):
                print("draw ,both 1 point")
                print("********************************")

                ug=+1
                pcg=+1
            elif(user=='rock'):
                print("user wins",ug)
                print("********************************")
                ug=+1
                if(pc=='rock'):
                    print("pc wins",pcg)
                    print("********************************")

                    pcg=+1
            elif(user=='scissor'):
                print("user wins",ug)
                print("********************************")

                ug=+1
                if(pc=='scissor'):
                    print("pc wins",pcg)
                    print("********************************")
                    pcg=+1
            elif(user=='paper'):
                print("user wins",ug)
                print("********************************")

                ug=+1
                if(pc=='paper'):
                    print("pc wins",pcg)
                    print("********************************")

                    pcg=+1
            
        if(ug==pcg):
            print("pc and user draw",ug,pcg)
            print(" game over")
            break

        elif(ug<pcg):
            print("pcg wins",pcg)
            print(" game over")
            break
        elif(ug>pcg):
            print("ug wins",ug)  
            print(" game over")
            break
        else:
            print(" game over")
            break


        


                       
        

    
    
    else:
        print("exit game")
        break