#!/usr/bin/env python
# -*- coding: utf8 -*-

# My imports
from unittest import TestCase
import dinnerPlanner


class TestCase(TestCase):
    def test_recipies(self):
        recipies = dinnerPlanner.main(list_ingredients=True)
        self.assertTrue(isinstance(recipies, dict))
