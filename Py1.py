
print("請輸入方程式：")
q=input()
if "+" in q :
    q1 = q.split("+")
elif "-" in q:
    q1 = q.split("-") 
elif "*" in q:
    q1 = q.split("*") 
elif "xy" in q:
    q = q.replace("xy","x1*1y") 
    q1 = q.split("*") 
qx=q1[0].split("x")
print("請輸入X值：")
inx = int(input())
ax = int(qx[0]) * inx ** int(qx[1])
qy=q1[1].split("y")
print("請輸入Y值：")
iny = int(input())

ay = int(qy[0]) * iny ** int(qy[1])
if "+" in q :
    fa=ax+ay
elif "-" in q:
    fa=ax-ay
elif "*" in q:
    fa=ax*ay 
print("答案是：" + str(fa))
