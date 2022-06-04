from random import random

p1=0.5
p2=0.5
d_mas=[[2, -3], [-1, 2]]
mas_v=[[0, 0] for i in range (0,100)]
EX=0
a=b=0
s=0;
for i in range(0, 100):
    if random()<p1:
        mas_v[i][0]=0
    else:
        mas_v[i][1]=1
    if random()<p2:
        mas_v[i][1]=0
    else:
        mas_v[i][0]=1
    if d_mas[mas_v[i][0]][mas_v[i][1]]>0:
        a+=d_mas[mas_v[i][0]][mas_v[i][1]]
    else:
        b+=d_mas[mas_v[i][0]][mas_v[i][1]]
sr_kv=0
for i in range(0,100):
    s+=(abs(d_mas[mas_v[i][0]][mas_v[i][1]])-(a-b)/100)**2
sr_kv=(s/99)**0.5
EX=d_mas[0][0]*p1*p2+d_mas[0][1]*(1-p2)*p1+d_mas[1][0]*(1-p1)*p2+d_mas[1][1]*(1-p1)*(1-p2)
D=4*p1*p2+9*p1*(1-p2)+1*(1-p1)*p2+4*(1-p1)*(1-p2)-(EX)**2

print("Cчет игроков А и В:", a, b)
print("Среднее значение выигрыша", a/100, b/100)
print("Мат ожидание", EX)
print("Среднее квадратическое отклонение", sr_kv)
print("Дисперсия", D)
print("Теоретическое среднее квадратичное отклонение", D**0.5)
