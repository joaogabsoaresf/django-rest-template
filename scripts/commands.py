import os
import inspect
import argparse
from app_manager import AppManager

class Commands:
    
    @classmethod
    def get_choices(cls):
        return [name for name, obj in inspect.getmembers(cls) if inspect.ismethod(obj) and not name.startswith('_') and not name == 'get_choices']
    
    @classmethod
    def create_app(cls):
        app_manager = AppManager()
        app_manager.create_dir()
        app_manager.create_files()
        app_manager.edit_settings()
    
    @classmethod
    def create_local_superuser(cls):
        os.system("python core/manage.py createsuperuser --username admin --email admim@joaosoares.dev")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("func", help="Função a ser executada", choices=Commands.get_choices())
    args = parser.parse_args()
    getattr(Commands, args.func)()
