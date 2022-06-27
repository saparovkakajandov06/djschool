from dateutil.parser import parse
import pytest
import re

from tests.factories import calculate_price, get_maximum_price


"""
    https://habr.com/ru/company/yandex/blog/242795/
    
    PyTest
        https://habr.com/ru/post/269759/
    
    Как работает yield
        https://habr.com/ru/post/132554/
"""


def is_date(string, fuzzy=False):
    """Check if string is valid date"""

    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


@pytest.mark.django_db
class TestCoreModels:

    def test_user_str(self, user):
        """Test User::__str__ function"""

        assert user.__str__() == user.username

    def test_user_is_superuser(self, superuser):
        """Test User::__str__ function"""

        assert superuser.is_superuser

    def test_branch_str(self, branch):
        """Test Branch::__str__ function"""

        assert branch.__str__() == "Berkarar"

    def test_group_str(self, group):
        """Test ProductSpecification::__str__ function"""

        assert group.name != ''

    def test_employee(self, employee):
        """Test several Employee's fields"""

        assert employee.gender == 1
        assert 0 <= employee.job_internship_total <= 20
        assert 0 <= employee.job_internship <= 5
        assert employee.working_hour in range(1, 41)
        assert len(employee.address) <= 100

        assert employee.account_fk.id > 0
        assert employee.branch_fk.all().count() > 0

    def test_student(self, student):
        """Test several Student's fields"""

        assert student.gender == 1
        assert student.nationality == 'azerian'
        assert student.school == 'Middle School #29'
        assert re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", student.email)
        assert len(student.address) <= 100

    def test_relative(self, relative):
        """Test several Relative's fields"""

        assert relative.title == 'Mom'
        assert len(relative.surname) <= 32
        assert len(relative.name) <= 32
        assert len(relative.phone) <= 15
        assert relative.occupation == 'Student'
        assert relative.__str__() == '{0} {1} ({2})'.format(relative.surname, relative.name, relative.phone)

    def test_season(self, season):
        """Test several Season's fields"""

        assert season.name == 'Summer'
        assert season.active
        assert is_date(season.start_date)
        assert is_date(season.end_date)

    def test_room(self, room):
        """Test several Room's fields"""

        assert room.name == 'ENG-1'
        assert room.branch_fk.id > 0

    def test_subject(self, subject):
        """Test several Subject's fields"""

        assert subject.name == 'English'

    def test_course(self, course):
        """Test several Course's fields"""

        assert course.name == 'Intermediate Level'
        assert 800 <= course.price <= 1500
        assert course.kind == 0
        assert course.subject_fk.id > 0

    def test_sub_course(self, sub_course):
        """Test several SubCourse's fields"""

        assert sub_course.day == 1
        assert sub_course.lesson_hour == 3
        assert sub_course.season_fk.id > 0
        assert sub_course.course_fk.id > 0
        assert sub_course.teacher_fk.id > 0

    def test_device(self, device):
        """Test several Device's fields"""

        assert device.name == 'Huawei E365'
        assert device.active

    def test_sms(self, sms):
        """Test several Sms's fields"""

        assert len(sms.phone) <= 15
        assert sms.message == 'You are register in Computer 1 course'
        assert sms.status == 1
        # assert sms.device_fk.id > 0

    def test_assign(self, assign):
        """Test several Assign's fields"""

        assert assign.sale in range(0, 15)
        assert assign.price == calculate_price(assign)
        assert assign.reason == '-'

        assert assign.student_fk.id > 0
        assert assign.subcourse_fk.id > 0

    def test_payment(self, payment):
        """Test several Payment's fields"""

        assert payment.amount <= get_maximum_price(payment)
        assert payment.type == 1
        assert payment.source == 1
        assert payment.contract == 1

        assert payment.student_fk.id > 0
        assert payment.subcourse_fk.id > 0
