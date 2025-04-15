import pytest

from typing import Final
from pages.login_page import LoginPage

EMAIL: Final[str] = 'user.name@gmail.com'
EMAIL_EMPTY: Final[str] = '  '
PASSWORD: Final[str] = 'password'
PASSWORD_EMPTY: Final[str] = '  '


@pytest.mark.parametrize('email, password',
                         [(EMAIL, PASSWORD), (EMAIL, PASSWORD_EMPTY), (EMAIL_EMPTY, PASSWORD)])
def test_wrong_email_or_password_authorization(login_page:LoginPage, email: str, password: str) -> None:
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.fill_login_form(email, password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
