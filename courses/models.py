from django.db import models

# Create your models here.
# course_registration/models.py


class Course(models.Model):
    course_id = models.CharField(max_length=50, primary_key=True)
    course_title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    capacity = models.IntegerField(default=30)
    open_seats = models.IntegerField(default=30)

    def __str__(self):
        return self.course_title
    
    def add_student(self):
        if self.open_seats > 0:
            self.open_seats -= 1
            self.save()
            print("Student successfully enrolled in the course.")
        else:
            print("Sorry, the course is full. Unable to enroll more students.")

    def drop_student(self):
        if self.open_seats < self.capacity:
            self.open_seats += 1
            self.save()
            print("Student successfully dropped from the course.")
        else:
            print("No students are currently enrolled in this course.")

