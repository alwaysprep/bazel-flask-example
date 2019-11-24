load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "test_app",
    srcs = ["test_app.py"],
    deps = [
        "//3rdparty/python:pytest",
        "//src/python/ws",
    ],
)

py_test(
    name = "test_conf",
    srcs = ["test_conf.py"],
    deps = [
        "//3rdparty/python:pytest",
        "//src/python/ws",
    ],
)

test_suite(
    name = "entire",
    tests = [
        "test_app",
        "test_conf",
    ],
)
