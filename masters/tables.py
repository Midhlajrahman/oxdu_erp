from core.base import BaseTable

from .models import State

from web.models import Course



class StateTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = State
        fields = ("name",)


class CourseTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = Course
        fields = ("course_name",)