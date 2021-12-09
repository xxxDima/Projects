import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import numpy as np
from matplotlib.ticker import NullLocator
import matplotlib.ticker as ticker

x = np.array(
    ['2021-11-12', '2021-11-13', '2021-11-14',
     '2021-11-15', '2021-11-16', '2021-11-17',
     '2021-11-18', '2021-11-19'])
y = np.array([2.8012, 2.8043, 2.8043, 2.8043, 2.8144, 2.8056, 2.8063, 2.817])
y_usd = np.array([2.4428, 2.4511, 2.4511, 2.4511, 2.4595, 2.4679, 2.4848, 2.486])


# fig, axes = plt.subplots(nrows=2, ncols=1)
# fig.tight_layout() # Or equivalently,  "plt.tight_layout()"

plt.show()

eur = plt.subplot(211)
plt.plot(x, y)
plt.legend(['eurFirst series'])
# eur.figure.set_constrained_layout_pads(w_pad=4 / 72, h_pad=4 / 72, hspace=0, wspace=0)
# eur.figure.set_constrained_layout_pads.figure.subplot.hspace(25)
plt.subplots_adjust(hspace=0.5)


usd = plt.subplot(212)
plt.plot(x, y_usd, 'r', linewidth=3)
plt.legend(['usd2 First series'])


usd.tick_params(pad = 1,    #  Расстояние между черточкой и ее подписью
               labelsize = 7,    #  Размер подписи
               labelcolor = 'r',    #  Цвет подписи
               labelrotation = 45)    #  Поворот подписей





plt.title('1111111')
plt.figtext('2', '2', '77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777jhvh')
plt.suptitle('Курсы валют EUR и USD по отношению к BYN')


# eur.xaxis.set_major_locator(NullLocator())
#eur.yaxis.set_major_locator(LinearLocator(7))


eur.grid()
plt.xlabel('2222222222222')
usd.grid()




plt.show()



# yy = [2.8043, 2.3, 2.9, 4.5, 2.3, 3.2, 1.6]
# print(len(x), len(y))
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot()
# ax.plot(yy)
# ax.set(xlim=(-1, 7), ylim=(-3, 9))
# ax.yaxis.set_major_locator(LinearLocator(3))
#
# #plt.plot(x, y, yy)
# plt.grid()



