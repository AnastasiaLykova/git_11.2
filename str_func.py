def string_upper(text):
    """Возвращает строку заглавными буквами"""
    return text.upper()


def string_title(text):
    """Делает заглавными первые буквы каждого слова в строке"""
    lst = text.split(" ")
    title_text = ""
    for word in lst:
        title_text += word.title() + " "
    return title_text
