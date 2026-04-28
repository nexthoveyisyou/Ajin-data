## ---------------------------------------------------------------------
## 경로
## - 절대경로 : Windows OS 관점에서는 드라이브 C,D 기준으로 경로/파일 위치 설정
##             Linux OS 관점에서는 루트(/)
##             [예] C:\Users\kwon\Desktop\PYTORCH_IMAGE\data\flower.jpg
##
## - 상대경로 : 현재 파일이 있는 위치를 기준으로 경로/파일 위치 설정
#              특별한 의미를 가진 . , .. 기호를 사용함
#              [예] ../data/flower.jpg
## ---------------------------------------------------------------------
## Python 상대경로 설정
## - Run and Debug 패널 메뉴 선택 >> create a launch.json file 클릭
##   -> .vscode/launch.json 파일에 
##      "cwd":"${fileDirname}" 

## - Manage 패널 메뉴 선택 >> Settings 항목 클릭
##   -> 검색어 입력 창에 python terminal 입력
##   -> Python > Terminal: Execute In File Dir 메뉴 체크

## ------------------------------------------------------------------
## 실행 및 체크
## (1) 오른쪽 상단 ▷ 메뉴 클릭
## (2) 왼쪽 상단 Run > Run without Debugging Ctrl+F5
## ------------------------------------------------------------------
import os
print("현재 작업 디렉터리:", os.getcwd())    # current working directory : 현재 작업 폴더

num = 2025
print(f'num : {num}')
