from typing import Final

from playwright.sync_api import expect, Page
import pytest

EMAIL: Final[str] = 'user.name@gmail.com'
EMAIL_EMPTY: Final[str] = '  '
PASSWORD: Final[str] = 'password'
PASSWORD_EMPTY: Final[str] = '  '


@pytest.mark.parametrize('email, password',
                         [(EMAIL, PASSWORD), (EMAIL, PASSWORD_EMPTY), (EMAIL_EMPTY, PASSWORD)])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str) -> None:
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
