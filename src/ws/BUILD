load("@3rdparty//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_binary(
  name = "main",
  srcs = ["main.py"],
  deps = [
    # Flask
    requirement("Flask"),
    requirement("Jinja2"),
    requirement("Werkzeug"),
    requirement("itsdangerous"),
    requirement("click"),
    requirement("MarkupSafe"),
    ## Pandas
    requirement("pandas"),
    requirement("python-dateutil"),
    requirement("pytz"),
    requirement("numpy"),
    requirement("six"),
  ]
)