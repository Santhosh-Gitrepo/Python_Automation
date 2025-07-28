from Utils.WebAppDriver import WebAppDriver


def test_1():
    print("Hello")
    app = WebAppDriver("https://facebook.com")
    app.launch()
    print(app.get_element_by_text("Log in").text)
    app.close()
    print("Done")


def test_2():
    raise Exception("Fail test")

