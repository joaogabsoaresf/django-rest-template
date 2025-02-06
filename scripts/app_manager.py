import os

class AppManager:
    def __init__(self):
        self.base_path = "core/"
        self.folder_name = "apps/"
        self.app_name = self.set_app_name()
        self.app_path = os.path.join(self.base_path, self.folder_name, self.app_name)

    def set_app_name(self):
        name = input("Enter the name of the new app: ")
        name = name.lower()
        name = name.replace(" ", "_")
        return name

    def create_dir(self):
        self.create_dir_with_init(self.app_path)
        self.create_dir_with_init(os.path.join(self.app_path, "migrations"))
    
    def create_dir_with_init(self, app_path):
        os.makedirs(app_path, exist_ok=True)
        with open(os.path.join(app_path, "__init__.py"), 'w') as f:
            f.write("")

    def create_files(self):
        files = ["apps.py", "models.py", "serializers.py", "views.py", "urls.py"]
        for file in files:
            file_path = os.path.join(self.app_path, file)
            with open(file_path, 'w') as f:
                if file == "apps.py":
                    f.write(
                        f"from django.apps import AppConfig\n\n\n"
                        f"class {self.app_name.capitalize()}Config(AppConfig):\n"
                        f"    default_auto_field = 'django.db.models.BigAutoField'\n"
                        f"    name = 'apps.{self.app_name}'"
                    )
                elif file == "models.py":
                    f.write(
                        f"from django.db import models\n\n\n"
                        f"class {self.app_name.capitalize()}(models.Model):\n"
                        f"    pass"
                    )
                elif file == "serializers.py":
                    f.write(
                        f"from rest_framework import serializers\n"
                        f"from apps.{self.app_name}.models import {self.app_name.capitalize()}\n\n\n"
                        f"class {self.app_name.capitalize()}Serializer(serializers.ModelSerializer):\n"
                        f"    class Meta:\n"
                        f"        model = {self.app_name.capitalize()}\n"
                        f"        fields = '__all__'"
                    )
                elif file == "views.py":
                    f.write(
                        f"from rest_framework import viewsets\n"
                        f"from apps.{self.app_name}.models import {self.app_name.capitalize()}\n"
                        f"from apps.{self.app_name}.serializers import {self.app_name.capitalize()}Serializer\n\n\n"
                        f"class {self.app_name.capitalize()}ViewSet(viewsets.ModelViewSet):\n"
                        f"    queryset = {self.app_name.capitalize()}.objects.all()\n"
                        f"    serializer_class = {self.app_name.capitalize()}Serializer"
                    )
                elif file == "urls.py":
                    f.write(
                        f"from django.urls import path, include\n"
                        f"from rest_framework.routers import DefaultRouter\n"
                        f"from apps.{self.app_name}.views import {self.app_name.capitalize()}ViewSet\n\n\n"
                    )
                else:
                    f.write("")

    def edit_settings(self):
        comment = "# Automatically add all apps in the apps folder"
        with open("core/config/settings.py", "r") as f:
            for line_number, line in enumerate(f, start=1):
                if comment in line:
                    return self.add_app_to_settings(line_number)

    def add_app_to_settings(self, line_number):
        with open("core/config/settings.py", "r") as f:
            lines = f.readlines()
            lines.insert(line_number - 1, f"    'apps.{self.app_name}',\n")
        with open("core/config/settings.py", "w") as f:
            f.writelines(lines)
