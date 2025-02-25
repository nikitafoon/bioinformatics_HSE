{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fd728069-a2ca-4d55-a85a-66aa3b9dcd64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.5\n"
     ]
    }
   ],
   "source": [
    "seq1 = input('Enter the first sequence: ')\n",
    "seq2 = input('Enter the second sequence: ')\n",
    "\n",
    "n = len(seq1)\n",
    "m = len(seq2)\n",
    "\n",
    "s_matrix = [[0] * (m + 1) for _ in range(n + 1)] # Match/mismatch\n",
    "a_matrix = [[0] * (m + 1) for _ in range(n + 1)] # Move down\n",
    "b_matrix = [[0] * (m + 1) for _ in range(n + 1)] # Move forward\n",
    "\n",
    "def fill_s_matrix(seq1, seq2, d=-10, e=-0.5):\n",
    "\n",
    "    s_matrix[1][0] = d\n",
    "    for i in range(2, n + 1):\n",
    "        s_matrix[i][0] = d + (i - 1) * e\n",
    "\n",
    "    s_matrix[1][0] = d\n",
    "    for j in range(2, m + 1):\n",
    "        s_matrix[0][j] = d + (j - 1) * e\n",
    "\n",
    "    return s_matrix\n",
    "\n",
    "def fill_a_matrix(seq1, seq2, d=-10, e=-0.5):\n",
    "    for i in range(n + 1):\n",
    "        a_matrix[i][0] = d + (i - 1) * e\n",
    "\n",
    "    for j in range(m + 1):\n",
    "        a_matrix[0][j] = d + (j - 1) * e\n",
    "    return a_matrix\n",
    "\n",
    "def fill_b_matrix(seq1, seq2, d=-10, e=-0.5):\n",
    "    for i in range(n + 1):\n",
    "        b_matrix[i][0] = d + (i - 1) * e\n",
    "\n",
    "    for j in range(m + 1):\n",
    "        b_matrix[0][j] = d + (j - 1) * e\n",
    "    return b_matrix\n",
    "\n",
    "def needleman_wunsch(seq1, seq2):\n",
    "\n",
    "    '''\n",
    "    Let me introduce my interpretation of\n",
    "    Needleman-Wunsch algorithm with\n",
    "    affine gap penalty\n",
    "    '''\n",
    "\n",
    "    match = 5\n",
    "    mismatch = -4\n",
    "    d = -10\n",
    "    e = -0.5\n",
    "    \n",
    "    for i in range(1, n + 1):\n",
    "        for j in range(1, m + 1):\n",
    "            if seq1[i-1] == seq2[j-1]:\n",
    "                diagonal_move = s_matrix[i-1][j-1] + match\n",
    "            else:\n",
    "                diagonal_move = s_matrix[i-1][j-1] + mismatch\n",
    "\n",
    "            a_matrix[i][j] = max(a_matrix[i-1][j] + e, s_matrix[i-1][j] + d)\n",
    "            b_matrix[i][j] = max(b_matrix[i][j-1] + e, s_matrix[i][j-1] + d)\n",
    "            s_matrix[i][j] = max(diagonal_move, a_matrix[i][j], b_matrix[i][j])\n",
    "    \n",
    "    return s_matrix[n][m]\n",
    "\n",
    "fill_s_matrix(seq1, seq2)\n",
    "fill_a_matrix(seq1, seq2)\n",
    "fill_b_matrix(seq1, seq2)\n",
    "result = needleman_wunsch(seq1, seq2,)\n",
    "print(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Bf Study (bf_st)",
   "language": "python",
   "name": "bf_st"
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
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
