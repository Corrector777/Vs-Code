def truncate(text, number_of_char):
    return f'{text[: number_of_char]}...'
    

print(truncate('transilvaynia', 4))