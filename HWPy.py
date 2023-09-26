##Task 34

def count_vowels(word):
    vowels = "AEIOUYaeiouy"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def check_rhythm(pooh_poem):
    phrases = pooh_poem.split()
    rhythm = None
    
    for phrase in phrases:
        words = phrase.split('-')
        syllable_count = count_vowels(''.join(words))
        
        if rhythm is None:
            rhythm = syllable_count
        elif syllable_count != rhythm:
            return "Пам парам"
    
    return "Парам пам-пам"

pooh_poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(pooh_poem)
print(result)

##Task 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            row.append(result)
        print(" ".join(map(str, row)))
