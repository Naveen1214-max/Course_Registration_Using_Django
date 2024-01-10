# Create your views here.
# course_registration/views.py

from django.shortcuts import render, redirect
from .models import Course





def delete_course(request, course_id): #remove course 
    course = Course.objects.get(pk=course_id)
    course.delete()
    #return redirect('course_list')
    return redirect('/courses/list/')

def drop_student(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.drop_student()
    print("Student dropped successfully.")
    return redirect('/courses/list/')

                  #  or 
    
'''
def drop_student(request, course_id):  # remove student
    course = Course.objects.get(course_id=course_id)
    #if course.open_seats > 0:
    if course.open_seats < course.capacity:
        #course.open_seats -= 1
        course.open_seats += 1
        #course.capacity += 1
        course.save()
        print("Student successfully dropped fromt the course.")
    else:
        print("No students are currently enrolled in this course.")
    return redirect('course_list')
'''


def add_student(request, course_id):
    course = Course.objects.get(pk=course_id)
    course.add_student()
    print("Student added successfully.")
    return redirect('/courses/list/')

                # or
'''
def add_student(request, course_id): # enroll student 
    course = Course.objects.get(course_id=course_id)
    #if course.open_seats < course.capacity:
    if course.open_seats > 0:
        #course.open_seats +=1
        course.open_seats -= 1
        #course.capacity -= 1
        course.save()
        print("Student Successfully enrolled in the course.")
    else:
        print("Sorry, the course is full. Unable to enroll more students.")
    return redirect('course_list')
'''



def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})



def add_course(request):
    if request.method == 'POST':
        capacity = request.POST.get('capacity', 30)
        course_id = request.POST['course_id']
        instructor = request.POST['instructor']
        course_title = request.POST['course_title']
        Course.objects.create(course_id=course_id, course_title=course_title, instructor=instructor, capacity=capacity, open_seats=capacity)
        #course.save()
        #return redirect('course_list')
        return redirect('/courses/list/')
    return render(request, 'add_course.html')

