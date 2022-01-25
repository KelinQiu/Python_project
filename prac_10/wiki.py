import wikipedia

word = input("Enter a page title or phrase: ")
while word != '':
    try:
        page = wikipedia.page(word, auto_suggest=False)
        print(page.title)
        print(page.summary)
        word = input("Enter a page title or phrase: ")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e)
        word = input("Enter a page title or phrase: ")
    except wikipedia.exceptions.PageError as a:
        print(a)
        word = input("Enter a page title or phrase: ")
