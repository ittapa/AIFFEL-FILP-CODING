import re

#1단계 :  "the"라는 패턴을 컴파일한 후 패턴 객체를 리턴합니다.
pattern = re.compile("the")

# 2단계 : 컴파일된 패턴 객체를 활용하여 다른 텍스트에서 검색을 수행합니다.
pattern.findall('of the people, for the people, by the people')




src = "My name is..."
regex = re.match("My", src)
print(regex)
if regex:
    print(regex.group())
else:
    print("No!")



#- 전화번호(숫자, 기호)
phonenumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone = phonenumber.search('This is my phone number 010-111-1111')
if phone:
  print(phone.group())
print('------')
phone = phonenumber.match ('This is my phone number 010-111-1111')
if phone:
  print(phone.group())

  # - 현재 실행되고 있는 파이썬 실행 파일의 디렉토리를 반환합니다.
import sys

print(sys.executable)


