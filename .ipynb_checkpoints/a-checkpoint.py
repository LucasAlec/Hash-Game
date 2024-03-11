{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6cc951f4-5060-4dca-8394-c0e0ad7c76cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "print([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ce8c33de-44ac-4d80-ad6c-1ad2facb7c8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n",
      "[4, 5, 6]\n",
      "[7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "print([1,2,3])\n",
    "print([4,5,6])\n",
    "print([7,8,9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ab5c7b06-4047-4e5d-8900-a78c7fcca660",
   "metadata": {},
   "outputs": [],
   "source": [
    "def display(row1,row2,row3):\n",
    "    print(row1)\n",
    "    print(row2)\n",
    "    print(row3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b5da7f26-7531-4e08-b8ec-960bb9526aa5",
   "metadata": {},
   "outputs": [],
   "source": [
    "row1 = [' ', ' ', ' ']\n",
    "row2 = [' ', ' ', ' ']\n",
    "row3 = [' ', ' ', ' ']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "04480a9c-ff1c-480c-988d-a4e0c348891d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[' ', ' ', ' ']\n",
      "[' ', ' ', ' ']\n",
      "[' ', ' ', ' ']\n"
     ]
    }
   ],
   "source": [
    "display(row1,row2,row3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b80ae4fd-9640-46a3-b29d-4ba08c321190",
   "metadata": {},
   "outputs": [],
   "source": [
    "row2[1] = 'X'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8adcc905-c043-4926-b34f-8eaec60fe89a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[' ', ' ', ' ']\n",
      "[' ', 'X', ' ']\n",
      "[' ', ' ', ' ']\n"
     ]
    }
   ],
   "source": [
    "display(row1,row2,row3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "aee82cf4-251b-487e-8ece-54735964a627",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a value:  2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input(\"Please enter a value: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cdd20785-3ed7-4cc6-9eeb-993f6bf50759",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter a value:  2\n"
     ]
    }
   ],
   "source": [
    "result = input(\"Please enter a value: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "5acb8e5b-ff2d-4ada-b4ec-da6cc683bf6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose an index position:  2\n"
     ]
    }
   ],
   "source": [
    "position_index = int(input(\"Choose an index position: \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "918ca4f6-e7a1-4898-8c84-93cb77edb815",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(position_index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "564dbdcc-9891-424c-9fa7-31cc78ab9721",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' '"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "row2[position_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d928e281-d153-46e1-8243-7c40bd5cc7ba",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
