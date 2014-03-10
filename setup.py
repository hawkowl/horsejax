from setuptools import setup

# From http://stackoverflow.com/questions/7275295/how-do-i-write-a-setup-py-for-a-twistd-twisted-plugin-that-works-with-setuptools
try:
    from setuptools.command import egg_info
    egg_info.write_toplevel_names
except (ImportError, AttributeError):
    pass
else:
    def _top_level_package(name):
        return name.split('.', 1)[0]

    def _hacked_write_toplevel_names(cmd, basename, filename):
        pkgs = dict.fromkeys(
            [_top_level_package(k)
                for k in cmd.distribution.iter_distribution_names()
                if _top_level_package(k) != "twisted"
            ]
        )
        cmd.write_file("top-level names", filename, '\n'.join(pkgs) + '\n')

    egg_info.write_toplevel_names = _hacked_write_toplevel_names

setup(
    name="horsejax",
    version="0.1",
    description="Secure password generator via not so secure JSON.",
    long_description=(
        "Like http://correcthorsebatterystaple.net/ except it is a HTTP API"
        " which is logging your passwords and sending them all to the NSA."
    ),
    author="HawkOwl",
    author_email="hawkowl@atleastfornow.net",
    maintainer="HawkOwl",
    maintainer_email="hawkowl@atleastfornow.net",
    url="https://github.com/hawkowl/horsejax/",
    packages=["horsejax", "twisted.plugins"],
    package_data=dict(
        horsejax=["*.json"],
    ),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=[
        "horsephrase",
        "haddock"
    ]
)


# Make Twisted regenerate the dropin.cache, if possible.  This is necessary
# because in a site-wide install, dropin.cache cannot be rewritten by
# normal users.
try:
    from twisted.plugin import IPlugin, getPlugins
except ImportError:
    pass
else:
    list(getPlugins(IPlugin))