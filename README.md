# Python Bazel Example

- Bazel example with flask and pandas and pytest.
- Flask auto reloading enabled for development.

Install Bazel
---
If you don't have Bazel in your computer, you can install it from <a target='_blank' href='https://docs.bazel.build/versions/master/install.html'>here</a>.

Run
---
```shell script
git clone https://github.com/alwaysprep/bazel-flask-example.git
cd bazel-flask-example
bazel run //src/python/ws:wsgi   
```

Test
---
```shell script
bazel test //test/python/ws:entire
```

  
Contributing
------------

0. If you have any suggestions feel free to file an issue.
0. Pull requests are very welcome, but consider creating an issue first,
so we can discuss and decide together.
