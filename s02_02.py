if __name__ == '__main__':
    with open('tweet.txt', 'r') as f:
        lines = [line for line in f if line.strip().endswith('なう')]
        for line in lines:
            print(line)
            
