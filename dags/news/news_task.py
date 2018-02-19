from airflow.hooks.hive_hooks import HiveServer2Hook

from utils.airflow.hooks.hive_hook import HiveHook


class NewsTask(object):

    def show_table(self, templates_dict, **kwargs):
        hql = "select * from t1"
        print "In show_table...."
        print hql
        result = HiveHook().get_results(schema="default", hql=hql)
        print result