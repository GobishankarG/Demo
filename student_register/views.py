from django.shortcuts import render,redirect
from.forms import StudentRegisterForm
from .models import student_register

def create_student_register(request):
    if request.method=="POST":
        form=StudentRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form=StudentRegisterForm()
    return  render(request,"create.html",{"form":form})

#Search Student register
def search_student_register(request):
    student_registers=student_register.objects.all()
    return render(request,'search.html',{'student_registers':student_registers})


# Update student_register

def update_student_register(request,pk):
    student_registers = student_register.objects.get(id=pk)
    form = StudentRegisterForm(instance=student_registers)

    if request.method == 'POST':
        form = StudentRegisterForm(request.POST,request.FILES, instance=student_registers)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'student_registers': student_registers,
        'form': form,
    }
    return render(request,'update.html',context)


# Delete student_register

def delete_student_register(request, pk):
    student_registers = student_register.objects.get(id=pk)

    if request.method == 'POST':
        student_registers.delete()
        return redirect('/search')

    context = {
        'student_registers': student_registers,
    }
    return render(request, 'remove.html', context)
