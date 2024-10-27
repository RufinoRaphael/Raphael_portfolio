{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f5660211-d9d6-42a2-a20e-0cd1d83f5f58",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(x,y):\n",
    "    return x + y\n",
    "\n",
    "def subtract(x,y):\n",
    "    return x - y\n",
    "\n",
    "def multiply(x,y):\n",
    "    return x * y\n",
    "\n",
    "def divide(x,y):\n",
    "    return x / y\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0944beea-8bbd-4a8e-831b-3c57b8232fc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 'a' for addition\n",
      "Enter 's' for subtraction\n",
      "Enter 'm' for multiplication\n",
      "Enter 'd' for dividion\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter choice: (a, s, m, d):  d\n",
      "Enter first number:  50\n",
      "Enter second number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 50.0 / 2.0 =  25.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Want to do another calculation? (yes/no):  y\n",
      "Enter choice: (a, s, m, d):  a\n",
      "Enter first number:  2\n",
      "Enter second number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 2.0 + 2.0 =  4.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Want to do another calculation? (yes/no):  n\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter 'a' for addition\")\n",
    "print(\"Enter 's' for subtraction\")\n",
    "print(\"Enter 'm' for multiplication\")\n",
    "print(\"Enter 'd' for dividion\")\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "while True:\n",
    "    choice = input('Enter choice: (a, s, m, d): ')\n",
    "    if choice.lower() in ('a', 'add','addition','s','subtract','subtraction', 'm','multiply','multiplication', 'd', 'divide', 'division'):\n",
    "        num1 = float(input('Enter first number: '))\n",
    "        num2 = float(input('Enter second number: '))\n",
    "    \n",
    "        if choice.lower() in ('a', 'add','addition'):\n",
    "            print('Result: {} + {} = '.format(num1,num2),add(num1,num2))\n",
    "            \n",
    "        elif choice.lower() in ('s','subtract','subtraction'):\n",
    "            print('Result: {} - {} = '.format(num1,num2),subtract(num1,num2))\n",
    "    \n",
    "        elif choice.lower() in ('m','multiply','multiplication'):\n",
    "            print('Result: {} * {} = '.format(num1,num2),multiply(num1,num2))\n",
    "    \n",
    "        elif choice.lower() in ('d', 'divide', 'division'):\n",
    "            print('Result: {} / {} = '.format(num1,num2),divide(num1,num2))\n",
    "    \n",
    "    else:\n",
    "        print('Please input a correct choice')\n",
    "\n",
    "\n",
    "    next_calculation = input(\"Want to do another calculation? (yes/no): \")\n",
    "    if next_calculation.lower() in ['no', 'n', 'nope']:\n",
    "        break\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c5ec4bf-69c1-4de2-ac0f-6f34e91471dc",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
