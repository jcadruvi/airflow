from airflow.hooks.hive_hooks import HiveServer2Hook


class HiveHook(HiveServer2Hook):

    def __init__(self, hiveserver2_conn_id='hiveserver2_default', schema='default'):
        super(HiveHook, self).__init__(hiveserver2_conn_id)
        self.schema = schema

