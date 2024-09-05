from django.db import models

# লোগো মডেল, যা সাইটের লোগো সংরক্ষণ করবে
class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')  # লোগোর ইমেজ আপলোড হবে 'logos/' ফোল্ডারে
    alt_text = models.CharField(max_length=100, blank=True)  # লোগোর বিকল্প টেক্সট, যা ইচ্ছামত খালি রাখা যাবে

    def __str__(self):
        return self.alt_text or "Logo"  # লোগোর বিকল্প টেক্সট প্রদর্শন করবে, খালি থাকলে "Logo" দেখাবে

# কন্টাক্ট মডেল, যা ফোন নম্বর ও ইমেইল সংরক্ষণ করবে
class Contact(models.Model):
    phone = models.CharField(max_length=20)  # ফোন নম্বরের জন্য ফিল্ড
    email = models.EmailField()  # ইমেইলের জন্য ফিল্ড

    def __str__(self):
        return f"{self.phone} - {self.email}"  # ফোন এবং ইমেইল প্রদর্শন করবে

# সোশ্যাল মিডিয়া মডেল, যা নাম, লিংক এবং আইকন সংরক্ষণ করবে
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)  # সোশ্যাল মিডিয়ার নাম
    url = models.URLField()  # সোশ্যাল মিডিয়ার লিংক
    icon = models.ImageField(upload_to='social_icons/')  # সোশ্যাল মিডিয়ার আইকন আপলোড হবে 'social_icons/' ফোল্ডারে

    def __str__(self):
        return self.name  # সোশ্যাল মিডিয়ার নাম প্রদর্শন করবে

# ক্যারোসেল ইমেজ মডেল, যা ইমেজ ও ক্যাপশন সংরক্ষণ করবে
class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')  # ইমেজ আপলোড হবে 'carousel_images/' ফোল্ডারে
    caption = models.CharField(max_length=200, blank=True)  # ইমেজের ক্যাপশন, যা খালি রাখা যাবে

    def __str__(self):
        return f"Image {self.id}"  # ইমেজের আইডি প্রদর্শন করবে

# মেনু মডেল, যা সাইটের মেনু সংরক্ষণ করবে
class Menu(models.Model):
    title = models.CharField(max_length=255)  # মেনুর টাইটেল
    path = models.CharField(max_length=255, null=True, blank=True)  # মেনুর পথ, যা খালি রাখা যাবে

    def __str__(self):
        return self.title  # মেনুর টাইটেল প্রদর্শন করবে

# সাবমেনু মডেল, যা মেনুর অধীনে থাকবে
class SubMenu(models.Model):
    title = models.CharField(max_length=255)  # সাবমেনুর টাইটেল
    path = models.CharField(max_length=255, null=True, blank=True)  # সাবমেনুর পথ
    menu = models.ForeignKey('Menu', related_name='sub_menus', on_delete=models.SET_DEFAULT, default=1)  # মেনুর সাথে সংযুক্ত

    def __str__(self):
        return self.title  # সাবমেনুর টাইটেল প্রদর্শন করবে

# সাব-সাবমেনু মডেল, যা সাবমেনুর অধীনে থাকবে
class SubSubMenu(models.Model):
    title = models.CharField(max_length=255)  # সাব-সাবমেনুর টাইটেল
    path = models.CharField(max_length=255, null=True, blank=True)  # সাব-সাবমেনুর পথ
    sub_menu = models.ForeignKey('SubMenu', related_name='Sub_Sub_Menus', on_delete=models.SET_DEFAULT, default=1)  # সাবমেনুর সাথে সংযুক্ত

    def __str__(self):
        return self.title  # সাব-সাবমেনুর টাইটেল প্রদর্শন করবে

# থিম কালার মডেল, যা পৃষ্ঠার জন্য নির্দিষ্ট থিম কালার সংরক্ষণ করবে
class ThemeColor(models.Model):
    page_name = models.CharField(max_length=50, unique=True)  # পৃষ্ঠার নাম, যা ইউনিক হবে
    color_code = models.CharField(max_length=50)  # রঙের কোড, যা CSS এর ক্লাস হতে পারে

    def __str__(self):
        return self.page_name  # পৃষ্ঠার নাম প্রদর্শন করবে
