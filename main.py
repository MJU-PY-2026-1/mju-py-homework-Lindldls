# 파일이름 : main.py (4차과제까지)
# 작 성 자 : 60251684 전자공학 이인 

import random as r

# --------------------------------------전역변수
shop_name = ""
bread = ["곰보빵", "사과빵", "마늘빵", "뼈다귀", "생크림빵", "칼빵"]
faction_list = []

faction_dict = { "default" : ["좀비", "마녀", "뱀파이어", "웨어울프", "밴시", "목 없는 기사"]}
active_faction = "default" # 현재 찾아오는 팩션 

meet_list = []

reputation = 0.0
repu_list = []

# ----------------------------------시작연출
def intro():
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

# -----------------------------빵집 이름 입력
def makeshop():
    global shop_name 
    shop_name = input("\n빵집 이름을 입력해주세요. 이왕이면 기억에 잘 남는 거로요.")


def load_data():
    global faction_list, faction_dict
    try : 
        with open("faction_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                faction_list.append(parts) # 이중 리스트에서 불러온 데이터를 딕셔너리 형태로 변환해서 저장
                if len(parts) >= 7:
                    faction_dict[parts[0]] = parts[1:7]
        print("\n옛날 기록을 잘 불러왔어요. 도움이 될까요?")
    except FileNotFoundError:
        print("\n이전 기록이 없어요. 저런.")
        input("...")
        
def save_data(): #파일저장
    with open("faction_data.txt", "w", encoding="utf-8") as file:
        for i in range(len(faction_list)):
            for j in range(len(faction_list[i])):
                file.write(faction_list[i][j])
                if j != (len(faction_list[i])-1):
                    file.write(",")
            file.write("\n")
    print("\n당신이 적은 게 무사히 기록되었어요.")
            
# -------------------------------손님 받기
def meet_customer():
    global weight 
    weight = 1.0
    print("\n손님을 받으시는군요. 열심히 하시네요.")
    temp = input("그럼 주사위를 굴려볼까요? 행운을 빕니다.")
    num = r.randint(0,5)

    current_species = faction_dict[active_faction][num]
    meet_list.append(current_species)
    
    
    input(f"{num+1}. 좋은 숫자 같나요?")
    print(f"\n{current_species}를 모시겠습니다. 기호를 잘 맞춰주세요.")
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
            if t == num:
                print("\n축하드려요. 좋은 선택을 내리셨군요.")
                temp = input("... ")
                reputation = 1*weight
                return reputation
            else : 
                print("\n저런. 다시 하세요.")
                weight -= 0.2
    return 0

# ----------------*******도감 출력
def show_book():
    if meet_list:
        for sp in meet_list:
            print(f"당신은 지금까지 '{sp}'를 만나봤습니다.")
        temp = input("확인했나요?")
    else:
        print("\n아직 만난 분이 없으세요.")
        temp = input("확인했나요?")

# -----------------빵 종류
def showbread():
    print("\n당신이 가지고 있는 것.\n")
    for i in bread :
        print(f" {i} |", end=" ")
    temp = input("\n확인했나요?")

def print_faction():
    print("\n 현재 저장된 팩션 이중 리스트 : ")
    if not faction_list :
        print("등록된 커스텀 팩션이 없어요.")
        return
    for i in range(len(faction_list)):
        print(f"팩션 [{faction_list[i][0]}] : ", end="")
        for j in range(1, len(faction_list[i])):
            print(faction_list[i][j], end="/")
        print("")

# ---------------------팩션 기능
def faction_menu():
    faction_list.sort()
    print_faction()
            
    ft = input('추가할 팩션 이름? : ')
    temp_list = [ft]
    faction_list.append(temp_list)

def use_faction( ch ):
    global faction_dict
    for i in faction_list:
        if i[0] == ch:
            print(f"\n{ch}의 하위 종족명을 6개 입력해주세요.")
            new_sp = []
            for j in range (6):
                sub = input(f"{j+1}번째 종족 : ")
                new_sp.append(sub)
            i[1:] = new_sp

            faction_dict[ch] = new_sp
            print("\n저장 완료했어요. 이제 적용 가능해요.")
            return None
        print("\n없는 팩션이잖아요. 조심해요.")

def apply_faction():
    global active_faction
    print("\n=========현재 적용 가능 팩션=========")
    for key, value in faction_dict.items():
        print(f"{key} : {value}")

    sel = input("\n어떤 손님을 받으시겠어요? 이름을 정확히 적어요.\n : ")
    if sel in faction_dict:
        if len(faction_dict[sel]) >= 6:
            active_faction = sel
            print(f"\n잘 적용했어요. 이제부터는 {sel} 팩션의 손님들이 방문해요...")
            input("...")
        else:
            print("\n하위 종족이 6개는 넘어야 재미가 있어요.")
    else:
        print("\n그런 팩션은 없는데요.")
        input("...")

# -----------------------------점수 분석
def analyze_score():
    if repu_list:
        print("\n====결과 분석 ====")
        print("최고 점수 :", max(repu_list))
        print("평균 점수 :", sum(repu_list)/len(repu_list))
        print("종합 점수 :", sum(repu_list))
        if sum(repu_list) > 2 :
            print("축하드려요. 이제 돌아가실 일만 남았어요. ")
            temp = input("")
        else :
            print("저런. 업이 다 지워지기에는 부족하네요.\n다시 저희랑 놀아야겠어요. 푸흐흐.")
            temp = input("...")
            return 99
    else :
        print("기록이 없네요?")






# ---------------------------main
intro()
makeshop()
load_data()



day = 5
while True:

    weight = 1.0
    print("\n"*5)
    print(f"{shop_name} 빵집이에요. 장사가 잘 되나요? {day}일 남았어요.")
    print("-"*50)
    print("1. 손님 받기")
    print("2. ■■ 도감")
    print("3. 당신에게 있는 무언가.")
    print("4. 팩션 관리")
    print("5. 추천하지 않습니다. 선택하지 마세요.")
    print("6. ...오늘은 그만하실 건가요?")
    print("7. 이름을 바꾸실래요?")

    try : 
        ch = input("무엇을 하시겠습니까? 번호로 입력하세요. Ex : 1\n")
        choose = int(ch)
    except ValueError:
        print("\n숫자만 입력해요. 규칙을 잊지 마요.")
        temp = input("...")
        continue
    
    if ch not in ("1", "2", "3", "4", "5", "6", "7") :
        print("이게 아닐 텐데요. 다시 입력해주세요. ")
        temp = input("...")
        continue

    
    if choose == 1:
        score = meet_customer()
        repu_list.append(score)
        day -= 1
        
    elif choose == 2 : 
        show_book()
        
    elif choose == 3 :
        showbread()
        
    elif choose == 4 :
        try :
            temp = int(input("새로 만드는 거면 1번, 있는 팩션에 추가하는 거면 2번. \n그냥 보는 건 3번. 적용하는 건 4번. "))
        except ValueError:
            print("숫자로 대답해요.")
            continue
            
        if (temp == 1):
            faction_menu()
        elif (temp == 2):
            print_faction()
            name = input("수정할 팩션 이름을 선택해요. ")
            use_faction(name)
        elif (temp == 3):
            print_faction()
            temp = input("...")
        elif (temp == 4):
            apply_faction()
        else : 
            print("뭐에요.\n")
            temp = input("...")
            
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
        save_data()
        break
    elif choose == 7 :
        print("이름을 바꾸다니. 처음에 잘 정하지 그랬어요.")
        makeshop()
        print("이번에는 오래 갔으면 좋겠는데.")
        temp = input("...")
        
    else :
        print("제대로 해요.")
    
    if day == 0 :
        re = analyze_score()
        if re == 99:
            day = 3
            repu_list = []
            print(f"한 번 더 기회를 드릴게요. 이번에는 {day}일.")
            temp = input("...)")
            continue
        else :
            break
        
