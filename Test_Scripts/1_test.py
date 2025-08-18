from Utils.WebAppDriver import WebAppDriver

app = WebAppDriver("https://facebook.com")


def test_1():
    print("Hello")
    app.launch()
    print(app.get_element_by_text("Log in").text)
    print("Done")


def test_2():
    try:
        raise Exception("Fail test")
    except Exception as e:
        app.get_screenshot()
        app.close()

