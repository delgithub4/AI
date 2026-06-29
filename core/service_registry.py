from typing import Any


class ServiceRegistry:
    """
    Registers and resolves application services.

    Prevents tight coupling between services by providing
    a lightweight service locator.
    """

    def __init__(self):
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        self._services[name] = service

    def unregister(self, name: str) -> None:
        self._services.pop(name, None)

    def get(self, name: str):
        service = self._services.get(name)

        if service is None:
            raise KeyError(f"Service '{name}' is not registered.")

        return service

    def exists(self, name: str) -> bool:
        return name in self._services

    def clear(self) -> None:
        self._services.clear()

    def all(self):
        return self._services.copy()


service_registry = ServiceRegistry()
