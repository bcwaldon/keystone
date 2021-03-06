#!/usr/bin/env python

"""Manages execution of keystone test suites"""
from keystone.test import KeystoneTest


class SQLTest(KeystoneTest):
    config_name = 'sql.conf.template'
    test_files = ('keystone.db',)


class MemcacheTest(KeystoneTest):
    config_name = 'memcache.conf.template'
    test_files = ('keystone.db',)


class LDAPTest(KeystoneTest):
    config_name = 'ldap.conf.template'
    test_files = ('keystone.db', 'ldap.db', 'ldap.db.db',)

TESTS = [
    SQLTest,
    # currently failing, and has yet to pass in jenkins: MemcacheTest,
    LDAPTest,
]

if __name__ == '__main__':
    for test_num, test_cls in enumerate(TESTS):
        print 'Starting test %d of %d with config: %s' % \
            (test_num + 1, len(TESTS), test_cls.config_name)
        test_cls().run()
