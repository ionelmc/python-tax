from tox.session import Session
from tox.session import VirtualEnv
from tox.session import prepare


class TaxSession(Session):
    def _makevenv(self, name):
        envconfig = self.config.envconfigs.get(name, None)
        if envconfig is None:
            self.report.error("unknown environment %r" % name)
            raise LookupError(name)
        venv = FakeVirtualEnv(envconfig=envconfig, session=self)
        self._name2venv[name] = venv
        return venv


class FakeVirtualEnv(VirtualEnv):
    def create(self, action=None):
        self.just_created = True

    def _pcall(self, args, cwd, venv=True, testcommand=False,
               action=None, redirect=True, ignore_ret=False):
        cwd.ensure(dir=1)
        args[0] = self.getcommandpath(args[0], venv, cwd)
        env = self._getenv(testcommand=testcommand)
        return action.popen(args, cwd=cwd, env=env,
                            redirect=redirect, ignore_ret=ignore_ret)

    def is_allowed_external(self, _):
        return True


def main(args=None):
    try:
        config = prepare(args)
        retcode = TaxSession(config).runcommand()
        raise SystemExit(retcode)
    except KeyboardInterrupt:
        raise SystemExit(2)
