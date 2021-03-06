#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
import mq_http_aliyun_sdk.pkg_info

if sys.version_info <= (2, 5):
    sys.stderr.write("ERROR: mq python sdk requires Python Version 2.5 or above.\n")
    sys.stderr.write("Your Python version is %s.%s.%s.\n" % sys.version_info[:3])
    sys.exit(1)

setup(name=mq_http_aliyun_sdk.pkg_info.name,
      version=mq_http_aliyun_sdk.pkg_info.version,
      author="ahrli",
      author_email="ahrli_c@163.com",
      url=mq_http_aliyun_sdk.pkg_info.url,
      packages=["mq_http_aliyun_sdk"],
      license=mq_http_aliyun_sdk.pkg_info.license,
      description=mq_http_aliyun_sdk.pkg_info.short_description,
      long_description=mq_http_aliyun_sdk.pkg_info.long_description)











