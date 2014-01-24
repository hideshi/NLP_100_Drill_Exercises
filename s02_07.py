import re
if __name__ == '__main__':
    p = re.compile('([一-龠]{1,}|[ぁ-ん]{2,}|[ァ-ヴ]{2,})(さん|ちゃん|くん|さま|どの|君|様|殿|氏)')
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            m = p.search(line)
            if m:
                print(m.group())
