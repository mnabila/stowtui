#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from typing import List

from stowtui.template_interface.FileManagerTui import FileManagerTUI
from stowtui.helpers.meta import Version
from stowtui.helpers.meta import app_name


class StowApp(npyscreen.NPSAppManaged):

    def onStart(self):

        quit_s = '\t' * 3 + '^Q to quit'
        version = Version()
        name = app_name().capitalize

        self.addForm(
            "MAIN",
            FileManagerTUI,
            name=name + '\t' + version + quit_s,
        )
