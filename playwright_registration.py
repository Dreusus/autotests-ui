from playwright.sync_api import sync_playwright, Locator, expect


class Playwright:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
    timeout = 2000
    _s_email = '//input[@id=":r0:"]'
    _s_user_name = '//input[@id=":r1:"]'
    _s_password = '//input[@id=":r2:"]'
    _s_button_registration = 'registration-page-registration-button'
    _s_title_dashboard = 'dashboard-toolbar-title-text'

    def registration(self) -> None:
        self.page.goto(self.registration_url)
        self._fill_registration_form()
        self._click_registration_button()
        self._assert_title_text()

    def get_locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def get_locator_by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def close(self) -> None:
        self.browser.close()
        self.playwright.stop()

    def _fill_registration_form(self) -> None:
        self.get_locator(self._s_email).fill('user.name@gmail.com')
        self.get_locator(self._s_user_name).fill('username')
        self.get_locator(self._s_password).fill('password')

    def _click_registration_button(self) -> None:
        button = self.get_locator_by_test_id(self._s_button_registration)
        button.wait_for(state='visible', timeout=self.timeout)
        button.click()

    def _assert_title_text(self) -> None:
        title = self.get_locator_by_test_id(self._s_title_dashboard)
        expect(title).to_have_text('Dashboard')


if __name__ == "__main__":
    app = Playwright()
    try:
        app.registration()
    finally:
        app.close()
