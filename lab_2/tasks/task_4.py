def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    dict = {}
    for i in msg:
        dict[ord(i)] = 0
    for i in msg:
        k = 0
        k = dict[ord(i)] + 1
        dict[ord(i)] = k

    uniq_val = set(dict.values())
    if len(uniq_val) == 1:
        keys = dict.keys()
        char = chr(min(keys))
        out = (char, dict[ord(char)])
        print(out)
        return out
    else:
        max_val = max(uniq_val)
        sort_dict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
        char_list = []
        for i in sort_dict:
            if i[1] == max_val:
                char_list.append(i[0])
        out = (chr(min(char_list)), max_val)
        print(out)
        return out



if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)