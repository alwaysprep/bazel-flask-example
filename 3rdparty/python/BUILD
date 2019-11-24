load("@rules_python//python:defs.bzl", "py_library")
load("@3rdparty//:requirements.bzl", "requirement")

py_library(
    name = "flaks",
    visibility = ["//visibility:public"],
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
    visibility = ["//visibility:public"],
    deps = [
        requirement("pandas"),
        requirement("python-dateutil"),
        requirement("pytz"),
        requirement("numpy"),
        requirement("six"),
    ],
)