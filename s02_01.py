if __name__ == '__main__':
    with open('tweet.txt', 'r') as f:
        lines = [line for line in f if '拡散希望' in line]
        for line in lines:
            print(line)
            
