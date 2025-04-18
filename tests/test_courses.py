# from pathlib import Path

from playwright.sync_api import expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page) -> None:
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_toolbar_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar_title).to_have_text('Courses')

    courses_svg = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_svg).to_be_visible()

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title).to_have_text('There is no results')

    courses_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage,courses_list_page: CoursesListPage) -> None:
    ccp = create_course_page
    clp = courses_list_page

    ccp.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    ccp.check_visible_create_course_title()
    ccp.check_disabled_create_course_button()
    ccp.check_visible_image_preview_empty_view()
    ccp.check_visible_image_upload_view()
    ccp.check_visible_create_course_form(title='',description='',estimated_time='',
                                         max_score='0',min_score='0')
    ccp.check_visible_exercises_title()
    ccp.check_visible_create_exercise_button()
    ccp.check_visible_exercises_empty_view()

    # file = Path(__file__).parent.parent / 'testdata' / 'files' / 'image.png'
    file = './testdata/files/image.png'
    ccp.upload_preview_image(file=file)
    ccp.check_visible_image_upload_view(is_image_uploaded=True)

    ccp.fill_create_course_form(title = 'Playwright',estimated_time = '2 weeks',description =
    'Playwright',max_score = '100',min_score = '10')
    ccp.click_create_course_button()

    clp.check_visible_courses_title()
    clp.check_visible_create_course_button()
    clp.check_visible_course_card(index=0,title = 'Playwright',estimated_time = '2 weeks',max_score = '100',min_score = '10')