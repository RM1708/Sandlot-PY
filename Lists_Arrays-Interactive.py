#(tensorflow) rm@ubuntu:~/Sandlot-PY$ python
#Python 3.6.5 |Anaconda, Inc.| (default, Apr 29 2018, 16:14:56) 
#[GCC 7.2.0] on linux
#Type "help: ", "copyright: ", "credits" or "license" for more information.
M_asList = [[1, 2, 3],
        [4,5,6],
        [7,8,9]]
print("\nM as list: ",M_asList)
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("M_asList[:]: ",M_asList[:])
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("M_asList[:][0]: ",M_asList[:][0])
#[1, 2, 3]
...
...
import numpy as np
M_asMatrix = np.asarray(M_asList)
print("\nM as array:\n: ",M_asMatrix)
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
print("M_asMatrix[:]: ",M_asMatrix[:])
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
print("\nn[:][0]: ",M_asMatrix[:][0])
#array([1, 2, 3])
print("\nn[:, 0]: ",M_asMatrix[:, 0])
#array([1, 4, 7])

print("array M_asMatrix as list: : ",M_asMatrix.tolist())
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("M_asMatrix[:, 0] as list:: ",M_asMatrix[:, 0].tolist())
#[1, 4, 7]

print("M_asMatrix[:,0] to list and then to array: ",np.asarray(M_asMatrix[:,0].tolist()))
#array([1, 4, 7])

print("M_asMatrix[:, 0].T: ",M_asMatrix[:, 0].T)
#array([1, 4, 7])
print("Shape of M_asMatrix[:, 0].T: ",(M_asMatrix[:, 0].T).shape)
print("Shape of M_asMatrix[:, 0]: ",(M_asMatrix[:, 0]).shape)
print("N Dim of M_asMatrix[:, 0]: ",(M_asMatrix[:, 0]).ndim)
#
print("\nnp.transpose(M_asMatrix):\n", np.transpose(M_asMatrix))
#array([[1, 4, 7],
#       [2, 5, 8],
#       [3, 6, 9]])
print("M_asMatrix[:, 0]: ",M_asMatrix[:, 0])
#array([1, 4, 7])
print("np.transpose(M_asMatrix[:, 0]): ",np.transpose(M_asMatrix[:, 0]))
#array([1, 4, 7])
print("M_asMatrix[:, 0].shape: ",M_asMatrix[:, 0].shape)
#(3,)
print("M_asMatrix[:, 0][0]: ",M_asMatrix[:, 0][0])
#1

print("M_asMatrix[:, 0].ndim: ",M_asMatrix[:, 0].ndim)
#1

m = M_asMatrix[:,0]
print("1st Element of each Row as Row Vector m: : ",m)
#array([1, 4, 7])
print("Shape m: : ",m.shape)
print("np.transpose(m):\n",np.transpose(m))
print("Shape np.transpose(m):",(np.transpose(m)).shape)
print("1st element of each row as Col Vector:\n",m.reshape(3,1))
#array([[1],
#       [4],
#       [7]])
print("\nM_asMatrix:\n",M_asMatrix)
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
print("M_asMatrix.shape: ",M_asMatrix.shape)
#(3, 3)
print("M_asMatrix.tolist(): ",M_asMatrix.tolist())
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            #>>> n.tolist().shape
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: 'list' object has no attribute 'shape'
print("len(M_asMatrix.tolist()): ",len(M_asMatrix.tolist()))
#3
print("len(M_asMatrix.tolist()[0]): ",len(M_asMatrix.tolist()[0]))
#3

print("\ntype(M_asMatrix.tolist()): ",type(M_asMatrix.tolist()))
#<class 'list'>

print("\ntype(M_asMatrix): ",type(M_asMatrix))
#<class 'numpy.ndarray'>
print("\ntype(type(M_asMatrix)): ",type(type(M_asMatrix)))
#<class 'type'>

            #print (type(n)[0])
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #TypeError: 'type' object is not subscriptable
            #>>> n.__type__
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: 'numpy.ndarray' object has no attribute '__type__'
            #>>> n.type
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: 'numpy.ndarray' object has no attribute 'type'
            #>>> n.name
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: 'numpy.ndarray' object has no attribute 'name'
            #>>> n.__type__()
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: 'numpy.ndarray' object has no attribute '__type__'
            #>>> n.type()
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: 'numpy.ndarray' object has no attribute 'type'
print("\ntype(M_asMatrix): ",type(M_asMatrix))
#<class 'numpy.ndarray'>
            #>>> type(n).name
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: type object 'numpy.ndarray' has no attribute 'name'
            #>>> type(n).name()
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: type object 'numpy.ndarray' has no attribute 'name'
print("str(type(M_asMatrix)): ",str(type(M_asMatrix)))
#"<class 'numpy.ndarray'>"
print("str(type(M_asMatrix))[0]: ",str(type(M_asMatrix))[0])
#'<'
print("str(type(M_asMatrix))[1]: ",str(type(M_asMatrix))[1])
#'c'
print("str(type(M_asMatrix)).split(): ",str(type(M_asMatrix)).split())
#['<class', "'numpy.ndarray'>"]
            #>>> (type(n)).split()
            #Traceback (most recent call last):
            #  File "<stdin>: ", line 1, in <module>
            #AttributeError: type object 'numpy.ndarray' has no attribute 'split'
print("\ntype(M_asList): ",type(M_asList))
#<class 'list'>

print("\t\nDONE: : ", __file__)
