from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import CourseModelForm
from .models import Course
# BASE VIEW Class =VIEW

class CourseObjectMixin(object):
    model= Course
    #lookup = 'id'   
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj=get_object_or_404(self.model, id=id)
        return obj    


class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    
    def get(self, request, *args, **kwargs): #None means id is not required
        #GET Method
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs): #None means id is not required
        #POST Method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)
    
class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj=get_object_or_404(Course, id=id)
        return obj
    
    def get(self, request, id=None, *args, **kwargs): 
        #GET Method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance= obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs): 
        #POST Method
        #form = CourseModelForm(request.POST)
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance= obj)
            if form.is_valid():
                form.save()
                #form = CourseModelForm()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
     
class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()
    
    def get_queryset(self):
        return self.queryset
    
    def get(self, request, *args, **kwargs):
        context = {'object_list':self.get_queryset()}
        return render(request, self.template_name, context)

# class MyListView(CourseListView):    #inheritance also possible
#     queryset = Course.objects.filter(id=1)

class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    #GET Method
    def get(self, request, id=None, *args, **kwargs): #None means id is not required
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

class CourseDeleteView(CourseObjectMixin, View): #maintain seq of args
    template_name = 'courses/course_delete.html'
    
    def get(self, request, id=None, *args, **kwargs): 
        #GET Method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs): 
        #POST Method
        #form = CourseModelForm(request.POST)
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)
         

 
# HTTP Methods
def my_fbv(request, *args, **kwargs):
    #print(request.method)
    return render(request, 'courses/about.html', {})