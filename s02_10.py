import re
if __name__ == '__main__':
    #p = re.compile('[^一-龠ぁ-んァ-ヴ々ーＡ-Ｚａ-ｚ０-９A-Za-z0-9\w_]+')
    p = re.compile('[\W]+')
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            m = p.search(line)
            if m:
                print(m.group())
