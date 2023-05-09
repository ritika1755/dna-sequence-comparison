import tkinter as tk
from functools import partial

def find_lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    lcs_matrix = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs_matrix[i][j] = 0
            elif seq1[i-1] == seq2[j-1]:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1]+1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
    
    lcs_result = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            lcs_result = seq1[i-1] + lcs_result
            i -= 1
            j -= 1
        elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return lcs_result

def find_lis(seq):
    n = len(seq)
    lis_lengths = [1]*n

    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j] and lis_lengths[j]+1 > lis_lengths[i]:
                lis_lengths[i] = lis_lengths[j]+1
    
    max_length = max(lis_lengths)
    lis_result = ""
    for i in range(n-1, -1, -1):
        if lis_lengths[i] == max_length:
            lis_result = seq[i] + lis_result
            max_length -= 1

    return lis_result

def compare_seqs(seq1_entry, seq2_entry, result_label):
    seq1 = seq1_entry.get().upper()
    seq2 = seq2_entry.get().upper()
    lcs_result = find_lcs(seq1, seq2)
    lis_result = find_lis(lcs_result)
    result_label.config(text="Matching DNA sequence(LCS): {}\nLongest sequence in order(LIS): {}".format(lcs_result, lis_result))

def create_gui():
    root = tk.Tk()
    root.title("DNA Sequence Comparison")
    root.geometry("500x500")

    # Load image
    image = tk.PhotoImage(file="dna1.png")

    # Set background image
    bg_label = tk.Label(root, image=image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Set transparent input boxes
    seq1_entry = tk.Entry(root, bg="white", fg="black", highlightthickness=0, borderwidth=1)
    seq1_entry.place(x=200, y=150)
    seq2_entry = tk.Entry(root, bg="white", fg="black", highlightthickness=0, borderwidth=1)
    seq2_entry.place(x=200, y=200)

    seq1_label = tk.Label(root, text="Sequence 1:", bg="white", fg="black")
    seq1_label.place(x=100, y=150)
    seq2_label = tk.Label(root, text="Sequence 2:", bg="white", fg="black")
    seq2_label.place(x=100, y=200)

    result_label = tk.Label(root, text="", bg="white", fg="black")
    result_label.place(x=100, y=280)

    # Set transparent button
    compare_button = tk.Button(root, text="Compare", command=partial(compare_seqs, seq1_entry, seq2_entry, result_label),
                               bg="white", highlightthickness=0, borderwidth=1)
    compare_button.place(x=200, y=250)

    root.mainloop()





if __name__ == '__main__':
    create_gui()