import pkgutil
import sys

from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import List

branch_coverage = {
    "get_path_1": False,
    "get_path_2": False,
    "get_path_3": False,
    "get_path_4": False,
    "get_path_5": False,
    "get_path_6": False,
    "get_path_7": False,
    "list_module_1": False,
    "list_module_2": False
}


def get_path(module: ModuleType, testing: bool = False) -> str:
    if getattr(sys, "frozen", False) or testing:
        # frozen
        branch_coverage["get_path_1"] = True

        if getattr(sys, "_MEIPASS", False):
            # PyInstaller
            branch_coverage["get_path_2"] = True
            lib_dir = Path(getattr(sys, "_MEIPASS"))
        else:
            # others
            branch_coverage["get_path_3"] = True
            lib_dir = Path(sys.executable).parent / "lib"

        path = lib_dir.joinpath(*module.__package__.split("."))  # type: ignore
    else:
        branch_coverage["get_path_4"] = True
        # unfrozen
        branch_coverage["get_path_5"] = True
        if module.__file__ is not None:
            path = Path(module.__file__).parent
            branch_coverage["get_path_6"] = True
        else:
            raise RuntimeError(f"Can't find path from module `{module}.")
        branch_coverage["get_path_7"] = True
    return str(path)


def list_module(module: ModuleType, testing: bool = False) -> List[str]:
    global file
    path = get_path(module)

    if getattr(sys, "_MEIPASS", False) or testing:
        # PyInstaller
        branch_coverage["list_module_1"] = True
        return [file.parent.name for file in Path(path).glob("*/__init__.py")]
    else:
        branch_coverage["list_module_2"] = True
        return [name for _, name, is_pkg in pkgutil.iter_modules([str(path)]) if is_pkg]

def find_available_locales(providers: List[str]) -> List[str]:
    available_locales = set()

    for provider_path in providers:
        provider_module = import_module(provider_path)
        if getattr(provider_module, "localized", False):
            langs = list_module(provider_module)
            available_locales.update(langs)
    return sorted(available_locales)


def find_available_providers(modules: List[ModuleType]) -> List[str]:
    available_providers = set()
    for providers_mod in modules:
        if providers_mod.__package__:
            providers = [
                ".".join([providers_mod.__package__, mod]) for mod in list_module(providers_mod) if mod != "__pycache__"
            ]
            available_providers.update(providers)
    return sorted(available_providers)
