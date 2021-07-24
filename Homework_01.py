# Ex 1
def kthTerm(n, k):
    return int(bin(k)[2:], n)


# Ex 2
def filterBible(scripture, book, chapter):
    return [
        book_id
        for book_id in scripture
        if book_id[0:2] == book and book_id[2:5] == chapter
    ]


# Ex 3
from collections import Counter

def isPalindrome(strng):
    unpaired_letters = sum(
        value % 2 
        for value in dict(Counter(strng)).values()
    )
    return unpaired_letters <= 1


#Ex 4
def findPermutation(n, p, q):
    return [1 + p.index(x) for x in q]



# Ex 6
def order(a):
    b = sorted(a)
    if a == b:
        return "ascending"
    if a == b[::-1]:
        return "descending"
    return "not sorted"


# Ex 7
def Cipher_Zeroes(N):
    number_of_zeros = {digit : 0 for digit in '123457'}
    number_of_zeros.update({digit : 1 for digit in '069'})
    number_of_zeros['8'] = 2
    
    M = sum(
        number_of_zeros[digit]
        for digit in N
    )
    
    if M == 0:
        return 0
    if M % 2:
        M += 1
    else:
        M -= 1
    return bin(M)[2:]


# Ex 8
def studying_hours(a):

    curr_len = 1
    max_len = 1
    
    for prev_day, curr_day in zip(a, a[1:]):
        if prev_day <= curr_day:
            curr_len += 1
            max_len = max((curr_len, max_len))
        else:
            curr_len = 1
            
    return max_len
