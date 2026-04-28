# ================================================
# 문제 1. 메모 저장 기능 만들기
# ------------------------------------------------
# 구현 : 간단한 메모 프로그램의 저장 기능. 
#
# 요구사항
# -> 사용자에게 메모 내용을 입력받기.
# -> 날짜별 폴더 생성 및 해당 날짜 폴더에 파일 저장.
#    폴더 생성 함수는 import os 
#                   os.mkdir("폴더명")
# -> 입력받은 내용을 memo_YYYY_MM_DD.txt 파일에 저장.
# -> 저장이 끝나면 "메모가 저장되었습니다."를 출력.
#
# 저장 형식
# -> 날짜
# -> 메모 내용
# -> 기존 내용은 유지하고 새 내용은 뒤에 추가
# ================================================
"""
import os 
import datetime as dt

date = dt.date.today() # 오늘 날짜 뽑기
folder = str(date)  # 폴더명을 날짜로

if not os.path.exists(folder):  # 폴더가 없을 때만 생성
    os.mkdir(folder)

filename = folder + '/memo_' + str(date) +'.txt'
memo = input("메모 내용 : ")

# 파일에 내용 덮어쓰기
with open(filename, 'at', encoding='utf-8') as f:
    f.write(f'{date}\n{memo}\n')
    f.write('----------------------------')

print("메모가 저장되었습니다.")

"""
## --------------------------------------------------
## 함수 이름 : save_memo
## 함수 기능 : 특정 날짜에 메모 저장 후 결과 출력
## 매개 변수 : 날짜, 내용
## 함수 결과 : 파일에 추가 후 메시지 출력       => 반환값 X
#             저장 여부 반환                 => 반환값 전달
## --------------------------------------------------
## 모듈 로딩
import os

## 전역변수
MEMO_PATH = '../../Memo'
MEMBER_PATH = '../../Member'
USER_FILE = f'{MEMBER_PATH}/users.txt'


def save_memo(wdate , memo):
    # (1) Memo 폴더 존재 여부
    if not os.path.exists(MEMO_PATH):
        os.mkdir(MEMO_PATH)
    else:
        print(f'{MEMO_PATH} 존재합니다.')

    # (2) 파일에 기록 : open -> write -> close : with ~ as 구문으로 간소화
    filepath = f"{MEMO_PATH}/memo_{wdate}.txt"
    wCnt = 0    # 내용 유무
    with open(filepath, mode='a', encoding= 'utf8') as F:
        wCnt = F.write("\n[Memo-1]\n")
        wCnt = F.write(memo+"\n")

    # (3) 저장 여부 출력
    msg = "파일 존재하지 않거나 저장 실패" if not os.path.exists(filepath) else f"{wCnt} 개 저장 완료"
    print(msg)

## 입력 받은 메모 저장
## => 날짜, 메모 내용
def input_save_memo():
    inData = input("날짜와 메모 내용 입력(예: 2026_03_01 내용입니다):").strip().split()

    ## 입력 데이터 검사 => 최소 2개 이상 존재
    if len(inData) >=2:
        pass
        # 0번째 원소는 날짜여야 함
        if inData[0].replace("_","").isdecimal():
            # 1번째 원소부터는 메모 내용
            memo = " ".join(inData[1:])
            save_memo(inData[0], memo)
        else:
            print("YYYY_MM_DD 형식의 날짜가 아닙니다.")
    else:
        print("날짜와 메모 내용 중 누락된 부분이 있습니다.")

# ====================================================================================
# 문제 2. 회원 추가 기능 만들기
# ------------------------------------------------
# 구현 : 회원 관리 프로그램의 회원 등록 기능.
#
# 요구사항
# -> 사용자에게 연락처, 이름, 지역, 직업, 취미 입력받기. (input)
# -> 입력받은 정보를 users.txt 파일에 추가 저장.
# -> 이미 저장된 회원 정보는 유지되어야 함.
# -> 저장 후 "회원 등록 완료" 출력.
# -> 이미 존재하는 회원이면 "이미 등록되어 있습니다" 출력.
#
#
# 저장 형식
# -> 연락처          이름       지역      직업     취미
# -> 010-2222-1111  태권V      대구     운동선수  태권도 
# ================================================


"""

import os

phone_number = input("연락처 : ")
name = input("이름 : ")
location = input("지역 : ")
job = input("직업 : ")
hobby = input("취미 : ")

filename = 'users.txt'

# 파일을 먼저 읽어서 기존 내용을 확인
if os.path.exists(filename):
    with open(filename, 'rt', encoding='utf-8') as f:   # 읽기
        content = f.read()
else:
    content = '' # 파일 없으면 빈 문자열로

if phone_number in content: 
    print("이미 등록되어 있습니다")
else:
    with open(filename, 'at', encoding='utf-8') as f:    # 덮어쓰기
        f.write(f'{phone_number}\t{name}\t{location}\t{job}\t{hobby}\n')
        print("회원 등록 완료")

"""

# -----------------------------------------------------
# 함수이름 : create_dir_file
# 함수기능 : 폴더 또는 파일 생성
# 매개변수 : path 생성할 폴더 또는 파일 경로
#           isfile 생성하고자 하는 것이 파일인지 폴더인지
# 함수결과 : 생성 여부 True/False 반환
# -----------------------------------------------------

def create_dir_file(path, isfile= False):
    # 존재 여부 체크
    if not os.path.exists(path):
        # 폴더 생성
        if not isfile:
            os.mkdir(path)
        else:
            # 파일 생성
            with open(USER_FILE,mode='x',encoding='utf8') as F:
                F.write(f"{'연락처':<15}{'이름':<10}{'지역':<10}{'직업':<10}{'취미':<10}\n") # 왼쪽정렬

        return os.path.exists(path)

    else:
        return True

# -----------------------------------------------------
# 함수이름 : join_user
# 함수기능 : 회원 등록 / 파일 저장
# 매개변수 : phone, name, loc, job, hobby   phone - 중복되지 않는 데이터로써 식별자 (id), 전화번호 형식, 숫자 구성 체크
# 함수결과 : 생성 여부 True/False 반환
# -----------------------------------------------------

def join_user(phone, name, loc, job, hobby):

    # 연락처 데이터 형식 및 구성 검사
    if phone.replace("-","").isdecimal():

        # 파일 데이터 추출
        with open(USER_FILE, mode = 'r', encoding='utf8') as rF:
            allDatas = rF.read()

        # 중복 여부 체크
        if phone in allDatas:
            print(f"{phone} 이미 등록된 회원입니다.")
        else:
            # 새로운 회원으로 추가
            with open(USER_FILE, mode = 'a', encoding="utf8") as F:
                wCnt = F.write(f"{phone:<15}{name:<10}{loc:<10}{job:<10}{hobby:<10}\n")
                print(f"{wCnt}개 데이터 저장")
    else:
        print("유효한 데이터가 아닙니다.")

## 함수 테스트 -------------------------------------

if create_dir_file(MEMBER_PATH) and create_dir_file(USER_FILE, True):
    print("폴더 및 파일 준비 완료")

    ## 등록 요청 메시지
    indata = input("회원등록 연락처, 이름, 지역, 직업, 취미 입력:").strip().split(",")

    ## 등록 정보 체크
    if len(indata)==5:
        join_user(*indata) # * : 언패킹
    else:
        print("필수 회원 정보 연락처, 이름, 지역. 직업, 취미가\n모두 입력되었는지 확인바랍니다.")

else:
    print("폴더 및 파일 문제 체크 필요")







