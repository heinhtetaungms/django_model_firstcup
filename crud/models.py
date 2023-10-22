from django.db import models


# User model
class User(models.Model):
    first_name = models.CharField(max_length=30, default='John')
    last_name = models.CharField(max_length=30, default='Doe')
    dob = models.DateField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Instructor model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Is full time: {self.full_time}, Total Learners: {self.total_learners}"


# Course model
class Course(models.Model):
    name = models.CharField(max_length=100, default='Online Course')
    description = models.CharField(max_length=500)
    instructors = models.ManyToManyField(Instructor)
    learners = models.ManyToManyField(User, related_name='courses_learners', through='Enrollment')

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"


# Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="Title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()


# Enrollment model
class Enrollment(models.Model):
    learner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)


# Learner model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'

    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]

    occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES, default=STUDENT)
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Date of Birth: {self.dob}, Occupation: {self.occupation}, Social Link: {self.social_link}"
