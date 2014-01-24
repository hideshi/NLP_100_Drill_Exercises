if __name__ == '__main__':
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            index = line.find(' RT ')
            if index != -1:
                print(line[index + 4 :])
            
