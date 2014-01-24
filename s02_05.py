import re
if __name__ == '__main__':
    p = re.compile('@\w+')
    template = '<a href="https://twitter.com/#!/{0}">{1}</a>'
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            m = p.match(line)
            if m:
                print(template.format( m.group()[1:], m.group() ))