from django.db import models

# লোগো মডেল, যা সাইটের লোগো সংরক্ষণ করবে
class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')  # লোগোর ইমেজ আপলোড হবে 'logos/' ফোল্ডারে
    alt_text = models.CharField(max_length=100, blank=True)  # লোগোর বিকল্প টেক্সট, যা ইচ্ছামত খালি রাখা যাবে

    def __str__(self):
        return self.alt_text or "Logo"  # লোগোর বিকল্প টেক্সট প্রদর্শন করবে, খালি থাকলে "Logo" দেখাবে

# কন্টাক্ট মডেল, যা ফোন নম্বর ও ইমেইল সংরক্ষণ করবে
class Contact(models.Model):
    phone = models.CharField(max_length=20)  # ফোন নম্বরের জন্য ফিল্ড
    email = models.EmailField()  # ইমেইলের জন্য ফিল্ড

    def __str__(self):
        return f"{self.phone} - {self.email}"  # ফোন এবং ইমেইল প্রদর্শন করবে

# সোশ্যাল মিডিয়া মডেল, যা নাম, লিংক এবং আইকন সংরক্ষণ করবে
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)  # সোশ্যাল মিডিয়ার নাম
    url = models.URLField()  # সোশ্যাল মিডিয়ার লিংক
    icon = models.ImageField(upload_to='social_icons/')  # সোশ্যাল মিডিয়ার আইকন আপলোড হবে 'social_icons/' ফোল্ডারে

    def __str__(self):
        return self.name  # সোশ্যাল মিডিয়ার নাম প্রদর্শন করবে

# ক্যারোসেল ইমেজ মডেল, যা ইমেজ ও ক্যাপশন সংরক্ষণ করবে
class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')  # ইমেজ আপলোড হবে 'carousel_images/' ফোল্ডারে
    caption = models.CharField(max_length=200, blank=True)  # ইমেজের ক্যাপশন, যা খালি রাখা যাবে

    def __str__(self):
        return f"Image {self.id}"  # ইমেজের আইডি প্রদর্শন করবে

# মেনু মডেল, যা সাইটের মেনু সংরক্ষণ করবে
class Menu(models.Model):
    title = models.CharField(max_length=255)  # মেনুর টাইটেল
    path = models.CharField(max_length=255, null=True, blank=True)  # মেনুর পথ, যা খালি রাখা যাবে

    def __str__(self):
        return self.title  # মেনুর টাইটেল প্রদর্শন করবে

# সাবমেনু মডেল, যা মেনুর অধীনে থাকবে
class SubMenu(models.Model):
    title = models.CharField(max_length=255)  # সাবমেনুর টাইটেল
    path = models.CharField(max_length=255, null=True, blank=True)  # সাবমেনুর পথ
    menu = models.ForeignKey('Menu', related_name='sub_menus', on_delete=models.SET_DEFAULT, default=1)  # মেনুর সাথে সংযুক্ত

    def __str__(self):
        return self.title  # সাবমেনুর টাইটেল প্রদর্শন করবে

# সাব-সাবমেনু মডেল, যা সাবমেনুর অধীনে থাকবে
class SubSubMenu(models.Model):
    title = models.CharField(max_length=255)  # সাব-সাবমেনুর টাইটেল
    path = models.CharField(max_length=255, null=True, blank=True)  # সাব-সাবমেনুর পথ
    sub_menu = models.ForeignKey('SubMenu', related_name='Sub_Sub_Menus', on_delete=models.SET_DEFAULT, default=1)  # সাবমেনুর সাথে সংযুক্ত

    def __str__(self):
        return self.title  # সাব-সাবমেনুর টাইটেল প্রদর্শন করবে

# থিম কালার মডেল, যা পৃষ্ঠার জন্য নির্দিষ্ট থিম কালার সংরক্ষণ করবে
class ThemeColor(models.Model):
    page_name = models.CharField(max_length=50, unique=True)  # পৃষ্ঠার নাম, যা ইউনিক হবে
    color_code = models.CharField(max_length=50)  # রঙের কোড, যা CSS এর ক্লাস হতে পারে

    def __str__(self):
        return self.page_name  # পৃষ্ঠার নাম প্রদর্শন করবে
