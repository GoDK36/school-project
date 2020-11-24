class CustomError1(Exception):
    def __str__(self):
        return "띄어쓰기나 특수문자를 제외해주세요."

class CustomError2(Exception):
    def __str__(self):
        return "올바른 형식의 전화번호가 아닙니다."

def PhoneNum(number):
    # 다른 기호 제거하기
    if '-' in number or '#' in number or '.' in number or ' ' in number:
        raise (CustomError1())
    else:
        # 숫자로 이루어졌는지 검사
        number = int(number)
        # 11자리 맞는지 검사 (앞의 0이 없어졌기에 10으로 설정)
        if len(str(number)) != 10:
            raise(CustomError2())
        else:
            # 맨 앞 0이 날라가는 걸 막기 위해 넣은 0
            print("저장된 전화번호는 0{0}입니다.".format(number))


while True:
    try:
        print("전화번호를 입력해주세요.", end=" -> ")
        phone = input()
        PhoneNum(phone)
    except CustomError1 as cerr1:
        print("다시 입력해주세요 ({0})".format(cerr1))
    except CustomError2 as cerr2:
        print("다시 입력해 주세요 ({0})".format(cerr2))
    except ValueError as ver:
        print("숫자만으로 다시 입력해주세요. ({0})".format(ver))
    else:
        break