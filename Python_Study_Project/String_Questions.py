lline = "-" * 70


#Example #1 인덱싱
print("\nExample #1 인덱싱")
a = "Life is too short, You need Python"

print(a[3])
print(a[12])
print(a[0], a[1], a[2], a[3], a[4])


#Example #2 인덱싱 음수 ver.
print("\nExample #2 인덱싱 음수")
print(a[-1])
print(a[-2])


#Example #3 슬라이싱(인덱스를 활용한) ver.

print("\nExample #3 슬라이싱")
b = a[0] + a[1] + a[2] + a[3]

print(b)

#Example #4 슬라이싱
print("\nExample #4 슬라이싱")
print("a에 저장한 문자열에서 \"Life\"를 출력하라.\n")
print("오답: ", a[0:3])
print("정답: ", a[0:4])

#Example #5 슬라이싱 활용 (시작번호, 끝번호)
print("\nExample #5")
print(a[19:])
#a[시작 번호: 끝 번호]에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.

#Example #6 슬라이싱 활용 (시작번호, 끝번호)
print("\nExample #6")
print(a[:17])
print(a[:13])
#a[시작 번호: 끝 번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.

#Example #7 슬라이싱 활용 (시작번호, 끝번호)

print("\nExample #7")
print(a[:])
#a[시작 번호: 끝 번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다.

#Example #8 슬라이싱 활용 (시작번호, 끝번호)

print("\nExample #8")
print(a[19:-7])
#위 소스코드에서 a[19:7]이 뜻하는 것은 a[19]에서부터 a[-8]까지를 말한다. 이 역시 a[-7]은 포함이 되지 않는다.
#Example #8 문자열을 슬라이싱으로 나누기
print("20010331Rainy를 연도 2001, 월과 일을 나타내는 0331, 날씨를 나타내는 Rainy의 세 부분으로 나누어라.")

a = "20010331Rainy"
date = a[:8]
weather = a[8:]

print(date)
print(weather)

print(lline)
year = a[:4] #-> 처음부터 a[3]까지

month = a[4:8] #-> a[4]부터 a[7]까지

weather = a[8:] #-> a[8]부터 마지막까지

print("year:", year, "\nmonth:", month, "\nweather:", weather)


print(lline)

print(lline)

#Example #9 숫자 대입
print("Example #9")
print("I eat %d apples." %3)

print(lline)
#Example #10 문자열 대입
print("Example #10")
print("I eat %s apples." %"five")

print(lline)
#Example #11 숫자 값을 나타내는 변수로 대입
print("Example #11")
number = 3

print("I eat %d apples." %number)

print(lline)

#Example #12 문자열 안에 2개 이상의 값을 넣기
print("Example #12")
number = 10

day = "three"

print("I ate %d apples. so I was sick for %s days." %(number, day))

print(lline)

print(lline)
#Example #13
print("Example #13")
print("I have %s apples." %3)
print("Rate is %s." %3.234)

print(lline)

#Example #14
print("Example #14")
print("Successful rate is %d%%." %99)

print(lline)

#Example #15
print("Example #15")
print("%10s" % "hi")
#위의 소스코드를 인덱스열로 표현하면 이렇다.
#0 1 2 3 4 5 6 7 h i

#0부터 7까지는 공백, h는 8, i는 9에 들어간다

print(lline)
#Example #16
print("Example #16")
print("%-10sjane" % 'hi')
print(lline)

#Example #17
print("Example #17")
print("%0.4f" %3.4215555)

print(lline)
#Example #18
print("Example #18")
print("%10.4f" % 3.4215555)


print(lline)

#Example #19
print("Example #19")
print("I eat {0} apples.".format(3))

print(lline)
#Example #20
print("Example #20")
print("I eat {0} apples.".format("five"))


print(lline)

#Example #21
print("Example #21")

number = 12
print("I eat {0} apples.".format(number))

print(lline)

#Example #22
print("Example #22")

number = 10
day = "three"

print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

print(lline)
#Example #23
print("Example #23")

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day = 3))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day = "three"))

print(lline)


#Example #24
print("Example #24")

print("I ate {0} apples. so I was sick for {day} days.".format(10, day = 3))
#format(10, day = 3)에서 볼 수 있듯이, 인덱스와 함수 둘 다 활용하여 사용 가능하다.

print(lline)
#Example #25

print("Example #25")
#왼쪽 정렬
print("{0:<10}".format("hi"))
#:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.


print(lline)
#Example #26
print("Example #26")
#오른쪽 정렬
print("{0:>10}".format("hi"))

print(lline)
#Example #27
print("Example #27")
#가운데 정렬
print("{0:^10}".format("hi"))

print(lline)

#Example #28
print("Example #28")
#공백채우기
print("1. {0:=^10}".format("hi"))
print("2. {0:!^10}".format("bro"))
print("3. {0:!<10}".format("bro"))
print("4. {0:!>10}".format("bro"))


print(lline)

#Example #29
print("Example #29")

y = 3.14159265

print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

print(lline)
#Example #30
print("Example #30")
print("{{and}}".format())
print("{{However}}".format())
print("{{Putting two Curly Brackets makes you print a curly bracket}}".format())


print(lline)

#Example #31
print("Example #31")
name = "Hunter"

Age = 22

print(f"My name is {name}, and I am {Age} years old.")
print(f"My name is {name}, and I am {Age + 1} years old in Korea")


#Example #32
print("Example #32")

dic = {'name':"Hunter", "age": 22}
print(f"My name is {dic['name']}, and I am {dic['age']} years old.")
print(f'My name is {dic["name"]}, and I am {dic["age"]} years old.')
#TIP: Make Sure to remember to use 'Single Quotation' when you are using "Double Quotation" with print function.
#     Make Sure to remember to use "Double Quotation" when you are using 'Single Quotation' with print function.

print(lline)