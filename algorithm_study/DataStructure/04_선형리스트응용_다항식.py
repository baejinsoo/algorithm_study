## 함수 선언부
def printPoly(p_x):
    term = len(p_x) -1 # 최고차항
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        coef = p_x[i] # coef : 계수

        if coef >= 0 :
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + " "
        term -= 1
    return polyStr


def calcPoly(xValue, p_x):
    term = len(p_x) - 1
    result = 0

    for i in range(len(p_x)):
        # for _ in range(term):
        #     p_x[i] *= xValue
        # result += p_x[i]
        result += p_x[i] * xValue ** term
        term -= 1

    return result


## 전역 변수부
px = [4, -3, 0, 2] # 4x^3 + 3x^2 + 0x^1 + 2x^0


## 메인 코드부
if __name__ == '__main__':
    result = printPoly(px)
    print(result)
    print(calcPoly(5, px))
