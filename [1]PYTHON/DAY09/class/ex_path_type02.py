## ---------------------------------------------------------------------
## 경로
## - 절대경로 : Windows OS 관점에서는 드라이브 C,D 기준으로 경로/파일 위치 설정
##             Linux OS 관점에서는 루트(/)
##             [예] C:\Users\kwon\Desktop\PYTORCH_IMAGE\data\flower.jpg
##
## - 상대경로 : 현재 파일이 있는 위치를 기준으로 경로/파일 위치 설정
#              특별한 의미를 가진 . , .. 기호를 사용함
#              [예] ../data/flower.jpg
## ------------------------------------------------------------------
## ------------------------------------------------------------------
## 파일의 경로
## (1) tmp_in.txt 는 현재 파이썬 코드 파일과 동일한 폴더에 존재
## (2) tmp_out.txt : [1]PYTHON 폴더 안에 존재
##                   현재 파이썬 코드 파일과 다른 위치에 있음
## ------------------------------------------------------------------
## 파일 및 경로 관련 함수, 클래스 존재하는 파일 : 모듈
## 모듈을 코드에 포함하기 문법 => import 모듈파일명
import os

## [실습] check.py 파일의 절대경로, 상대경로를 출력하기

file_path_abs1 = r'C:\Users\KDT-008\Desktop\KDT_14\[1]PYTHON\DAY01\class\check.py'
file_path_re1 = r'../../DAY01/class/check.py'

print(file_path_abs1, os.path.exists(file_path_abs1), sep = ' => ')
print(file_path_re1, os.path.exists(file_path_re1), sep = ' => ')




