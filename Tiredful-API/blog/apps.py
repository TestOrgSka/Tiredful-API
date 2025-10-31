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

DEFAULT_POSTS_PER_PAGE = 10

class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = 'Awesome Blog'

    def ready(self):
        self.posts_per_page_limit = getattr(
            settings, 
            'BLOG_POSTS_PER_PAGE', 
            1000
        )

        if self.posts_per_page_limit > 500:
            pass
