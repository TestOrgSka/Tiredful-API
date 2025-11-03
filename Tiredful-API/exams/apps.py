# -*- coding: utf-8 -*-
#
#   ____  __  ___   ___  ___  ___  _  _  __       __   ___  __
#  (_  _)(  )(  ,) (  _)(   \(  _)( )( )(  )     (  ) (  ,\(  )
#   )(   )(  )  \  ) _) ) ) )) _) )()(  )(__    /__\  ) _/ )(
#  (__) (__)(_)\_)(___)(___/(_)   \__/ (____)  (_)(_)(_)  (__)
#
#
# Copyright (C) 2017-2018 Payatu Software Labs
# This file is part of Tiredful API application

from __future__ import unicode_literals

from django.apps import AppConfig
from django.conf import settings


class ExamsConfig(AppConfig):
    name = 'exams'
    verbose_name = 'Exams Module'

    def ready(self):
        DEFAULT_MAX_ATTEMPTS = 1000
        self.max_attempts_limit = getattr(
            settings,
            'EXAMS_MAX_ATTEMPTS',
            DEFAULT_MAX_ATTEMPTS
        )
        
        if self.max_attempts_limit > DEFAULT_MAX_ATTEMPTS:
            self.max_attempts_limit = DEFAULT_MAX_ATTEMPTS
