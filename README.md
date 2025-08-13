# Needleman-Wunsch Algorithm
The first file is a Needleman-Wunsch algorithm with affine gap penalty\n
This algorithm is about alignment of two words. As a biologist, I consider words that consist of four letters: A, T, G and C (and sometimes U :)
In this script I use DNAFull matrix of match/mismatch (that means if letters are similar, we add points, and if not, we
take away points, like if we have A-A pair -- +5, if A-G -- -4).
Also if words have different length, we need to insert gaps - spaces between letters. It looks like A-TG, where '-' is gap.
Here I use an affine gap penalty, which means that gap open costs more, than gap extend.
So, this cute algorithm align two words this way:
CTCGA
CT--A
The score in this example = 4.5
You are welcome!
