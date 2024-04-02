import matplotlib.pyplot as plt
import numpy as np

# 以下は　[10, 11, 12, 13, 14, 15, 16, 17, 18, 19] と同じ
time:list[int] = [i for i in range(10,20)]

# 以下は適当な指数関数にtimeを代入したもの
OD600:list[float] = [np.exp(i*0.12) for i in time]


fig = plt.figure(figsize=[5,5])
plt.scatter(time, OD600,s=30, c='tab:blue', marker='o', label='sample1')
plt.xlabel("time(h)")
plt.ylabel("OD600(-)")
plt.grid()
plt.legend()

fig.savefig("OD600.png", dpi=600)
