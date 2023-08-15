"""
    -> h: list[int]
    -> word: str

    Constrains
    -> 1 <= h[?] <= 7 where ? is an english letter
"""

def designer_pdf_viewer(h: list[int], word: str) -> int:
    word = word.lower() # convert the word to lowercase
    num_of_letter = [ord(letter) - 97 for letter in word] # 97 is the ascii code for 'a' letter 
    max_heigh_letter = [h[i] for i in num_of_letter] # get the tallest letter
    return max(max_heigh_letter) * len(word) # multiply the tallest letter by the length of the word


if __name__ == '__main__':
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = 'zaba'
    print(designer_pdf_viewer(h, word))
