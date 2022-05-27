from unicodedata import name
from django.shortcuts import redirect, render
from .models import Employee
# Create your views here.

# display table


def index(request):
    emp = Employee.objects.all()
    return render(request, "crud/index.html", {
        'employee': emp
    })

# add a employee


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(name=name, email=email, address=address, phone=phone)
        emp.save()
        # soon after save the employee, put into the browser the url called "index"
    return redirect("crud:index")


def edit(request):
    # soon after save the employee, put into the browser the url called "index"
    return render(request, "crud/index.html", {
        'employee': Employee.objects.all()
    })


def update(request, emp_id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(id=emp_id, name=name, email=email,
                       address=address, phone=phone)
        emp.save()
        return redirect("crud:index")

    return render(request, "crud/index.html", {
        'employee': Employee.objects.get(id=emp_id)
    })


def delete(request, emp_id):
    Employee.objects.filter(id=emp_id).delete()
    return redirect("crud:index")
