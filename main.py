# 파일이름 : main.py (2차과제까지)
# 작 성 자 : 60251684 전자공학 이인 

shop_name = ""
bread = ["곰보빵", "사과빵", "마늘빵", "뼈다귀", "생크림빵", "칼빵"]
faction_list = []
species = ["좀비", "마녀", "뱀파이어", "웨어울프", "밴시", "목 없는 기사"]
meet_list = []
reputation = 0.0
repu_list = []


scenario = [
    "이곳에 오신 것을 환영합니다, 낯선 이여...",
    "우선, 이곳에 우연찮게 오셨으리라고 생각합니다. 물론 저도 예상치 못했지만요.",
    "여기는 당신이 알던 곳과는 다른 곳입니다. 당신들의 말로는, 이세계라고 하죠.",
    "당신을 돌려보내려면 저도 꽤 많은 힘을 써야 합니다. 그전까지 기다려주셨으면 해요.",
    "또, 그렇게 하기 위해서는 당신의 업(karma)을 확인해야 합니다. 이 차원의 규칙이거든요.",
    "당신의 업이 위태로울 것 같아 불안하신가요?",
    "걱정하지 마세요. 저희가 준비한 곳에서 '적절히' 응대해주신다면. 업이 깨끗해질 겁니다. ",
    "그럼 무운을 빕니다."
]

for i in scenario:
    print(f"{i:50s}", end="")
    input("")

shop_name = input("\n\n\n빵집 이름을 입력해주세요. 이왕이면 기억에 잘 남는 거로요. ")
print("고마워요. 날\n"+"나를\n"*5+"잊지 말아요.")






import random as r

day = [5, 4, 3, 2, 1]
for i in day :
    weight = 1.0
    print("\n"*5)
    print("-"*50)
    print(f"{i}일 남았습니다. 신중하게 시간을 사용하세요.\n")
    print("1. 손님 받기")
    print("2. ■■ 도감")
    print("3. 당신에게 있는 무언가.")
    print("4. 팩션")
    print("5. 추천하지 않습니다. 선택하지 마세요.")
    print("6. ...오늘은 그만하실 건가요?")
    ch = input("무엇을 하시겠습니까? 번호로 입력하세요. Ex : 1\n")
    chosse = 0
    if ch not in ("1", "2", "3", "4", "5", "6") :
        print("이게 아닐 텐데요. 다시 입력해주세요. ")
        temp = input("...")
        continue
    else :
        choose = int(ch)

    if choose == 1 :
        print("\n")
        print("손님을 받으시는군요. 열심히 하시네요.")
        print("그럼 주사위를 굴려볼까요? 행운을 빕니다.")
        num = r.randint(0,5)
        meet_list.append(num)
        # print(meet_list)
        input(f"{num+1}. 좋은 숫자 같나요?")
        print(f"\n{species[num]}를 모시겠습니다. 기호를 잘 맞춰주세요.")
        temp = input("...대답.")
        print("")

        for i in range(3, 0, -1):
            print("\n\n", bread)
            print(f"이 손님에겐 어떤 빵이 괜찮을까요? 남은 기회는 {i}번이에요.")
            take = input("빵 이름을 적어주세요.   ")
            if take not in bread:
                print("\n제대로 적어요. 기회가 얼마 없으니.\n")
                weight -= 0.2
            else :
                t = bread.index(take)
                if t == num :
                    print("\n축하드려요. 좋은 선택을 내리셨군요.")
                    temp = input("... ")
                    reputation = 1*weight
                    repu_list.append(reputation)
                    break
                else : 
                    print("\n저런. 다시 하세요.")
                    weight -= 0.2
                    continue
        continue
                          


    elif choose == 2 : 
        for m in meet_list:
            print(f"당신은 지금까지 '{species[m]}'를 만나봤습니다. 축하드려요.")
        temp = input("확인했나요?")
        continue
    elif choose == 3 :
        print("당신이 가지고 있는 것.")
        for i in bread :
            print(f" {i} |", end=" ")
        temp = input("\n확인했나요?")
        continue
    elif choose == 4 :
        faction_list.sort()
        print(faction_list)
        print("어떤 팩션을 보고 싶나요?")
        ft = input("자유롭게 입력하세요. ")
        faction_list.append(ft)
        print("\n뭐, 그렇다고 보여준다는 건 아니에요.")
        temp = input("...")
        continue
    elif choose == 5 : 
        print("잘못 누른 거죠?")
        __1 = input("Y / N    ")
        if __1 == "N" or __1 == "n" : 
            print("다시 물을게요. 잘못 누른거죠?") 
            __2 = input ("Y / N    ")
            if __2 == "N" or __2 == "n" :
                print("저런. 그러지 말지. ")
                temp = input("?")
                for i in range(20):
                    print("날"*i + "잊지"*(i+1) + "말아요"*(i+2), end="")
                temp = input("")
                print("\n"*20)
                break
        else : 
            print("다행이네요.")
            input("")
            continue
    elif choose == 6 :
        print("그래요. 또 봐요. 다음이 있다면요.")
        break
    else :
        print("제대로 해요.")
    
if repu_list : 
    print(repu_list)
    print("최고 점수 :", max(repu_list))
    print("평균 점수 :", sum(repu_list)/len(repu_list))
    print("종합 점수 :", sum(repu_list))
else :
    print("기록이 없네요?")

if sum(repu_list) > 2 :
    print("축하드려요. 이제 돌아가실 일만 남았어요. ")
    temp = input("")
else :
    print("저런. 업이 다 지워지기에는 부족하네요.\n다시 저희랑 놀아야겠어요. 푸흐흐.")
    
