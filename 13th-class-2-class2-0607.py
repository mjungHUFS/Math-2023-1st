## 용어정리 ===============================================================
# 객체(object) 속성을 가질 수 있는 모든 것
# 클래스(class) 객체를 쉽고 편리하게 생성하기 위해 만들어진 구문
# 인스턴스 (instance) 클래스를 기반으로 생성한 객체
# 생성자(constructor) 클래스 이름과 같은 인스턴스를 생성할 때 사용하는 함수
# 메소드(method) 클래스가 가진 함수
#==========================================================================

#===========================
# isinstance(인스턴스,클래스) 함수
#===========================
class Student:
    def __init__(self):
        pass



# 클래스의 상속 =================
class Human: # 부모클래스
    def __init__(self):
        pass

class Student(Human):# 자식클래스 
    def __init__(self):
        pass


# 예제 ==========================
class Student:
    def study(self):
        print("공부를 합니다")
class Teacher:
    def teach(self):
        print("학생을 가르칩니다")




#isinstance는 주로 객체의 자료형을 판단할 때 사용 ===================
def factorial(n):



##=============================================
## __이름__() 함수: 특수한 상황에 자동으로 호출
##=============================================
## 예제 
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science


students = [Student("홍길동", 90, 87, 92, 88),
            Student("가나다", 100, 84, 89, 95)]

## 실행 


print('이름', '총점', '평균', sep='\t') #마지막 것이 없으면 쭉 붙어서 출력됨



#이름	총점	평균
#홍길동	357	89.25
#가나다	368	92.0

## __이름__() 함수: 특수한 상황에 자동으로 호출 ===================
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science



students = [Student("홍길동", 90, 87, 92, 88),
            Student("가나다", 100, 84, 89, 95)] #객체 


print('이름', '총점', '평균', sep='\t') #마지막 것이 없으면 쭉 붙어서 출력됨 


## 클래스 변수 =======================================================
class Student:
    count = 0 # 클래스 변수 
    
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정:=> 호출시  클래스이름.변수이름 사용
        


students = [Student("홍길동", 90, 87, 92, 88),
            Student("가나다", 100, 84, 89, 95)] #객체


              

## 클래스메서드(클래스함수) ====================================================
# @classmethod : 데코레이터(Decorator)
# class 클래스 이름:
#     @classmethod
#     def 클래스함수(cls, 매개변수);
#           pass
# => 호출시: 클래스이름.함수이름(매개변수)

class Student:

    # 클래스 변수 


    # 클래스 메서드/함수


    # 인스턴스 메서드/함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science



# 학생추가 
Student("홍길동", 90, 87, 92, 88)
Student("가나다", 100, 84, 89, 95)

Student.print()


## Staticmethod(정적메서드) ======================================================
#인스턴스 메서드가 객체의 인스턴스 필드를 self를 통해 엑세스할 수 있는 반면,
#정적 메서드는 이러한 self 파라미터를 갖지 않고 인스턴스 변수에 엑세스할 수 없다.
#따라서, 정적 메서드는 보통 객체 필드와 독립적이지만 로직상 클래스내에 포함되는 메서드에 사용된다.
#정적 메서드는 메서드 앞에 @staticmethod 라는 Decorator를 표시하여 해당 메서드가 정적 메서드임을 표시
#==================================================================================

class Rectangle:
    count = 0  # 클래스 변수
 
    def __init__(self, width, height):

 
    # 인스턴스 메서드/함수

 
    # 정적 메서드/함수

  

    # 클래스 메서드/함수


 
 
# 테스트


