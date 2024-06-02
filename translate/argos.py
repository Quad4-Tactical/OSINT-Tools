import argostranslate.package, argostranslate.translate

def setup_translation(from_code, to_code):
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        (pkg for pkg in available_packages if pkg.from_code == from_code and pkg.to_code == to_code), None
    )
    if package_to_install:
        argostranslate.package.install_from_path(package_to_install.download())

def translate_text(text, from_code, to_code):
    setup_translation(from_code, to_code)
    return argostranslate.translate.translate(text, from_code, to_code)