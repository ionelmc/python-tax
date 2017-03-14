import os
import sys

pytest_plugins = 'pytester',


def test_main(testdir):
    testdir.makefile('.ini', tox=r"""[tox]
envlist = foobar
skipsdist = true

[testenv]
commands =
    python -c "import sys; print('sys.executable=%r' % sys.executable)"
    python -c "import sys, os; sys.stdout.write('OK\n') if {0!r} == os.path.dirname(os.path.normcase(sys.executable)) else sys.stdout.write('BAD\n')"
""".format(os.path.dirname(os.path.normcase(sys.executable))))

    result = testdir.run('tax', '-v', '-e', 'foobar')
    result.stdout.fnmatch_lines([
        "foobar installed: *",
        "foobar runtests: PYTHONHASHSEED=*",
        "foobar runtests: commands[[]0[]] | *",
        "sys.executable=*",
        "foobar runtests: commands[[]1[]] | *",
        "OK",
    ])
