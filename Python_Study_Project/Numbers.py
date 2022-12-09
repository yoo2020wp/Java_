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