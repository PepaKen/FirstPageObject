from pages.auth_page import AuthPage


def test_auth_page_login(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys("pepatest@gmail.com")
    page.password.send_keys("12345")
    page.btn_success.click()

    assert page.get_current_url() != "https://petfriends1.herokuapp.com/login"



