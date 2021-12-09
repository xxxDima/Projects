import matplotlib.pyplot as plt
import random
import numpy as np


def orel_end_reshka():
    a, b, c = 10, 100, 1000
    orel = 0  # количество орлов
    num = 0
    reska = 0  # количество решка
    banka_orel = 0
    banka_reshka = 0
    m_banka = 1  # максимальная банка для решек
    reshka_bolshe_2 = 0
    banka2_reshka = 0
    m2_banka = 1  # максимальная банка для орлов
    num_orel = 0
    list_orel = []

    for i in a, b, c:
        while num < i:
            rand = random.randint(0, 1)  # 1 = орел, 2 = решка
            if rand == 1:
                num_orel += 1
                orel += 1
                banka_orel += 1
                banka_reshka = 0
                if banka2_reshka > m2_banka:
                    m2_banka = banka2_reshka
                else:
                    banka2_reshka = 0
            elif rand == 0:
                reska += 1
                banka_reshka += 1
                banka2_reshka += 1
                if banka_reshka >= 2:
                    reshka_bolshe_2 += 1
                if banka_orel > m_banka:
                    m_banka = banka_orel
                else:
                    banka_orel = 0
            if num % 10 == 0:
                list_orel.append(num_orel)
                num_orel = 0
            num += 1
        q = orel / i * 100

        print(f"{q}% с {i} раз выпал орел")
    print(m_banka, "exist orel one time")
    print(reshka_bolshe_2, "раз подряд выпадала решка")
    print("%d exist reshka one time" % m2_banka)
    # print(list_orel)

    plt.plot(list_orel)
    plt.show()


orel_end_reshka()
