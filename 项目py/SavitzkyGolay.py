import numpy as np
from scipy.signal import savgol_filter
def SavitzkyGolay(a):
    if len(a) == 0:
        print("输入数组为空，请输入二维数组")
        return
    y = np.zeros(shape=(len(a), len(a[0])))
    for i in range(len(a)):
        # 使用Savitzky-Golay 滤波器后得到平滑图线
        temp = savgol_filter(a[i], 25, 3, mode='nearest')
        y[i] = temp
    return y


