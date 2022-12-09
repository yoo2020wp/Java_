print("Github too hard Xd")


print("Day 1 of re-learning Python Since December 09, 2022. The day before my Birthday.")
print("-----------------------------Numbers-----------------------------------------")
#----------------Numbers----------------------------

"""
Numbers
            Example
Integer: 123, -345, 0

float: 123.45, -1234.5, 3.4e10

octal #: 0o34, 0o25

Hexadecimal: 0x2A, 0xFF

"""

#정수형(Integer)이란 말 그대로 정수를 뜻하는 자료형을 말한다. 
#ex)
print("정수형(Integer)이란 말 그대로 정수를 뜻하는 자료형을 말한다. ")
a = 123
a = -127
a = 0

#Floating-point, 소수점이 포함된 숫자를 말한다. 
#ex)
print("\nFloating-point, 소수점이 포함된 숫자를 말한다.")
b = 1.2
print("\nb = 1.2 ->", b)
b = -3.45
print("\nb = -3.45 ->", b)
#아래의 방식은 우리가 일반적으로 볼 수 있는 실수형의 소수점 표현 방식이다.
print("\n아래의 방식은 우리가 일반적으로 볼 수 있는 실수형의 소수점 표현 방식이다.")
a = 4.24E10
print("\n4.24E10 -> ", a)
a = 4.24e-10
print("\n4.24e-10 ->", a)


#8진수와 16진수
print("\n8진수와 16진수")
#8진수(Octal)를 만들기 위해서는 숫자가 0o 또는 0O(대문자 O)(숫자0 + 알파벳 소문자 o 또는 대문자 O)로 시작하면 된다.

a= 0o17
print("\n0o17 ->", a)

#16진수(Hexadecimal)를 만들기 위해서는 Ox로 시작하면 된다.
a = 0x8ff
b = 0xABC

print("\n0x8ff ->", a)
print("\n0xABC ->", a)

#Arithmetic Operator (+, -, *, /)

print("\nArithmetic Operator (+, -, *, /)")

#Exclude +, -. *, /


# % -> 나눗셈 후 나머지를 반환하는 operator (remainder only)
# // -> 나눗셈 후 몫만 반환하는 operator

print("\n실습 타임")
print("\n연산자를 이용해서 숫자 14를 3으로 나누었을 때 몫과 나머지를 확인하라.")
a = 14
b = 3

print("a 를 b와 나누었을 때의 몫은", a//b, "나머지는", a%b, "이다")

print("\n---------------------------------------------------------------------------")
print("---------------------문자열------------------------------")

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