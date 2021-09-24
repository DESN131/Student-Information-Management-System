import os
import numpy as np
import matplotlib.pyplot as plt

filename = "student.txt"


def main():
    while 1:
        menu()
        choice = input("")
        try:
            choice = int(choice)
        except ValueError:
            continue
        if choice in [0, 1, 2, 3, 4, 5, 6]:
            if choice == 0:
                ans = input("是否确定退出系统？y/n\n")
                if ans == "y":
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                show()
            elif choice == 3:
                search()
            elif choice == 4:
                delete()
            elif choice == 5:
                modify()
            elif choice == 6:
                total()
        else:
            print("输入错误，请重新输入")
            continue


def insert():
    student_list = []
    while 1:
        name = input("请输入学生姓名：")
        if not name:
            break
        try:
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
        except:
            print("数据有误，请重新输入")
            continue
        student = {"name": name, "chinese": chinese, "math": math, "english": english}
        student_list.append(student)
        answer = input("是否要继续添加？y/n\n")
        if answer == "y":
            continue
        else:
            break
    save(student_list)
    print("信息已保存")


def save(lst):
    try:
        stu_txt = open(filename, "a", encoding="utf-8")
    except:
        stu_txt = open(filename, "w", encoding="utf-8")
    for item in lst:
        stu_txt.write(str(item) + "\n")
    stu_txt.close()


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as rfile:
            students = rfile.readlines()
            for item in students:
                d = dict(eval(item))
                name = d["name"]
                chinese = d["chinese"]
                math = d["math"]
                english = d["english"]
                tot = chinese + math + english
                print(f"姓名：{name}， 语文成绩：{chinese}， 数学成绩：{math}， 英语成绩：{english}， 总成绩：{tot}")
    else:
        print("无学生信息，请先录入")


def search():
    student_query = []
    while 1:
        name = ""
        if os.path.exists(filename):
            name = input("请输入想要查找学生的姓名：")
            with open(filename, "r", encoding="utf-8") as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if name != "":
                        if d["name"] == name:
                            student_query.append(d)
            if student_query == []:
                print("未找到学生信息\n")
                return
            show_student(student_query)
            student_query.clear()
            answer = input("是否要继续查询？y/n\n")
            if answer == "y":
                continue
            else:
                break
        else:
            print("无学生信息，请先录入")
            return


def show_student(lst):
    lst = str(lst)
    lst = lst[1: -1]
    dic = {}
    dic = dict(eval(lst))
    if len(lst) == 0:
        print("未查询到学生信息")
        return
    else:
        name = dic["name"]
        chinese = dic["chinese"]
        math = dic["math"]
        english = dic["english"]
        tot = chinese + math + english
        print(f"学生姓名为: {name}")
        print(f"语文成绩为: {chinese}")
        print(f"数学成绩为: {math}")
        print(f"英语成绩为: {english}")
        print(f"总成绩为: {tot}")


def delete():
    while 1:
        name = input("请输入想要删除的学生的姓名:")
        if name != "":
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, "w", encoding="utf-8") as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d["name"] != name:
                            wfile.write(str(d) + "\n")
                        else:
                            flag = True
                    if flag == 1:
                        print(f"姓名为{name}的学生信息已删除")
                    else:
                        print(f"未找到姓名为{name}的学生信息")
            else:
                print("无学生信息")
                break
            show()
            answer = input("是否要继续删除？y/n\n")
            if answer == "y":
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as rfile:
            student_old = rfile.readlines()
    else:
        print("无学生信息文件，请先录入学生信息")
        return
    student_id = input("请输入想要修改的学生姓名：")
    with open(filename, "w", encoding="utf-8") as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d["name"] == student_id:
                print("已找到学生信息，请修改")
                while 1:
                    try:
                        d["name"] = input("请输入姓名:")
                        d["chinese"] = int(input("请输入语文成绩:"))
                        d["math"] = int(input("请输入数学成绩:"))
                        d["english"] = int(input("请输入英语成绩:"))
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                wfile.write(str(d) + "\n")
                print("修改成功")
            else:
                wfile.write(str(d) + "\n")
    answer = input("是否要继续修改？y/n\n")
    if answer == "y":
        modify()


def total():
    mode = input("请输入想要查询的科目：\n1. 语文\n2. 数学\n3. 英语\n4. 总成绩\n")
    lst_c = []
    lst_m = []
    lst_e = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as rfile:
            students = rfile.readlines()
            for item in students:
                d = dict(eval(item))
                lst_c.append(d["chinese"])
                lst_m.append(d["math"])
                lst_e.append(d["english"])
        lstc = np.array(lst_c)
        lstm = np.array(lst_m)
        lste = np.array(lst_e)
        lstt = lstc + lstm + lste
        if mode == "1":
            plt.rcParams['font.sans-serif'] = 'SimHei'
            plt.xlabel("语文分数")
            plt.ylabel("人数")
            plt.title("语文分数统计直方图")
            plt.hist(lstc, bins=10, color='steelblue', density=0, edgecolor='black', histtype='bar', alpha=0.8, range=((0, 100)))
            plt.show()
        elif mode == "2":
            plt.rcParams['font.sans-serif'] = 'SimHei'
            plt.xlabel("数学分数")
            plt.ylabel("人数")
            plt.title("数学分数统计直方图")
            plt.hist(lstm, bins=10, color='steelblue', density=0, edgecolor='black', histtype='bar', alpha=0.8, range=((0, 100)))
            plt.show()
        elif mode == "3":
            plt.rcParams['font.sans-serif'] = 'SimHei'
            plt.xlabel("英语分数")
            plt.ylabel("人数")
            plt.title("英语分数统计直方图")
            plt.hist(lste, bins=10, color='steelblue', density=0, edgecolor='black', histtype='bar', alpha=0.8, range=((0, 100)))
            plt.show()
        elif mode == "4":
            plt.rcParams['font.sans-serif'] = 'SimHei'
            plt.xlabel("总成绩")
            plt.ylabel("人数")
            plt.title("总成绩统计直方图")
            plt.hist(lstt, bins=10, color='steelblue', density=0, edgecolor='black', histtype='bar', alpha=0.8, range=((0, 300)))
            plt.show()
    else:
        print("无学生信息，请先录入")


def menu():
    print("************************************************")
    print("欢迎使用【学生信息管理系统】")
    print("请选择你想要进行的操作")
    print("1. 新建学生信息")
    print("2. 显示全部信息")
    print("3. 查询学生信息")
    print("4. 删除学生信息")
    print("5. 修改学生信息")
    print("6. 全部成绩分析")
    print("0. 退出系统")
    print("**************************************************")


main()
