import sys

pytest_plugins = 'pytester',


def test_main(testdir):
    testdir.makefile('.ini', tox="""[tox]
envlist = foobar
skipsdist = true

[testenv]
commands =
    python -c "import sys; print('sys.executable=%%r' %% sys.executable)"
    python -c "import sys; sys.executable == %r and sys.stdout.write('OK\\n')"
""" % (
        sys.executable,
    ))
    result = testdir.run('tax', '-e', 'foobar')
    result.stdout.fnmatch_lines([
        "foobar create: *",
        "foobar installed: *",
        "foobar runtests: PYTHONHASHSEED=*",
        "foobar runtests: commands[[]0[]] | *",
        "sys.executable=*",
        "foobar runtests: commands[[]1[]] | *",
        "OK",
    ])
