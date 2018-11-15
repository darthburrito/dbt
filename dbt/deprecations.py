from dbt.logger import GLOBAL_LOGGER as logger


class DBTDeprecation(object):
    name = None
    description = None

    def show(self, *args, **kwargs):
        if self.name not in active_deprecations:
            desc = self.description.format(**kwargs)
            logger.info("* Deprecation Warning: {}\n".format(desc))
            active_deprecations.add(self.name)


class SqlWhereDeprecation(DBTDeprecation):
    name = "sql_where"
    description = """\
The `sql_where` option for incremental models is deprecated and will be
  removed in a future release. Check the docs for more information

  https://docs.getdbt.com/docs/materializations
  """


class SeedDropExistingDeprecation(DBTDeprecation):
    name = 'drop-existing'
    description = """The --drop-existing argument to `dbt seed` has been
  deprecated. Please use --full-refresh instead. The --drop-existing option
  will be removed in a future version of dbt."""


def warn(name, *args, **kwargs):
    if name not in deprecations:
        # this should (hopefully) never happen
        raise RuntimeError(
            "Error showing deprecation warning: {}".format(name)
        )

    deprecations[name].show(*args, **kwargs)


# these are globally available
# since modules are only imported once, active_deprecations is a singleton

active_deprecations = set()

deprecations_list = [
    SqlWhereDeprecation(),
    SeedDropExistingDeprecation()
]

deprecations = {d.name: d for d in deprecations_list}


def reset_deprecations():
    active_deprecations.clear()
