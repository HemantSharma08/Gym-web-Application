from django.contrib import admin
from django.urls import path
from gym.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout/',Logout, name="logout"),
    path('user_logout/',user_logout, name="user_logout"),
    path('user_profile/', user_profile, name="user_profile"),
    path('user_change_password/', user_change_password, name="user_change_password"),
    path('booking_history/', booking_history, name='booking_history'),
    path('manageCategory/', manageCategory, name='manageCategory'),
    path('editCategory/<int:pid>', editCategory, name='editCategory'),
    path('deleteCategory/<int:pid>', deleteCategory, name='deleteCategory'),
    path('managePackageType/', managePackageType, name='managePackageType'),
    path('editPackageType/<int:pid>', editPackageType, name='editPackageType'),
    path('deletePackageType/<int:pid>', deletePackageType, name='deletePackageType'),
    path('reg_user/', reg_user, name="reg_user"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('deleteBooking/<int:pid>', deleteBooking, name='deleteBooking'),
    path('addPackage', addPackage, name='addPackage'),
    path('managePackage/', managePackage, name='managePackage'),
    path('deletePackage/<int:pid>', deletePackage, name='deletePackage'),
    path('new_booking/', new_booking, name='new_booking'),
    path('bookingReport/', bookingReport, name='bookingReport'),
    path('regReport/', regReport, name='regReport'),
    path('changePassword', changePassword, name='changePassword'),
    path('editPackage/<int:pid>', editPackage, name='editPackage'),
    path('registration',registration, name="registration"),
    path('user_login/',user_login, name="user_login"),
    path('apply-booking/<int:pid>/', apply_booking, name="apply_booking"),
    path('booking_detail/<int:pid>/', booking_detail, name="booking_detail"),

]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
