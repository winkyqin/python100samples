# https://www.runoob.com/python/python-exercise-example1.html
# 题目：
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：
# 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。


def fun():
    data = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i == j or i == k or j == k:
                    continue
                else:
                    data.append(i * 100 + j * 10 + k)
    return data


if __name__ == "__main__":
    print(fun())
