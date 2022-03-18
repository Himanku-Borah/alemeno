from django.contrib import admin
from .models import Kid, Image
from .helper import sendEmail
from django.contrib import messages
class KidAdmin(admin.ModelAdmin):
  list_display = ('kid_name', 'kid_age', 'parent_phone', 'parent_email',)

class ImageAdmin(admin.ModelAdmin):
  fields = ('kid', 'image_url', "thumbnail", 'is_approved', 'food_group','created_on', "updated_on","approved_by",)
  radio_fields = {'food_group': admin.HORIZONTAL}
  list_display = ('kid', 'image_url', 'created_on', 'updated_on', 'approved_by', 'food_group',)
  readonly_fields = ("updated_on","approved_by","thumbnail",)

  def save_model(self, request, obj, form, change):
    if not obj.approved_by:
      obj.approved_by = request.user
      if obj.food_group == "Unknown":
        template = 'alemeno/send_mail.html'
        sendEmail(user=request.user, mail_subject="Food Category Alert", template=template, kid_id = obj.kid_id, kid=obj.kid)
        messages.add_message(request, messages.INFO, 'An email has been sent for unknown category.')
        print("Kid id is----------------")
        print(obj.kid_id)
    obj.save()

admin.site.register(Kid, KidAdmin)
admin.site.register(Image, ImageAdmin)