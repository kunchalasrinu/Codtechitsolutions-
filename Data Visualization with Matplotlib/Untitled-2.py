{
 "cells": [
  {
   "cell_type": "raw",
   "id": "5c4cd50c-709b-446a-81d6-6bc7d833c598",
   "metadata": {},
   "source": [
    "                                Q-1, Write a Numpy Program to create an array of all Even integers from 30-70"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "223e5158-2543-4e0e-a7ec-4fed8f77d8f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "raw",
   "id": "a01ee49c-714d-4d3d-a89f-001d3ca03909",
   "metadata": {},
   "source": [
    "//np.arange(start,stop,step,dtype=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "580bc850-bcb4-4029-9af8-5a81dbf9dd06",
   "metadata": {},
   "outputs": [],
   "source": [
    "even_integers=np.arange(30,71,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6148643c-9363-4d56-bc89-872842718672",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70]\n"
     ]
    }
   ],
   "source": [
    "print(even_integers)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "b6a289e7-c077-4293-bfb3-c59af9514e91",
   "metadata": {},
   "source": [
    "                               Q-2, Write a NumPy program to generate an array of 15 random numbers from a standard normal\n",
    "                                     distribution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "910a2416-9551-4354-8a25-24fa6b7e4f35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1.59819553,  1.01465338, -0.63479162,  1.7191466 ,  0.84507713,\n",
       "        0.16690899, -0.90942397,  0.08226275, -0.48686864,  0.73216845,\n",
       "       -1.20117478,  0.87138883,  0.75733266,  0.12763408,  1.89695857])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.randn(15)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "2430722a-cd73-430c-b9e5-8b0079b11a59",
   "metadata": {},
   "source": [
    "                               Q-3, How to compute the cross-product of two matrices in NumPy?"
   ]
  },
  {
   "cell_type": "raw",
   "id": "628da01a-2644-49e1-b69e-689cf9e7526b",
   "metadata": {},
   "source": [
    "Syntax: numpy.cross(a, b, axisa=-1, axisb=-1, axisc=-1, axis=None)[\n",
    "\n",
    "Return: cross product of two (arrays of) vectors."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c0126338-7983-433c-956d-2994f358ef24",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix1=np.array([[15,16,17],[18,19,20]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e61693b1-f713-4bab-bdee-dce8bfdf73dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix2=np.array([[21,22,23],[24,25,26]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "59163b6c-5f82-44d2-9138-9b532285938a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-6, 12, -6],\n",
       "       [-6, 12, -6]])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.cross(matrix1,matrix2)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "7b491837-de8e-4972-aa12-50b1f7642954",
   "metadata": {},
   "source": [
    "                                Q-4, How to compute the determinant of an array using NumPy?"
   ]
  },
  {
   "cell_type": "raw",
   "id": "82e01978-9eaa-40e0-ae17-f6c466b224a9",
   "metadata": {},
   "source": [
    "Syntax=numpy.linalg.det(array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ac8f89f7-2d8d-406e-bd56-a3b0d55d1cd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "square_matrix=np.array([[1,2],[3,4]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "999901ea-c4c6-4580-b4ed-898a8f48d981",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-2.0000000000000004"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linalg.det(square_matrix)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "28f2fa73-c7d5-453a-a9f4-73ad68c6cd60",
   "metadata": {},
   "source": [
    "                                 Q-5, How to create a 3x3x3 array with random values using NumPy?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f3ba36af-0bc1-43fa-89c2-4866cc9c9e8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 1.10156133,  0.30665053, -0.196424  ],\n",
       "        [ 2.20276501,  0.14221521, -0.75577565],\n",
       "        [ 1.22131065, -0.29798711,  0.65711766]],\n",
       "\n",
       "       [[-0.83112735, -0.13867719, -1.1404511 ],\n",
       "        [-0.58476615, -1.25820176, -0.67225031],\n",
       "        [-0.75872208,  0.54578955,  1.2927712 ]],\n",
       "\n",
       "       [[-0.64997363,  0.49881877, -1.12578452],\n",
       "        [-0.76530294,  0.22371251,  0.83575492],\n",
       "        [-1.10061331,  0.05151549, -0.4304596 ]]])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.randn(3,3,3)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "885484e2-8107-43b2-be38-787bf94f4019",
   "metadata": {},
   "source": [
    "                                        Q-6, How to create a 5x5 array with random values and find the minimum and maximum values using\n",
    "                                        NumPy?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "7957a8a1-7470-4f55-8526-91a155eac0ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "rand_array=np.random.randn(5,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "138b3f47-3676-407c-be3a-bf98bf314e64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5x5 array with random values\n",
      "[[ 0.10497624 -1.84660824  0.71295604  0.49231324 -0.73721114]\n",
      " [-0.7255614   0.82023906 -1.09078425  1.39509311 -0.20707983]\n",
      " [ 2.02259329 -0.23980399 -0.42637968  0.27911145 -1.06849668]\n",
      " [ 2.34229306 -1.03252207  0.0708624  -0.4258266   1.20570946]\n",
      " [ 0.74631444 -0.6122599  -0.59213064  0.45312626  0.11676235]]\n"
     ]
    }
   ],
   "source": [
    "print(\"5x5 array with random values\")\n",
    "print(rand_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "d8f05b0f-3837-4699-a728-379d46dc674e",
   "metadata": {},
   "outputs": [],
   "source": [
    "min_rand_array=np.min(rand_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "39f16af7-597b-4ac0-95f3-591b8c2af04f",
   "metadata": {},
   "outputs": [],
   "source": [
    "max_rand_array=np.max(rand_array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d3ab3960-a566-488a-bbdf-9b5a43032888",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum value:\n",
      "-1.8466082408996083\n",
      "Maximum value:\n",
      "2.34229305539013\n"
     ]
    }
   ],
   "source": [
    "print(\"Minimum value:\")\n",
    "print(min_rand_array)\n",
    "print(\"Maximum value:\")\n",
    "print(max_rand_array)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "5dbe73e8-7fa6-4b86-88a5-c417e1a58873",
   "metadata": {},
   "source": [
    "                                        Q-7, How to compute the mean, standard deviation, and variance of a given array along the second axis in\n",
    "                                             NumPy?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "02723ca3-1dc2-45ec-8b9e-42d654f48a2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_array=np.array([[1,2,3],\n",
    "                       [4,5,6],\n",
    "                       [7,8,9]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "a2adaa7a-4210-4a4f-b613-e2f80fdfb1c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean=np.mean(sample_array,axis=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9bd8df17-a390-4fe8-a32c-02f5f0182f33",
   "metadata": {},
   "outputs": [],
   "source": [
    "variance=np.var(sample_array,axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a66a4e11-b3ef-4308-ae9b-af646a5e2a9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "sd=np.std(sample_array,axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "4a316685-663d-468a-84e0-8c8c1dd509eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean is [2. 5. 8.]\n",
      "variance is [0.66666667 0.66666667 0.66666667]\n",
      "Standard deviation [0.81649658 0.81649658 0.81649658]\n"
     ]
    }
   ],
   "source": [
    "print(\"Mean is\",mean)\n",
    "print(\"variance is\",variance)\n",
    "print(\"Standard deviation\",sd)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26fdcc6b-fed4-443c-932d-010494763e45",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}