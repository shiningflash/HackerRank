def reverse_word_and_swap_cases(sen):
    w = sen.split()
    w = list(reversed(w))
    ans = " ".join(w)
    return ans.swapcase()

if __name__ == "__main__":
    sen = input()
    sen = reverse_word_and_swap_cases(sen)
    print(sen)