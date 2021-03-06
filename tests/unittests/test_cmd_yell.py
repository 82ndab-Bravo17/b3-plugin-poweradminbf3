# -*- encoding: utf-8 -*-
from b3.config import XmlConfigParser
from poweradminbf3 import Poweradminbf3Plugin
from tests.unittests import Bf3TestCase


class Test_config(Bf3TestCase):

    def test_no_preference(self):
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.assertEqual(10, self.p._yell_duration)

    def test_yell_duration_int(self):
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="preferences">
                <set name="yell_duration">1</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.assertEqual(1.0, self.p._yell_duration)

    def test_yell_duration_float(self):
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="preferences">
                <set name="yell_duration">1.3</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.assertEqual(10, self.p._yell_duration)

    def test_yell_duration_too_low(self):
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="preferences">
                <set name="yell_duration">0.3</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.assertEqual(10, self.p._yell_duration)

    def test_yell_duration_junk(self):
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="preferences">
                <set name="yell_duration">foo</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.assertEqual(10, self.p._yell_duration)

    def test_yell_duration_empty(self):
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="preferences">
                <set name="yell_duration"></set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.assertEqual(10, self.p._yell_duration)



class Test_cmd_yell(Bf3TestCase):

    def setUp(self):
        Bf3TestCase.setUp(self)
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="commands">
                <set name="yell">20</set>
            </settings>
            <settings name="preferences">
                <set name="yell_duration">2</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.p.onStartup()


    def test_no_argument(self):
        self.moderator.connects("moderator")
        self.moderator.message_history = []
        self.moderator.says("!yell")
        self.assertEqual(1, len(self.moderator.message_history))
        self.assertEqual('missing parameter, try !help yell', self.moderator.message_history[0])

    def test_nominal(self):
        self.moderator.connects("moderator")
        self.moderator.says("!yell changing map soon !")
        self.console.write.assert_called_once_with(('admin.yell', 'changing map soon !', '2'))



class Test_cmd_yellteam(Bf3TestCase):

    def setUp(self):
        Bf3TestCase.setUp(self)
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="commands">
                <set name="yellteam">20</set>
            </settings>
            <settings name="preferences">
                <set name="yell_duration">2</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.p.onStartup()


    def test_no_argument(self):
        self.moderator.connects("moderator")
        self.moderator.message_history = []
        self.moderator.says("!yellteam")
        self.assertEqual(1, len(self.moderator.message_history))
        self.assertEqual('missing parameter, try !help yellteam', self.moderator.message_history[0])

    def test_nominal(self):
        self.moderator.connects("moderator")
        self.moderator.teamId = 3
        self.moderator.says("!yellteam changing map soon !")
        self.console.write.assert_called_once_with(('admin.yell', 'changing map soon !', '2', 'team', '3'))



class Test_cmd_yellsquad(Bf3TestCase):

    def setUp(self):
        Bf3TestCase.setUp(self)
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="commands">
                <set name="yellsquad">20</set>
            </settings>
            <settings name="preferences">
                <set name="yell_duration">2</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.p.onStartup()


    def test_no_argument(self):
        self.moderator.connects("moderator")
        self.moderator.message_history = []
        self.moderator.says("!yellsquad")
        self.assertEqual(1, len(self.moderator.message_history))
        self.assertEqual('missing parameter, try !help yellsquad', self.moderator.message_history[0])

    def test_nominal(self):
        self.moderator.connects("moderator")
        self.moderator.teamId = 3
        self.moderator.squad = 4
        self.moderator.says("!yellsquad changing map soon !")
        self.console.write.assert_called_once_with(('admin.yell', 'changing map soon !', '2', 'squad', '3', '4'))


class Test_cmd_yellplayer(Bf3TestCase):

    def setUp(self):
        Bf3TestCase.setUp(self)
        self.conf = XmlConfigParser()
        self.conf.loadFromString("""
        <configuration plugin="poweradminbf3">
            <settings name="commands">
                <set name="yellplayer">20</set>
            </settings>
            <settings name="preferences">
                <set name="yell_duration">2</set>
            </settings>
        </configuration>
        """)
        self.p = Poweradminbf3Plugin(self.console, self.conf)
        self.p.onLoadConfig()
        self.p.onStartup()


    def test_no_argument(self):
        self.moderator.connects("moderator")
        self.moderator.message_history = []
        self.moderator.says("!yellplayer")
        self.assertEqual(1, len(self.moderator.message_history))
        self.assertEqual('invalid parameters, try !help yellplayer', self.moderator.message_history[0])

    def test_nominal(self):
        self.joe.connects('joe')
        self.moderator.connects("moderator")
        self.moderator.says("!yellplayer joe changing map soon !")
        self.console.write.assert_called_once_with(('admin.yell', 'changing map soon !', '2', 'player', 'joe'))

