import imp
#table_functions = imp.load_module('reformat', *imp.find_module('reformat', ['data']))
DATABASE_CONFIG = {
        'user':'postgres',
        'db':'candsites',
        }
ERSATZPG_CONFIG = {
        'debug':True
        }
ERSATZPG_CONFIG.update(DATABASE_CONFIG)

