from sklearn import preprocessing
import numpy as np

x = np.array([
1416.6132699006055,
1555.2003874578882,
1416.1478257394485,
1474.4768855388616,
1425.5626974819013,
1446.3502334301163,
1294.7153483859015]

)




def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range
print(normalization(x))