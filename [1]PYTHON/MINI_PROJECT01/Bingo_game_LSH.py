## ===========================================================================================
## 빙고 게임
## ===========================================================================================

import random                     # 랜덤 모듈 활용

## ---------------------------------------------
## 1단계: 빙고 이중 리스트 생성 gen_bingo()
## ---------------------------------------------
# 사용할 파이썬 기능:
#   - list(range(...))           → 1~25 숫자 목록 만들기
#   - random.randint(0, len-1)   → 남은 목록에서 무작위 인덱스 선택
#   - list.pop(index)            → 선택한 인덱스 값을 꺼내면서 목록에서 제거 (중복 방지)
#   - 중첩 for 반복문             → 5행 × 5열 이중 리스트 구성



def gen_bingo():
    numbers = list(range(1, 26))
    rows = []                                            # 전체 행들의 빈 리스트
    for _ in range(5):
        row = []                                         # 각 행의 빈 리스트
        for _ in range(5):
            index = random.randint(0, len(numbers) - 1)  # 각 인덱스 번호 (0부터 24)
            number = numbers.pop(index)                  # 전체 리스트에서 값을 꺼냄
            row.append(number)                           # 각 row에다가 꺼낸 번호 추가
        rows.append(row)                                 # 전체 행 리스트에 추가
    return rows                                          # 2차원 행 리스트 리턴


## ---------------------------------------------
## 2단계: 빙고판 출력 함수 show_bingo()
## ---------------------------------------------
# 사용할 파이썬 기능:
#   - for 반복문 (이중 리스트 순회)
#   - " ".join()  → 칸 너비 맞춰서 보기 좋게 출력

board = gen_bingo()                                      # 빙고 리스트 생성

def show_bingo(board):                                   # 매개변수를 board로
    for row in board:
        print(" ".join(f"{str(n):>2}" for n in row))     # 반복문을 활용해서 join을 통해 row마다 한 줄 출력
    print('-' * 20)                                      

## ---------------------------------------------
## 3단계: 숫자 입력 받아 칸에 X값 표시하기 user_num()
## ---------------------------------------------
# 사용할 파이썬 기능:
#   - input() + int()        → 사용자 입력 받기
#   - 중첩 for 반복문         → 이중 리스트 전체 순회
#   - enumerate()            → 인덱스와 값을 동시에 얻기
#   - 조건문 if              → 입력값과 일치하는 칸 찾기
#   - 문자열 'X'로 값 교체 

def user_num(board):
    found = False
    num_str = input("원하는 숫자를 입력하시오(1~25) : ")
    print('-' * 20)

    if not num_str.lstrip('-').isnumeric() or num_str.count('-') > 1:  
        # ex) -1 입력하면 isnumeric을 통해 숫자 판명남 / -만 단독으로 입력하면 문자로 판명
        print('-' * 20) 
        print("숫자만 입력하시오.")
        print('-' * 20) 
        return
    
    num = int(num_str)

    if num<1 or num>25:     # 범위 초과 검사
        print('-' * 20) 
        print("1~25 사이의 숫자를 입력하시오.")
        print('-' * 20) 
        return

    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == num:
                board[r][c] = 'X'
                found = True
                break
        if found:
            break
    if not found:
        print('-' * 20) 
        print("이미 입력한 값입니다.")
        print('-' * 20)            
            

## ---------------------------------------------
## 4단계: 빙고 완성 여부 확인 함수 judge_bingo()
## ---------------------------------------------
# 사용할 파이썬 기능:
#   - for 반복문 + if          → 한 줄이 전부 'X'인지 직접 확인
#   - for ~ else 구조          → break 없이 끝나면 else 실행 (빙고 완성)
#   - 리스트 컴프리헨션         → 열(column) 추출

#   - 대각선 인덱스 규칙
#     좌→우 대각선: board[i][i]
#     우→좌 대각선: board[i][4-i]
#   - 완성된 빙고 줄 수 세기    → 몇 줄 빙고인지 반환


def judge_bingo(board):
    count = 0                    # 빙고 개수 판별하는 변수

    # 가로 5줄 확인
    for r in range(5):
    # board[r] 한 줄이 전부 'X'인지 확인
        for cell in board[r]:
            if cell != 'X':      # 'X'가 아닌 게 하나라도 있으면
                break            # 빙고가 아니므로 종료하고
        else:
            count+=1             # 그렇지 않으면 빙고 카운트

    # 세로 5줄 확인
    for c in range(5):
    # [board[r][c] for r in range(5)] 로 열을 확인
        col = [board[r][c] for r in range(5)]
        for cell in col:
            if cell !='X':      # 'X'가 아닌 게 하나라도 있으면
                break           # 빙고가 아니므로 종료하고
        else:
            count+=1            # 그렇지 않으면 빙고 카운트


    # 대각선 2줄 확인
    # board[i][i]  (좌→우)
    for i in range(5):
        if board[i][i] != 'X':
            break
    else:
        count+=1

    # board[i][4-i] (우→좌)
    for i in range(5):
        if board[i][4-i] != 'X':
            break
    else:
        count+=1

    return count 

## ---------------------------------------------
## 5단계: 다시하기 함수 restart_game()
## ---------------------------------------------
# 사용할 파이썬 기능:
#   - input()   → 다시하기 여부 입력
#   - return    → 새 빙고판 또는 None 반환

def restart_game():
    again = input("다시 하시겠습니까? (y/n) : ")
    if again == 'y':
        new_board = gen_bingo()
        show_bingo(new_board)
        return new_board
    return None          # n 입력 시


## ---------------------------------------------
## 6단계: 게임 루프 (전체 흐름)
## ---------------------------------------------
# 사용할 파이썬 기능:
#   - while True 무한 루프   → 게임이 끝날 때까지 반복
#   - break                 → 빙고 완성 시 루프 종료
#   - 앞에서 만든 함수들을 순서대로 호출
## ---------------------------------------------
# 전체 흐름:
#   1) 빙고판 생성 → 출력
#   2) 숫자 입력 → 칸 표시 → 빙고판 다시 출력
#   3) 빙고 완성 줄 수 확인
#   4) 3줄 빙고면 게임 종료 및 다시하기

show_bingo(board)
prev_count = 0                  # 이전 count
turn = 0                        # 몇 턴만에 빙고를 완성했는지

while True:
    user_num(board)             # 숫자 입력 받아 X 표시
    turn += 1                   # 매 입력마다 턴 수 카운트

    show_bingo(board)           # 변경된 빙고판 보여주고
    count = judge_bingo(board)  # 빙고 수 카운트

    if count != prev_count:                # 이전 count와 달라졌을 때만 출력 가능
        if count == 1:
            print("1줄 빙고! 남은 빙고 수는 2줄입니다")
        elif count == 2:
            print("2줄 빙고! 남은 빙고 수는 1줄입니다")

        prev_count = count                 # 이전 count에 현재 count 저장

    if count == 3:
        print(f"3줄 빙고! {turn}번 만에 완성!")

        new_board = restart_game()         # 다시하기 함수 호출
        if new_board is not None:          # None이 아니면 (= y를 입력했으면) 게임 재시작
            board = new_board              # 새 빙고판으로 교체
            turn = 0                       # 턴 초기화
            prev_count = 0                 # 빙고 수 초기화
        else:                              # None이면 (= n을 입력했으면) 루프 종료
            break