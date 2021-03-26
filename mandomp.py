
#-*- coding:utf-8 -*-
import os
card_name=["고블린","고블린","해골전사","해골전사","오크","오크","뱀파이어","뱀파이어","골렘","골렘","사신","마왕","드래곤"]
card_attk=[1,1,2,2,3,3,4,4,5,5,6,7,9]
card_week=[["횃불"],["횃불"],["횃불","성수"],["횃불","성수"],["횃불"],["횃불"],["성수"],["성수"],[],[],["성수"],[],["창"]]

if __name__ == "__main__" :
    while(True):
        print("명령어 설명 : ")
        print(" 게임 시작하기 : start")
        print(" 카드 일람 : list")
        t=input()
        if t=="start":
            while(True):        
                print("플레이어 수 입력 :")
                z=int(input())
                #for i in Range(z):

        if t=="list":
            print("이름 , 공격력 , 약점")
            for e, i in enumerate(card_name):
                s=""
                s+=i+", "
                s+=str(card_attk[e])+", "
                for j in card_week[e]:
                    s+=j
                    if e<len(card_week[e])-1:
                        s+="/"
                print(s)
            print("\n")