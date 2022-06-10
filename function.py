def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file =  open(test.txt, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)


countWordsFromFile()