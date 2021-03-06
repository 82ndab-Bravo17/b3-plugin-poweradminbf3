# -*- encoding: utf-8 -*-
import time, os
from tests import prepare_fakeparser_for_tests
prepare_fakeparser_for_tests()

from b3.fake import fakeConsole
from b3.fake import admin

from poweradminbf3 import Poweradminbf3Plugin

from b3.config import XmlConfigParser

conf = XmlConfigParser()
conf.setXml("""
<configuration plugin="poweradminbf3">
    <settings name="commands">
        <set name="loadconfig">40</set>
    </settings>
    <settings name="preferences">
        <set name="config_path">%(script_dir)s</set>
    </settings>
</configuration>
""" % {'script_dir': os.path.abspath(os.path.join(os.path.dirname(__file__), '../extplugins/conf/serverconfigs'))})

p = Poweradminbf3Plugin(fakeConsole, conf)
p.onLoadConfig()
p.onStartup()

admin.connects(2)
admin.says('!loadconfig hardcore-tdm')
time.sleep(2)

admin.says('!loadconfig hardcore-')
time.sleep(2)