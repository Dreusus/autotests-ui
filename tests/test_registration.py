from typing import Final

import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

EMAIL: Final[str] = 'user.name@gmail.com'
PASSWORD: Final[str] = 'password'
USERNAME: Final[str] = 'username'


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage) -> None:
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(username=USERNAME, password=PASSWORD, email=EMAIL)
    registration_page.registration_form.check_visible(username=USERNAME, password=PASSWORD, email=EMAIL)
    registration_page.click_registration_button()

    dashboard_page.toolbar_view_component.check_visible()
