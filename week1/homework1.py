print("한양은행 대출 상환금 계산 서비스에 오신걸 환영합니다.")
p = int(input("대출원금이 얼마인가요? (백만원이상 만)"))
y = int(input("상환기간은 몇 년인가요? (년 단위로)"))
r = float(input("이자율은 몇% 인가요? (0.0에서 100.0 사이 수만)"))
print("\n대출 상환금 내역을 알려드리겠습니다.")

print("대출원금:", p , "원")
print("연 이자율",r,"%로",y,"년 동안 매월 원리금 균등으로 상환")

r = (r*0.01)/12
y = y*12
d = int((p*r*(1+r)**y)/((1+r)**y-1))
print("매월",d,"원씩 지불하셔야 합니다.")
print("상환완료시까지 총 상환금액은",d*4*12,"원 입니다.");

print("\n저희 한양은행은 항상 여러분과 함께 합니다.\n또 들려주세요.")