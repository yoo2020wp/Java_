print("---------------------문자열------------------------------")


print("Index\n")
"""
1. Line 10 ~ 89 -> 파이썬에서 문자열을 표현하는 방법

2. Line 94 ~ 157 -> 여러 줄인 문자열을 변수에 대입하고 싶을 때 (\n, \t... etc)

3. Line 160 ~ -> 문자열 연산하기 (문자열 더하기, 곱하기, 길이 구하기, 인덱싱과 슬라이싱)
"""

"""
파이썬에서 문자열을 표현하는 방법은 총 4가지가 있다.
There are 4 ways to express String in Python.

1. 큰따옴표로(")로 양쪽 둘러싸기 Double Quotation 

2. 작은따옴표(')로 양쪽 둘러사기 Single Quotation

3. 큰따옴표 3개를 연속으로("*3) 써서 양쪽 둘러싸기 Putting Double Quotations 3 times

4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기 Putting Single Quotations 3 times
"""

#Example

print("\n1. Hello World")

print('\n2. Python is fun for now')

print("""\n3. Life is too short, You need Python""")

print('''\n4. My favorite food is mopo tofu''')


#As you can see the result, you can use 4 ways to print the sentences using quotations.
#Reason why:
"""
1. 문자열에 작은따옴표(') 포함시키기 Include Single Quotation in String

ex) Python's favorite food is perl -> 문장 안에 작은 따옴표를 넣고 싶으면 문자열을 큰 따옴표로 둘러싸야한다. If you want to put single quotation in a sentence, you need to use Double Quotation in String.
 
Error occurs if:

food = 'Python's favorite food is perl'
Output -> File "<stdin>", Line 1
            food = Python's favorite food is perl'
                                   ^
          SyntaxError: invalid syntax

2. 문자열에 큰따옴표(") 포함시키기 Include Double Quotation in String

ex) Python is very easy." he says.

위와 같이 큰따옴표(")가 포함된 문자열이라면 문자열을 작은 따옴표(')로 둘러싸면 된다. To include Double Quotation in a sentence, You need to put single quotation in String


3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기 Use BackSlash(\) to Include Single and Double Quotation in String and a sentence

작은따옴표(')나 큰따옴표(")를 문자열에 포함시키는 또 다른 방법은 백슬래시(\)를 이용하는 것이다. 백슬래시를 사용하면 백슬래시 뒤의 작은따옴표나 큰따옴표는 문자열을 둘러싸는
기호의 의미가 아니라 문자 ('), (") 그 자체를 뜻하게 된다.


"""
print("\n1111111111111111111111111111111111111111111111111111111111111\n")

#Example for #1

food = "Python's favorite food is perl"

print("\n1.", food)

print("\n222222222222222222222222222222222222222222222222222222222\n")

#Example for #2

say = '"Python is very easy." he says.'

print("\n2.", say)

print("\n3333333333333333333333333333333333333333333333333333333333333\n")

#Example for #3

food = 'Python\'s favorite food is perl'

say = "\"Python is very easy.\" he says."

print("\n3.", food)
print("\n3.", say)

print("--------------------------------------------------------------------------------------------------------------------")

"""
여러 줄인 문자열을 변수에 대입하고 싶을 때:
문자열이 항상 한 줄짜리만 있는 것은 아니다. 다음과 같이 여러줄의 문자열을 변수에 대입하려면 어떻게 처리해야할까?

Expected Output:
Life is too short
You need Python


1. 줄을 바꾸는 Escape Code '\n' 삽입하기.

하지만, 이 방법을 사용할 때는 읽기에 불편하고 줄이 길어지는 단점이 있다.


2. 연속된 작은 따옴표 3개(''') 또는 큰 따옴표 3개("*3) 사용하기

1번의 단점을 극복하기 위해 파이썬에서는 다음과 같이 작은 따옴표 3개 또는 큰 따옴표 3개를 사용한다.
"""

print("\n1111111111111111111111111111111111111111111111111111111111111111111111111")

#Example for #1

multiline1 = "Life is too short\n   You need Python"

print("\n1.", multiline1)


print("\n222222222222222222222222222222222222222222222222222222222222222222222222222")

#Example for #2

multiline2_1 = '''
Life is too short
You need Python
'''

multiline2_2 = """
Life is too short
You need Python
"""

print("\n2.1", multiline2_1)
print("\n2.2", multiline2_2)

"""
Types of Escape Code


    Code                Explanation

1. \n                   문자열 안에서 줄을 바꿀 때 사용
2. \t                   문자열 사이에 탭 간격을 줄 때 사용
3. \\                   문자 \를 그대로 표현할 때 사용
4. \'                   작은 따옴표(')를 그대로 표현할 때 사용
5. \"                   큰 따옴표(")를 그대로 표현할 때 사용
6. \r                   캐리지 리턴(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
7. \f                   폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
8. \a                   벨 소리(출력할 때 PC 스피커에서 '삑'소리가 난다)
9. \b                   백스페이스
10.\000                 Null 문자


**이 중에서 활용 빈도가 높은 것은 \n, \t, \\, \', \"이다. 나머지는 프로그램에서 잘 사용하지 않는다.
"""

print("\n문자열 연산하기")

"""
문자열 연산하기

파이썬에서는 문자열을 더하거나 곱할 수 있다. 다른 언어에서는 쉽게 찾아볼 수 없는 재미있는 기능으로, 우리 생각을 그대로 반영해 주는 파이썬만의 장점이라고 할 수 있다.

1. 문자열 더해서 연결하기 (Concatenation)

2. 문자열 곱하기

Line 186 ~ 192번을 보면 코드에서 *의 의미는 우리가 일반적으로 아는 곱하기가 아니다.
아래의 코드에서 a * 2는 a를 두 번 반복하라는 뜻이다.
즉, *는 문자열의 반복을 뜻하는 의미로 사용되었다.

3. 문자열 곱하기 응용

print("-" * 50)

4. 문자열 길이 구하기
문자열의 길이는 "len" 함수(length)를 사용하면 구할 수 있다. len 함수는 print 함수처럼
파이썬의 기본 내장 함수로 별다른 설정 없이 사용이 가능하다.

5. 문자열 인덱싱과 슬라이싱

인덱싱(Indexing)이란 무엇인가를 '가리킨다'는 의미이고, 슬라이싱(Slicing)은 무엇인가를 '잘라낸다'는 의미이다. 
Do it!점프 투 파이썬 - 전면 개정판 51쪽 참고

Ex) L i f e   i s   t o o   s h o r t ,   Y o u   n e e d   P y t h o n
    0                   1                   2                   3 
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3
    
    "Life is too short, You need Python" 문자열에서 L은 첫 번째 자리를 뜻하는 숫자 0,
    바로 다음인 i는 1 이런 식으로 계속 번호를 붙인 것이다. 중간에 있는 short의 s는 12가 된다.
"""


print("11111111111111111111111111111111111111111111111111111111")
#Example for #1

head = "Python"
tail = " is fun!"

print("\n", head + tail)


print("222222222222222222222222222222222222222222222222222222222222\n")
#Example for #2

a = "python"

b = a * 2

print(b)

print("333333333333333333333333333333333333333333333333333333333333333\n")
#Example for #3

print("=" * 50)
print("My Program")
print("=" * 50)

print("\n444444444444444444444444444444444444444444444444444444444444444444444\n")

a = "Life is too scary"

print(a, "<- length:", len(a))

#중간 실습
#'You need python'문장을 만들고 길이를 구해보자.

print("중간 실습 문제 답안")

a = "\'You need python\'"

print(a, len(a))


