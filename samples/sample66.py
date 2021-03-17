# https://www.runoob.com/python/python-exercise-example66.html
# 题目：
# 输入3个数a,b,c，按大小顺序输出。　　　
# 程序分析：
# 无。
from distlib.compat import raw_input


def fun():
    # python raw_input()# 用来获取控制台的输入。
    # raw_input() # 将所有输入作为字符串看待，返回字符串类型。
    num1 = raw_input("请输入数字1:")
    num2 = raw_input("请输入数字2:")
    num3 = raw_input("请输入数字3:")

    try:
        data = []
        if int(num1) and int(num2) and int(num3):
            data.append(num1)
            data.append(num2)
            data.append(num3)
            data.sort(reverse=True)
    except Exception as e:
        print(e)
        print("您的输入有误，请重新输入!!!")
        return
    finally:
        return data


if __name__ == "__main__":
    print(fun())
