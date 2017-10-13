print("------商家:0 用户:1------")
choice=input(">>>")
print("-------------------------")

def shangjia():
    while True:
        with open("product.txt") as f:
            a=f.read()
            b=a.split()
            c=[]
            for i in b:
               c.append(i.split(','))
            f.close()
        print('-----商品列表-----')
        for x in c:
            print(c.index(x)+1,x[0],x[1])
        print("-------选项-------")
        print("0 quit")
        print("x 修改价格")
        print("y 增加商品")
        choice1=input(">>>")
        if choice1 == "0":
            exit()
        elif choice1 == "x":
            while True:
                print("输入商品编号：")
                choice2=input(">>>")
                if choice2.isdigit():
                    choice2=int(choice2)
                    if choice2 <= len(c):
                        print("---- 选择商品：%s ----" % (c[choice2-1][0]))
                        jiage=input("输入修改后的价格>>>")
                        c[choice2-1][1]=jiage
                        jj=""
                        for y in c:
                            jj=jj+",".join(y)+" "
                        j=jj
                        with open('product.txt','w') as f1:
                            f1.write(j)
                            f1.close()
                        choice3=input("是否继续修改，yes or no >>>")
                        if choice3 == "yes":
                            continue
                        else:
                            break
                    else:
                        print("--> 编号错误,谢谢")
                        continue
                else:
                    print("--> 编号错误，谢谢")
                    continue
        elif choice1 == "y":
            while True:
                name=input("输入商品名：")
                price=input("输入商品价格：")
                p=" "+name+","+price
                with open("product.txt",'a') as f2:
                    f2.write(p)
                    f2.close()
                choice4=input("继续添加? yes or no >>>")
                if choice4 == "yes":
                    continue
                else:
                    break
        else:
            print("选择错误，谢谢")
            continue

def yonghu():
    username=input("输入用户名：")
    shangpin = []
    with open('user.txt') as f:
        a=f.read()
        b=eval(a)
        f.close()
    if b.get(username):
        salary=b[username]['salary']
    else:
        salary = input("输入您购物的金额：")
        if salary.isdigit():
            b[username]={'salary':salary,'product':[]}
            with open('user.txt', 'w') as f1:
                g = str(b)
                f1.write(g)
                f1.close()
        elif int(salary) < 0 :
            print("输入正确的金额!")
        else:
            print("输入正确的金额")
    print("欢迎您，%s" % username)
    print("您的余额是,%s" % b[username]['salary'])
    if len(b[username]['product'])!= 0:
        print("您已购得以下商品：")
        print("-----------------")
        for xx in b[username]['product']:
            print(xx)
        print("-----------------")


    with open("product.txt") as f2:
        p1=f2.read()
        p2=p1.split()
        p3=[]
        for i in p2:
           p3.append(i.split(','))
        f2.close()

    while True:
        print("------商品列表------")
        for pp in p3:
            print(p3.index(pp)+1,pp[0],pp[1])
        print("-------------------")
        print("-------选项-------")
        print("0 quit")
        print("1 shopping")
        choice=input(">>>")
        if choice == "0":
            exit()
        elif choice == "1":
            salary=int(salary)
            while True:
                bianhao=input("输入商品编号：")
                if bianhao.isdigit():
                    bianhao=int(bianhao)
                    if bianhao <= len(p3):
                        jiage=int(p3[bianhao-1][1])
                        if salary >= jiage:
                            salary=salary-jiage
                            print("%s,购买成功! 余额：%s" %(p3[bianhao-1][0],salary))
                            shangpin.append(p3[bianhao-1][0])
                        else:
                            print("您的余额已不足，谢谢！")
                    choice1=input("继续购买？yes or no >>>")
                    if choice1 == "yes":
                        continue
                    else:
                        print("本次购得：%s" % ",".join(shangpin))
                        for zz in shangpin:
                            b[username]['product'].append(zz)
                        b[username]['salary']=salary
                        e=str(b)
                        with open('user.txt','w') as f3:
                            f3.write(e)
                            f3.close()
                        break
                else:
                    print("商品编号错误！")
                    continue
            else:
                print("商品编号错误！")
                continue
        else:
            print("选项错误，谢谢")
            continue



if choice == "0":
    shangjia()
elif choice == "1":
    yonghu()
else:
    print("选项错误，谢谢")

