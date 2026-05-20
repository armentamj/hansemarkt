from django.db import models  # Essential for creating database tables
from django.conf import settings  # Used to safely reference your User model
from django_resized import ResizedImageField # Used for making all cellphone images very memory efficiant.

class Goods(models.Model):
    # Links the item to a User (Staff/Owner). 
    # SET_NULL: If the user is deleted, the product stays in the database.
    # null/blank=True: Allows items to exist without an assigned user.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='goods'
    )

    # This is the "per line"
    unit = models.CharField(
    max_length=50,
    default="Stück",  # This fills existing items with "Stück" (piece)
    help_text="z.B. kg, Liter, Dose, Flasche"
    )

    class Meta:
        # Changes the name of a single item
        verbose_name = "Ware" 
        # Changes the name of the section in the admin list
        verbose_name_plural = "Waren" 

    
    # The name of the product (max 200 characters)
    name = models.CharField(max_length=200)
    
    # Stores the price (e.g., 999.99). max_digits is total digits, decimal_places is cents.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # A toggle to show/hide the product on your website newspaper index
    is_active = models.BooleanField(default=True)
    
    # Allows image uploads. Files will be saved in a 'media/goods_images/' folder.
    image = ResizedImageField(
        size=[1200, 1200],       # Max width/height. Keeps aspect ratio, but prevents giant 4K mobile uploads.
        quality=80,              # Drastically shrinks file size with no visible quality loss.
        force_format='WEBP',     # Converts heavy mobile JPEGs into ultra-light WebP files.
        upload_to='goods_images/', 
        blank=True, 
        null=True
    )
    
    # Automatically records the date/time when the item was first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Tells Django to show the actual name (e.g., "Apples") in the admin panel 
    # instead of "Goods object (1)"
    def __str__(self):
        return self.name