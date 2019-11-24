load("@rules_python//python:defs.bzl", "py_library")
load("@3rdparty//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "flask",
    deps = [
        requirement("Flask"),
        requirement("Jinja2"),
        requirement("Werkzeug"),
        requirement("itsdangerous"),
        requirement("click"),
        requirement("MarkupSafe"),
    ],
)

py_library(
    name = "pandas",
    deps = [
        requirement("pandas"),
        requirement("python-dateutil"),
        requirement("pytz"),
        requirement("numpy"),
        requirement("six"),
    ],
)

py_library(
    name = "pytest",
    deps = [
        requirement("pytest"),
        requirement("pluggy"),
        requirement("py"),
        requirement("packaging"),
        requirement("importlib-metadata"),
        requirement("more-itertools"),
    ],
)
