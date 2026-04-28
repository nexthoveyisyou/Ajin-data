## =======================================================
## 파일 복사 기능 구현
## - 파일명 : member.txt
## - 구  현 
# `(1) member.txt 파일 생성
##     이름   성별   지역
##    -------------------
##    홍길동   남자   부산
##    마징가   여자   대구
##    베트맨   남자   서울
## =======================================================



ORG_FILE_NAME = 'member.txt'
CPY_FILE_NAME = 'member_copy.txt'

with open(ORG_FILE_NAME, mode= 'w', encoding= 'utf8') as F:
    F.write("  이름     성별   지역  \n")
    F.write("-----------------------\n")
    F.write("  홍길동   남자   부산  \n")
    F.write("  마징가   여자   대구  \n")
    F.write("  베트맨   남자   서울  \n")


## =======================================================
## - (2) 복사 기능
##   member_copy.txt
## =======================================================
## 원본 파일 내용 => 복사 파일 넣기

"""
with open(ORG_FILE_NAME, mode= 'r', encoding= 'utf8') as orgF:
    all_data = orgF.read()

with open(CPY_FILE_NAME, mode= 'w', encoding= 'utf8') as cpyF:
    cpyF.write(all_data)

"""

with open(ORG_FILE_NAME, mode= 'r', encoding= 'utf8') as orgF:
    with open(CPY_FILE_NAME, mode= 'w', encoding= 'utf8') as cpyF:
        cpyF.write(orgF.read())
   