from .models import Course, Meta


def main_context(request):
    course = Course.objects.all()
    meta = Meta.objects.all().last()

    return {"course_header": course, "meta": meta}
