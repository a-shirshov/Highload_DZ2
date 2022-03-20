#!/usr/bin/env python3

import re
import sys
import socket
from http import client as httplib
import unittest

arg_host = "localhost"
arg_port = 80
if len(sys.argv) > 1:
  arg_host = sys.argv[1]
if len(sys.argv) > 2:
  arg_port = int(sys.argv[2])

class HttpServer(unittest.TestCase):
  host = arg_host
  port = arg_port

  def setUp(self):
    self.conn = httplib.HTTPConnection(self.host, self.port, timeout=10)

  def tearDown(self):
    self.conn.close()

  def test_index_not_found(self):
    """directory index file absent"""
    self.conn.request("GET", "/httptest/dir1/")
    r = self.conn.getresponse()
    _ = r.read()
    self.assertEqual(int(r.status), 403)

loader = unittest.TestLoader()
suite = unittest.TestSuite()
a = loader.loadTestsFromTestCase(HttpServer)
suite.addTest(a)


class NewResult(unittest.TextTestResult):
  @staticmethod
  def get_description(test):
    doc_first_line = test.shortDescription()
    return doc_first_line or ""


class NewRunner(unittest.TextTestRunner):
  resultclass = NewResult


runner = NewRunner(verbosity=2)
runner.run(suite)