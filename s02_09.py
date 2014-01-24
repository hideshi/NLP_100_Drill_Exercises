import re
if __name__ == '__main__':
    p1 = re.compile('[0-9]{3}-[0-9]{4}')
    p2 = re.compile('[一-龠]{2}(都|道|府|県)')
    p3 = re.compile('([^都道府県])+(市|区|郡|町|村)')
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            m1 = p1.search(line)
            m2 = p2.search(line)
            m3 = p3.search(line)
            if m1 and m2 and m3:
                print(m1.group(), m2.group(), m3.group())
