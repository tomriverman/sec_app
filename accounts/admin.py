from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import MyUser

# Register your models here.

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display = ('username','full_name', 'phone', 'city', 'nat_id','is_admin','is_staff','is_livr', 'is_confirm', 'is_pack' )

	list_filter = ('is_admin','is_staff','is_livr')

	fieldsets = (
			(None, {'fields': ('username','password','full_name','phone','city','nat_id')}),
			('Permissions', {'fields': ('is_admin','is_staff','is_livr', 'is_confirm', 'is_pack')})
		)
	search_fields = ('username','city')
	ordering = ('username','city','is_admin','is_staff','is_livr', 'is_confirm', 'is_pack')

	filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)


admin.site.unregister(Group)