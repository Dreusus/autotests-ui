from typing import Final

EMAIL: Final[str] = 'user.name@gmail.com'
PASSWORD: Final[str] = 'password'
USERNAME: Final[str] = 'username'

def test_successful_registration(registration_page,dashboard_page) -> None:
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(username=USERNAME, password=PASSWORD, email=EMAIL)
    registration_page.click_registration_button()

    dashboard_page.check_dashboard_title_text()