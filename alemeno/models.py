from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.admin.decorators import display
from django.template.loader import get_template
from django.urls import reverse


class LowercaseEmailField(models.EmailField):
  def to_python(self, value):
    """
    Convert email to lowercase.
    """
    value = super(LowercaseEmailField, self).to_python(value)
    # Value can be None so check that it's a string before lowercasing.
    if isinstance(value, str):
        return value.lower()
    return value

#Kids table
class Kid(models.Model):
  kid_name  = models.CharField(max_length=200, blank=False)
  kid_age = models.PositiveSmallIntegerField(blank=False)
  parent_phone = models.CharField(max_length=10, blank=False)
  parent_email = LowercaseEmailField(_('email address'), unique=True)

  def __str__(self):
      return self.kid_name
  class Meta:
    db_table = 'kid_table'
    managed = True
    verbose_name = 'Kid'
    verbose_name_plural = 'kids'

#Food group categories
FOOD_CHOICES = (
  ('Fruit', 'Fruit'),
  ('Vegetable', 'Vegetable'),
  ('Grain', 'Grain'),
  ('Protein', 'Protein'),
  ('Dairy', 'Dairy'),
  ('Unknown', 'Unknown'),
)
#Image Table
class Image(models.Model):
  kid = models.ForeignKey(Kid, blank=False, on_delete=models.CASCADE)
  image_url = models.URLField(blank=False)
  # created_on = models.DateTimeField(auto_now_add=True)
  created_on = models.DateTimeField(default=timezone.now)
  updated_on = models.DateTimeField(auto_now=True)
  is_approved = models.BooleanField()
  approved_by = models.ForeignKey(User, blank=True, editable=False, on_delete=models.DO_NOTHING, null=True, verbose_name='Updated By')
  food_group = models.CharField('Group', choices=FOOD_CHOICES,  max_length=50)

  @display(description='Image')
  def thumbnail(self):
    return get_template('alemeno/preview.html').render({
        'field_name': 'image_url',
        'src': self.image_url if self.image_url else None,
    })

  def __str__(self):
      return self.food_group
  class Meta:
    db_table = 'image_table'
    managed = True
    verbose_name = 'Image'
    verbose_name_plural = 'Images'