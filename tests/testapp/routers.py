# -*- coding:utf-8 -*-
from __future__ import absolute_import


class NothingOnSQLiteRouter(object):

    def allow_migrate(self, db, app_label, **hints):
        return db in ('default', 'other')
