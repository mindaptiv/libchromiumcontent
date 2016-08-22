{
  'targets': [
    {
      'target_name': 'importer',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/components/components.gyp:bookmarks_browser',
        '<(DEPTH)/components/components.gyp:component_metrics_proto',
        '<(DEPTH)/components/components.gyp:favicon_base',
        '<(DEPTH)/components/components.gyp:google_core_browser',
        '<(DEPTH)/components/components.gyp:history_core_browser',
        '<(DEPTH)/components/components.gyp:search_engines',
        '<(DEPTH)/components/components.gyp:query_parser',
      ]
    }
  ]
}
