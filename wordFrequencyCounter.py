import string

def count_word_frequency(file_path):
    word_freq = {}
    with open(file_path, 'r') as file:
        # reading in file
        content = file.read()
        # removing punctuation
        content = content.translate(str.maketrans('', '', string.punctuation)).lower()
        # splitting content into "words"
        words = content.split()
        # count freq of word
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq

def main():
    # test file path
    file_path =  ''
    word_frequency = count_word_frequency(file_path)
    for word, frequency in word_frequency.items():
        print(f'{word}: {frequency}')

if __name__ == '__main__':
    main()