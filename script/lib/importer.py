#!/usr/bin/env python

import os

BINARIES = {
  'darwin': [
    'libbookmarks_browser.a',
    'libcomponent_metrics_proto.a',
    'libfavicon_base.a',
    'libgoogle_core_browser.a',
    'libhistory_core_browser.a',
    'libsearch_engines.a',
    'libquery_parser.a',
    'liburl_formatter.a',
  ],
  'linux': [
    'libbookmarks_browser.a',
    'libcomponent_metrics_proto.a',
    'libfavicon_base.a',
    'libgoogle_core_browser.a',
    'libhistory_core_browser.a',
    'libsearch_engines.a',
    'libquery_parser.a',
    'liburl_formatter.a',
  ],
  'win32': [
    os.path.join('obj', 'components', 'bookmakrs_browser.lib'),
    os.path.join('obj', 'components', 'component_metrics_proto.lib'),
    os.path.join('obj', 'components', 'favicon_base.lib'),
    os.path.join('obj', 'components', 'google_core_browser.lib'),
    os.path.join('obj', 'components', 'history_core_browser.lib'),
    os.path.join('obj', 'components', 'search_engines.lib'),
    os.path.join('obj', 'components', 'query_parser.lib'),
    os.path.join('obj', 'components', 'url_formatter.lib'),
  ],
}

INCLUDE_DIRS = [
  'components/bookmarks/browser',
  'components/favicon_base',
  'components/google/core/browser',
  'components/history',
  'components/search_engines',
  'components/query_parser',
  'third_party/protobuf',
]
GENERATED_INCLUDE_DIRS = [
  'components/strings',
  'protoc_out/components/metrics',
]
OTHER_HEADERS = [
]
