from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.form_component = CreateCourseFormComponent(page)
        self.toolbar_view_component = CreateCourseToolbarViewComponent(page)
        self.exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

    def check_visible_create_course_button(self):
        expect(self.toolbar_view_component.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.toolbar_view_component.create_course_button).to_be_disabled()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(title='There is no exercises',
                                                description='Click on "Create exercise" button to create new exercise')
