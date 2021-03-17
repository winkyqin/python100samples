# https://www.runoob.com/python/python-exercise-example7.html
# 题目：
# 将一个列表的数据复制到另一个列表中。
# 程序分析：
# 使用列表[:]。


def fun():
    # 数组切片的知识点
    l1 = [1, 2, 2, 23, 5]
    l2 = l1[:]
    return l2


if __name__ == "__main__":
    print(fun())
