from selene.support.shared import browser


def test_add_user():
    browser.element('#addNewRecordButton').click()
    browser.element("#firstName").type('Ash')
    browser.element("#lastName").type('Ash')
    browser.element("#userEmail").type('name@name.com')
    browser.element("#age").type("29")
    browser.element("#salary").type('300')
    browser.element("#department").type("club")
    browser.element("#submit").click()


def test_change_user_info():
    browser.element("#edit-record-2").click()
    browser.element("#firstName").clear().type("Ash")
    browser.element("#lastName").clear().type('Ash')
    browser.element("#userEmail").clear().type('name@name.com')
    browser.element("#age").clear().type("29")
    browser.element("#salary").clear().type('300')
    browser.element("#department").clear().type("club")
    browser.element("#submit").click()


def test_delete_user():
    browser.element("#delete-record-3")

