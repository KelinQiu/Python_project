import wikipedia

word = input("Enter page title or search phrase: ")
while word != "":
    try:
        print(wikipedia.summary(word))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    page = wikipedia.page(word, auto_suggest=False)
    print(page.word)
    print(page.summary)
    print(page.url)

    word = input("Enter page title or search phrase: ")