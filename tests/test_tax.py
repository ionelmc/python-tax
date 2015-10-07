import sys

pytest_plugins = 'pytester',


def test_main(testdir):
    testdir.makefile('.ini', tox="""[tox]
envlist = foobar
skipsdist = true

[testenv]
commands = python -c "import sys; assert sys.executable == %r, '%%s != %s' %% sys.executable; print('OK')"
""" % (
        sys.executable, sys.executable
    ))
    result = testdir.run('tax', '-e', 'foobar')
    result.stdout.fnmatch_lines([
        "foobar create: *",
        "foobar installed: *",
        "foobar runtests: *",
        "OK",
    ])
