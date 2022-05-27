from django.urls import path
from . import views


# to avoid url name colision
app_name = "crud"

# all the url for this App
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("edit", views.edit, name="edit"),
    path("update/<int:emp_id>", views.update, name="update"),
    path("delete/<int:emp_id>", views.delete, name="delete"),

]
