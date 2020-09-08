# python 문자열


## python3 문자열 처리 
-기본 str
```
>>> str1 = b'hello' #binary
>>> str2 = 'hello' # str
>>> str3 = u'hello' # unicode
>>> print(type(str1), type(str2), type(str3))
<type 'bytes'>, <type 'str'>, <type 'str'>
```

## 개행 문자
```
\'
\"
\t  탭
\n  줄바꿈
\\ 역슬래시
```

## str
 - startswith
 - endwith
 - strip, lstrip, rstrip
 - upper
 - lower
 - capitalize
 - isX, supper/ lower/ title / alpha / alnum / decimal
 - join / spilt
 - replace
  - \t, \n , \r(케리지 리턴)
 
 ## 정규표현식
 ``` import re ```
- .compile("~~") #패턴객체
- findall  # 패턴 찾기
- search() : 일치하는 패턴 찾기 * 일치 패턴이 있으면 MatchObject를 반환합니다.
- match() : search()와 비슷하지만, 패턴이 검색대상에 처음부터 일치해야 합니다.
- findall() : 일치하는 모든 패턴 찾기 * 모든 일치 패턴을 리스트에 담아서 반환합니다.
- split() : 패턴으로 나누기
- sub() : 일치하는 패턴으로 대체하기
- 아래는 search(), match() 등이 리턴하는 MatchObject가 가진 메소드입니다.
- group() : 실제 결과에 해당하는 문자열을 반환합니다.

## file
- with as   # close 들어가있음.

- f.read() : 파일을 읽는다.
- f.readline() : 파일을 한 줄씩 읽는다.
- f.readlines() : 파일 안의 모든 줄을 읽어 그 값을 리스트로 반환한다.
- f.write(str) : 파일에 쓴다. 문자열 타입을 인자로 받는다.
- f.writelines(str) : 파일에 인자를 한 줄씩 쓴다.
- f.close() : 파일을 닫는다.
- f.seek(offset) : 새 파일의 위치를 찾는다.
 
 
 ## os  sys
 
- sys.path : 현재 폴더와 파이썬 모듈들이 저장되어 있는 위치를 리스트 형태로 반환
- sys.path.append() : 자신이 만든 모듈의 경로를 append 함수를 이용해서 추가함으로써 추가한 디렉토리에 있는 파이썬 모듈을 불러와 사용할 수 있다.
- os.chdir() : 디렉토리 위치 변경
- os.getcwd() : 현재 자신의 디렉터리 위치를 반환
- os.mkdir() : 디렉토리 생성
- os.rmdir() : 디렉토리 삭제 (단, 디렉토리가 비어 있을 경우)
- glob.glob() : 해당 경로 안의 디렉토리나 파일들을 리스트 형태로 반환
- os.path.join() : 경로(path)를 병합하여 새 경로 생성
- os.listdir() : 디렉토리 안의 파일 및 서브 디렉토리 리스트
- os.path.exists() : 파일 혹은 디렉토리의 경로 존재 여부 확인
- os.path.isfile() : 파일 경로의 존재 여부 확인
- os.path.isdir() : 디렉토리 경로의 존재 여부 확인
- os.path.getsize() : 파일의 크기 확인
 
## pands csv file read,write method 제공
- df = pd.read_csv('pandas.csv')
- df.head()

## xml library - 
```import xml.etree.ElementTree as ET```
- Element() : 태그 생성
- SubElement() : 자식 태그 생성
- tag : 태그 이름
- text : 텍스트 내용 생성
- attrib : 속성 생성
- dump()
- 생성된 XML 요소 구조를 시스템(sys.stdout)에 사용합니다.
- write() : XML 파일로 저장
- 리스트(list)와 유사한 메소드를 제공 :append, insert, remove, pop

## json 파싱
``` import json ```
- json.load(f)
- 


## library

### os
### sys


### Element Tree libarry
``` import xml.etree.ElementTree as ET ```
- Element() : 태그 생성
- SubElement() : 자식 태그 생성
- tag : 태그 이름
- text : 텍스트 내용 생성
- attrib : 속성 생성