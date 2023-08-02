def penult_word(message):
    words = message.split()
    return words[-3]

quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Чтобы понять рекурсию, нужно сперва понять рекурсию'

print(penult_word(quote_1))
print(penult_word(quote_2))
print(penult_word(quote_3))