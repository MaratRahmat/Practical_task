from random import random
d_mas=[[2, -3], [-1, 2]]
mas=[[0, 0] for i in range (0,100)]
EX=0; A=B=0; s=0;
p2=0.25
p1=random()
for i in range(100):
    if random()<p1:
        mas[i][0]=1
    else:
        mas[i][1]=1
    if random()<p2:
        mas[i][1]=0
    else:
        mas[i][0]=1
    if d_mas[mas[i][0]][mas[i][1]]>0:
        d_mas[mas[i][0]][mas[i][1]]+=1
    
        
for i in range(0, 100):
    if random()<p1:
        mas[i][0]=0
    else:
        mas[i][1]=1
    if random()<p2:
        mas[i][1]=0
    else:
        mas[i][0]=1
    if d_mas[mas[i][0]][mas[i][1]]>0:
        A+=d_mas[mas[i][0]][mas[i][1]]
    else:
        B+=d_mas[mas[i][0]][mas[i][1]]
sr_kv=0
for i in range(0,100):
    s+=(abs(d_mas[mas[i][0]][mas[i][1]])-(A-B)/100)**2
sr_kv=(s/99)**0.5
EX=d_mas[0][0]*p1*p2+d_mas[0][1]*(1-p2)*p1+d_mas[1][0]*(1-p1)*p2+d_mas[1][1]*(1-p1)*(1-p2)
D=4*p1*p2+9*p1*(1-p2)+1*(1-p1)*p2+4*(1-p1)*(1-p2)-(EX)**2

print("Вероятности", p1, p2)
print("Cчет игроков А и В:", A, B)
print("Среднее значение выигрыша", A/100, B/100)
print("Математическое ожидание", EX)
print("Среднее квадратическое отклонение", sr_kv)
print("Дисперсия", D)
print("Теоретическое среднее квадратичное отклонение", D**0.5)
