from modeltranslation.translator import translator, TranslationOptions
from .models import Course, CoursePoint,Event,Career,Blog,Team,Banner,Branch,BranchCourse,Testimonial,Endorsement,FAQ,Partner
from exams.models import Examination

class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description','duration', 'fees',)


class CoursePointTranslationOptions(TranslationOptions):
    fields = ('content',)


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'venue','details','platform',)


class CareerTranslationOptions(TranslationOptions):
    fields = ('title', 'description','branch',)


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description','person_name',)


class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'designation',)


class BannerTranslationOptions(TranslationOptions):
    fields = ('banner_head', 'title', 'content',)


class BranchTranslationOptions(TranslationOptions):
    fields = ('branch_name', 'description','location','about_branch')


class BranchCourseTranslationOptions(TranslationOptions):
    fields = ('course_name','details', 'description','duration', 'fees',)


class TestimonialTranslationOptions(TranslationOptions):
    fields = ('person_name', 'designation', 'review',)


class EndorsementTranslationOptions(TranslationOptions):
    fields = ('name', 'designation',)


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


class PartnerTranslationOptions(TranslationOptions):
    fields = ('name',)


class ExaminationTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Course, CourseTranslationOptions)
translator.register(CoursePoint, CoursePointTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Career, CareerTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(Team, TeamTranslationOptions)
translator.register(Banner, BannerTranslationOptions)
translator.register(Branch, BranchTranslationOptions)
translator.register(BranchCourse, BranchCourseTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(Endorsement, EndorsementTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(Partner, PartnerTranslationOptions)
translator.register(Examination,ExaminationTranslationOptions)
