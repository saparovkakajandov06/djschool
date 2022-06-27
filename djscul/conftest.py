# third-party
import pytest
from pytest_factoryboy import register
from starlette.testclient import TestClient

# Django
import django
from django.contrib.auth.hashers import make_password

# local FastAPI
from backend.api.v1.main import app

###
# Django environment
###

django.setup()

###
# Import FastAPI environment
###


"""..."""


# local PyTest
from tests.factories import (UserFactory, BranchFactory, GroupFactory,
                             EmployeeFactory, StudentFactory, RelativeFactory,
                             SeasonFactory, RoomFactory, SubjectFactory,
                             CourseFactory, SubCourseFactory, DeviceFactory,
                             SmsFactory, AssignFactory, PaymentFactory)  # noqa E402

# Register all factories
register(UserFactory)
register(BranchFactory)
register(GroupFactory)
register(EmployeeFactory)
register(StudentFactory)
register(RelativeFactory)
register(SeasonFactory)
register(RoomFactory)
register(SubjectFactory)
register(CourseFactory)
register(SubCourseFactory)
register(DeviceFactory)
register(SmsFactory)
register(AssignFactory)
register(PaymentFactory)


####
# API
####

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here


####
# Core APP
####

# If you need access to the User (for example) several times in your Test,
#  create a fixture and use it in the test
@pytest.fixture
def user(db, user_factory):
    """Create user"""
    user = user_factory.create()
    user.set_password(user.password)
    user.save()
    return user


@pytest.fixture
def superuser(db, user_factory):
    """Create user"""
    user = user_factory.create(is_superuser=True)
    user.set_password(user.password)
    user.save()
    return user


@pytest.fixture
def branch(db, branch_factory):
    """Create branch"""
    branch = branch_factory.create()
    return branch


@pytest.fixture
def group(db, group_factory):
    """Create job"""
    group = group_factory.create()
    return group


@pytest.fixture
def employee(db, employee_factory):
    """Create employee"""

    branch1 = BranchFactory.create(name='Branch 1')
    branch2 = BranchFactory.create(name='Branch 2')

    employee = employee_factory.create(branch_fk=(branch1, branch2))

    return employee


@pytest.fixture
def student(db, student_factory):
    """ Create assign"""
    student = student_factory.create()
    return student


@pytest.fixture
def relative(db, relative_factory):
    """Create relative"""
    relative = relative_factory.create()
    return relative


@pytest.fixture
def season(db, season_factory):
    """Create season"""
    season = season_factory.create()
    return season


@pytest.fixture
def room(db, room_factory):
    """Create room"""
    room = room_factory.create()
    return room


@pytest.fixture
def subject(db, subject_factory):
    """Create subject"""
    subject = subject_factory.create()
    return subject


@pytest.fixture
def course(db, course_factory):
    """Create course"""
    course = course_factory.create()
    return course


@pytest.fixture
def sub_course(db, sub_course_factory):
    """Create subcourse"""
    sub_course = sub_course_factory.create()
    return sub_course


@pytest.fixture
def device(db, device_factory):
    """Create device"""
    device = device_factory.create()
    return device


@pytest.fixture
def sms(db, sms_factory):
    """Create sms"""
    sms = sms_factory.create()
    return sms


@pytest.fixture
def assign(db, assign_factory):
    """Create assign"""
    assign = assign_factory.create()
    return assign


@pytest.fixture
def payment(db, payment_factory):
    """Create payment"""
    payment = payment_factory.create()
    return payment
