"""Tests for the Services model classes."""

#pylint: disable=E1101

import unittest
from requests import HTTPError
from .. import BasePCOVCRTestCase
import pypco

class TestServies(BasePCOVCRTestCase):
    """Test the Services model classes."""

    def test_list_arrangement_sections(self):
        """Verify that we can list arrangement sections."""

        pco = self.pco

        song = pco.services.songs.get("16194010")
        arrangement = [arr for arr in song.rel.arrangements.list()][0]

        sections = [sec for sec in arrangement.rel.sections.list()]

        self.assertGreater(0, len(sections))