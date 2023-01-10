# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:10:33 2023

@author: 20pw39
"""

boatSide='Right'
mRight=3
cRight=3
mLeft=0
cLeft=0
i=0
while (i==0):
    if boatSide=="Right":
        print("Boat is on the right")
        m=int(input('Enter number of missionaries on boat '))
        c=int(input('Enter number of cannibals on boat '))
        if m+c<0 or m+c>2:
            print("Invalid move")
            continue
        if m>mRight or c>cRight:
            print("Invalid move")
            continue
        mRight=mRight-m
        cRight=cRight-c
        mLeft=mLeft+m
        cLeft=cLeft+c
        
        print('\U0001f482'*mLeft + '\U0001f479'*cLeft + " | " + '\U0001f30a'*2 + '\U0001f6A2' + '\U0001f30a'*2 + " | " + '\U0001f482'*mRight + '\U0001f479'*cRight)
        
        boatSide= "Left"
        if mRight>0 and mRight<cRight :
                print("YOU LOSE")
                break
        elif mLeft>0 and mLeft<cLeft :
            print("YOU LOSE") 
            break

        if mLeft==3 and cLeft==3 :
            print("YOU WIN")
            break
        
        if boatSide=="Left" :
        
            print("boat is on left side")
            m=int(input('Enter number of missionaries on boat '))
            c=int(input('Enter number of cannibals on boat '))

  
            if m+c<0 or m+c>2 :
                print("invalid move")
                continue
            if m>mLeft or c>cLeft:
                print("invalid move")
                continue
            
            mRight=mRight+m
            cRight+=c
            mLeft-=m
            cLeft-=c
            
            print('\U0001f482'*mLeft + '\U0001f479'*cLeft + " | " + '\U0001f30a'*2 + '\U0001f6A2' + '\U0001f30a'*2 + " | " + '\U0001f482'*mRight + '\U0001f479'*cRight)
        
        if mRight>0 and mRight<cRight:
            print("You lose")
            break
        elif mLeft>0 and mLeft<cLeft:
            print("You lose")
            break
        if mLeft==3 and cLeft==3:
            print("You win")
            break
    
            

   
 
