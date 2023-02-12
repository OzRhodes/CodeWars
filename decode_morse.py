# decodes Morse Code using the codewars imported decoder

def decodeMorse(morse_sequence):
    words = []
    for morse_word in morse_sequence.split('   '):
        word = ''.join(MORSE_CODE.get(morse_ltr, '') for morse_ltr in morse_word.split(' '))
        if word:
            words.append(word)
    return ' '.join(words)
