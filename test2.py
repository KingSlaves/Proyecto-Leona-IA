from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np

y = [(True, False), 
    (True, True), 
    (False, False), 
    (False, False), 
    (True, False)]

one_hot = MultiLabelBinarizer()

hp = one_hot.fit_transform(y)

print(hp)
print(y)