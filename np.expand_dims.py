import numpy as np
M = np.random.random((2, 3))
print("M: \n",M)
'''
array([[0.62376592, 0.17889671, 0.50143906],
       [0.64231837, 0.78843402, 0.42869213]])
       '''
N = np.expand_dims(M, axis=0)
print("\nN = np.expand_dims(M, axis=0): \n", N)
'''
array([[[0.62376592, 0.17889671, 0.50143906],
        [0.64231837, 0.78843402, 0.42869213]]])
        '''
print("\nM.shape: {}\nN.shape: {}".format(M.shape,N.shape))
'''(2, 3)
(1, 2, 3)
'''

P = np.expand_dims(M,axis=1)
print("\nP = np.expand_dims(M,axis=1):\n",P)
'''
array([[[0.62376592, 0.17889671, 0.50143906]],

       [[0.64231837, 0.78843402, 0.42869213]]])
       '''
print("\nM.shape: {}\nN.shape: {}\nP.shape: {}".format(M.shape,N.shape,P.shape))
'''
(2, 3)
(1, 2, 3)
(2, 1, 3)
'''
Q = np.expand_dims(M,axis=2)
print("\nQ = np.expand_dims(M,axis=2):\n",Q)
'''
array([[[0.62376592],
        [0.17889671],
        [0.50143906]],

       [[0.64231837],
        [0.78843402],
        [0.42869213]]])
        '''
print("\nM.shape: {}\nN.shape: {}\nP.shape: {}\nQ.shape: {}".format(M.shape,N.shape,P.shape,Q.shape))
'''
(2, 3)
(1, 2, 3)
(2, 1, 3)
(2, 3, 1)
'''


