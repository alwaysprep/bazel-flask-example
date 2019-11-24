load("@3rdparty//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "ws",
    srcs = glob(["**/*.py"]),
    deps = [
        # Flask
        "//3rdparty/python:flask",
         "//3rdparty/python:pandas"
    ],
)

py_binary(
  name = "wsgi",
  srcs = ["wsgi.py"],
  deps = [
    ":ws"
  ]
)