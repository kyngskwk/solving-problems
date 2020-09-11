_end =  '_end_'

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            if _end in current_dict:
                return False
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return True


def solution(phone_book):
    phone_book.sort()
    return make_trie(phone_book)

print(solution(['119', '97674223', '1195524421']))