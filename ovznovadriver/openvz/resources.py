# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2014 Rackspace
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo.config import cfg

from nova.openstack.common import log as logging

__openvz_resource_opts = [
    cfg.BoolOpt('ovz_use_cpuunit',
                default=True,
                help='Use OpenVz cpuunits for guaranteed minimums'),
    cfg.BoolOpt('ovz_use_cpulimit',
                default=True,
                help='Use OpenVz cpulimit for maximum cpu limits'),
    cfg.BoolOpt('ovz_use_cpus',
                default=True,
                help='Use OpenVz cpus for max cpus '
                     'available to the container'),
    cfg.BoolOpt('ovz_use_ioprio',
                default=True,
                help='Use IO fair scheduling'),
    ]

CONF = cfg.CONF
CONF.register_opts(__openvz_resource_opts)

LOG = logging.getLogger(__name__)


class ResourceManager(object):
    """Manage OpenVz container resources

    Meant to be a collection of class_methods that will decide/calculate
    resource configs apply them through the Container class"""


    def __init__(self, virtapi):
        """Requires virtapi (api to conductor) to get flavor info"""
        self.virtapi = virtapi

    def _get_flavor_info(self, context, flavor_id):
        """Get the latest flavor info which contains extra_specs"""
        # instnace_type refers to the flavor
        return self.virtapi.flavor_get(context, flavor_id)

    @classmethod
    def setup_memory(cls, context, container, requested_flavor_id):
        """
        """
        instance_type = cls._get_flavor_info(context, requested_flavor_id)

    @classmethod
    def setup_cpu(cls, context, container, requested_flavor_id):
        """
        """
        instance_type = cls._get_flavor_info(context, requested_flavor_id)

    @classmethod
    def setup_networking(cls, context, container, requested_flavor_id):
        """
        """
        instance_type = cls._get_flavor_info(context, requested_flavor_id)


class VswapResourceManager(object):
    """Vswap method of managing resources"""
    pass


class UBCResourceManager(object):
    """User Bean Counters method of managing resources"""
    pass