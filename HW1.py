Q =  input("請輸入方程式：")
Qx = input("請輸入X值：")
Qy = input("請輸入Y值：")

if "+" in Q :
    Q1 = Q.split("+")
    Q2="+"
elif "-" in Q:
    Q2="-"
    Q1 = Q.split("-")
elif "*" in Q:
    Q2="*"
    Q1 = Q.split("*")  
elif "/" in Q:
    Q1 = Q.split("/")
    Q2="/"
elif "xy" in Q:
    Q1= Q.replace("xy","x*y")
    Q1 = Q1.split("*")  
    Q2="*"
qx1=Q1[0].split("x")[0]
qx2=Q1[0].split("x")[1]
qy1=Q1[1].split("y")[0]
qy2=Q1[1].split("y")[1]
if qx1=="":
    qx1=1   
if qx2=="":
    qx2=1 
if qy1=="":
    qy1=1   
if qy2=="":
    qy2=1  
ans = str(qx1)+str(Qx)+"*"+str(qx2)+"^"+str(qy1)+ str(Qy)+"*"+str(qy2)+"^"+str(Q2)
print (ans)
