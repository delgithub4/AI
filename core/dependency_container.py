from core.service_registry import service_registry


class DependencyContainer:

    @staticmethod
    def register(name, service):
        service_registry.register(name, service)

    @staticmethod
    def resolve(name):
        return service_registry.get(name)

    @staticmethod
    def registered():
        return service_registry.all()
