def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Перебираем каждое слово в other_words
    for word in other_words:
        # Проверяем, содержится ли root_word в word или наоборот
        if root_word in word or word in root_word:
            # Если условие выполняется, добавляем слово в список same_words
            same_words.append(word)

    # Возвращаем сформированный список
    return same_words


# Пример вызова функции и вывод результата
result = single_root_words("cat", "catalog", "dog", "caterpillar", "scatter", "bat")
print(result)