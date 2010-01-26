#  Copyright 2008-2009 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org:licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


class ContentAssister(object):

    def __init__(self, lib_cache, res_cache, var_cache):
        self._lib_cache = lib_cache
        self._res_cache = res_cache
        self._var_cache = var_cache

    def content_assist_values(self, item, value):
        return item.content_assist_values() + \
               self._lib_cache.get_default_keywords()

