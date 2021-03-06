import importlib

class ModulesLoader():
    __loaded_modules = []

    @staticmethod
    def get_module_content_folder(module_name):
        return "content/{}".format(module_name)

    @staticmethod
    def get_module_folder(module_name):
        return "modules/{}".format(module_name)

    @staticmethod
    def get_module_package(module_name):
        return "modules.{}".format(module_name)

    @staticmethod
    def get_module_id(module_name):
        return ModulesLoader.__loaded_modules.index(module_name)

    @staticmethod
    def initialize_module(module_name):
        if ModulesLoader.is_module_loaded(module_name):
            return

        # Solve dependencies
        dependencies = ModulesLoader.get_module_dependencies(module_name)

        for dependency in dependencies:
            ModulesLoader.initialize_module(dependency)

        initializer = importlib.import_module("{}.init".format(ModulesLoader.get_module_package(module_name)))

        initializer.initialize()

        ModulesLoader.__loaded_modules.append(module_name)

    @staticmethod
    def is_module_loaded(module_name):
        return module_name in ModulesLoader.__loaded_modules

    @staticmethod
    def connect_module(module_name):
        initializer = importlib.import_module("{}.init".format(ModulesLoader.get_module_package(module_name)))

        initializer.connect()

    @staticmethod
    def load_manager(module_name):
        initializer = importlib.import_module("{}.init".format(ModulesLoader.get_module_package(module_name)))

        manager = initializer.load_manager()

        return manager 

    @staticmethod
    def get_module_dependencies(module_name):
        initializer = importlib.import_module("{}.init".format(ModulesLoader.get_module_package(module_name)))

        return initializer.depends_on() 

    @staticmethod
    def launch_main_module(module_name):
        initializer = importlib.import_module("{}.init".format(ModulesLoader.get_module_package(module_name)))

        initializer.main()

