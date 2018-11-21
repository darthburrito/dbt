![dbt logo](/etc/dbt-horizontal.png)

[![Code Climate](https://codeclimate.com/github/fishtown-analytics/dbt/badges/gpa.svg)](https://codeclimate.com/github/fishtown-analytics/dbt)
[![CircleCI](https://circleci.com/gh/fishtown-analytics/dbt/tree/master.svg?style=svg)](https://circleci.com/gh/fishtown-analytics/dbt/tree/master)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/v01rwd3q91jnwp9m/branch/development?svg=true)](https://ci.appveyor.com/project/DrewBanin/dbt/branch/development)
[![Slack](https://slack.getdbt.com/badge.svg)](https://slack.getdbt.com)

**[dbt](https://www.getdbt.com/)** (data build tool) enables data analysts and engineers to transform data in their warehouses by simply writing select statements.

These select statements, or "models", form a dbt project. These models frequently build on top of one another - dbt makes it easy to [manage relationships](https://docs.getdbt.com/reference#ref) between models, and [visualize these relationships ](https://docs.getdbt.com/docs/documentation), as well as assure the quality of your transformations through [testing](https://docs.getdbt.com/docs/testing).

dbt projects are used to [aggregate pageviews into sessions](https://github.com/fishtown-analytics/snowplow), calculate [ad spend ROI](https://github.com/fishtown-analytics/facebook-ads), or report on [email campaign performance](https://github.com/fishtown-analytics/mailchimp).


![dbt dag](/etc/dag.png?raw=true)

## Learn More About dbt
* Check out the [Introduction to dbt](https://dbt.readme.io/docs/introduction).
* Read the [dbt Viewpoint](https://dbt.readme.io/docs/viewpoint).

## Getting Started
* [Install dbt](https://docs.getdbt.com/docs/installation)
* Read the [documentation](https://docs.getdbt.com/).
* Productionize your dbt project with [Sinter](https://www.sinterdata.com)


## Join the dbt Community
- Join the [chat](http://ac-slackin.herokuapp.com/) on Slack.
- Find community posts on the [dbt Discourse](https://discourse.getdbt.com).

## Reporting Bugs and Contributing Code
* Want to report a bug or request a feature? Let us know on [Slack](http://ac-slackin.herokuapp.com/), or open [an issue](https://github.com/fishtown-analytics/dbt/issues/new).
* Want to help us build dbt? Check out the [Contributing Guidelines](/CONTRIBUTING.md)

## Code of Conduct
Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct].
