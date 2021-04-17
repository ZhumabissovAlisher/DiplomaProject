from django.shortcuts import render
from user_page.models import News , Course , Teacher , Blog

# Create your views here.

def main(request):
    news = News.objects.all()
    teachers = Teacher.objects.all()
    blogs = Blog.objects.all()
    context = {
        'news':news,
        'teachers':teachers,
        'blogs': blogs
    }
    
    return render(request,'index.html',context)

def news_special(request,pk):
    news = News.objects.get(pk=pk)
    context = {
        'news':news
    }
    
    return render(request,'news_special.html',context)

def student(request):
    return render(request,'student.html')

def teacher(request):
    teachers = Teacher.objects.all()

    teacher = {
        'teachers':teachers
    }
    return render(request,'teacher.html',teacher)

def course(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request,'course.html',context)

def programming(request):
    return render(request,'course.html')

def ent(request):
    return render(request,'course.html')

def exam(request):
    return render(request,'course.html')

def sport(request):
    return render(request,'course.html')

def technology(request):
    return render(request,'course.html')

def art(request):
    return render(request,'course.html')
