#!/usr/bin/env python
# encoding: utf-8

"""
❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
@author: iza e sofia
@license: GNU GENERAL PUBLIC LICENSE
@contact: izabela.head@gmail.com
@software: VSCode
@file: admin.py
❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
"""
from django.contrib.admin import AdminSite
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site


class SonoraAdminSite(AdminSite):
    site_header = 'Sonora administration'
    site_title = 'Sonora site admin'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser


admin_site = SonoraAdminSite(name='admin')

admin_site.register(Site, SiteAdmin)
