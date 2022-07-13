def read_file(_):
    data = []
    count = 0
    with open(_, 'r') as f:
        for _ in f:
            data.append(_)
            count += 1
            if count % 10000 == 0:
                print(len(data))
    print('檔案讀取完畢，共有 {0} 筆資料'.format(len(data)))
    return data


def word_len(data):
    sum_len = 0
    for _ in data:
        sum_len += len(_)
    print('每筆留言平均長度為 {0} 個字元'.format(sum_len / len(data)))
    return data


def word_len_2(data):
    new = [_ for _ in data if len(_) < 100]
    print('一共有 {0} 筆留言長度小於100個字元'.format(len(new)))
    return data


def word_len_3(data):
    good = [_ for _ in data if 'good' in _]
    print('一共有 {0} 筆留言包含good'.format(len(good)))
    return data


def digit_count(data):
    wc = {}
    for _ in data:
        words = _.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1
    return wc


def print_digit_count(wc):
    for word in wc:
        if wc[word] > 1000000:
            print(word, wc[word])
    print(len(wc))


def inquire(wc):
    while True:
        key = input('請問您想查什麼字: ')
        if key == 'q':
            print('感謝您的使用')
            break
        elif key in wc:
            print('{0} 出現過的次數為 {1}'.format(key, wc[key]))
        else:
            print('留言內沒有出現過')


def main(_):
    data = []
    wc = {}
    data = read_file(_)
    word_len(data)
    word_len_2(data)
    word_len_3(data)
    wc = digit_count(data)
    print_digit_count(wc)
    inquire(wc)


if __name__ == '__main__':
    main('reviews.txt')
