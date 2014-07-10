# Copyright 2014 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""ID Generator provider interface."""

import abc

import six

from keystone.common import dependency
from keystone.common import manager
from keystone import exception


@dependency.provider('id_generator_api')
class Manager(manager.Manager):
    """Default pivot point for the identifier generator backend."""

    def __init__(self):
        # TODO(henry-nash): Use a config option to select the generator driver
        super(Manager, self).__init__(
            'keystone.identity.id_generators.sha256.Generator')


@six.add_metaclass(abc.ABCMeta)
class IDGenerator(object):
    """Interface description for an ID Generator provider."""

    @abc.abstractmethod
    def generate_public_ID(self, mapping):
        """Return a Public ID for the given mapping dict.

        :param dict mapping: The items to be hashed.

        The ID must be reproduceable and no more than 64 chars in length.
        The ID generated should be independant of the order of the items
        in the mapping dict.

        """
        raise exception.NotImplemented()