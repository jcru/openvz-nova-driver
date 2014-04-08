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
    cfg.BoolOpt('ovz_use_ubc',
                default=True,
                help='Use OpenVz Vswap memory management model instead of '
                     'User BeanCounters'),
    ]

CONF = cfg.CONF
CONF.register_opts(__openvz_resource_opts)

LOG = logging.getLogger(__name__)


class ResourceManager(object):
    """Manage OpenVz container resources

    Meant to be a collection of class_methods that will decide/calculate
    resource configs and apply them through the Container class"""


    def __init__(self, virtapi):
        """Requires virtapi (api to conductor) to get flavor info"""
        self.virtapi = virtapi

    def _get_flavor_info(self, context, flavor_id):
        """Get the latest flavor info which contains extra_specs"""
        # instnace_type refers to the flavor (what you see in flavor list)
        return self.virtapi.flavor_get(context, flavor_id)

    @classmethod
    def configure_container_resources(cls, context, container,
                                      requested_flavor_id):
        instance_type = self._get_flavor_info(context, requested_flavor_id)

        instance_memory_mb = instance_type.get('memory_mb')
        instance_vcpus = instance_type.get('vcpus')
        instance_root_gb = instance_type.get('root_gb')




    def _setup_memory(cls, container, instance_type):
        """
        """
        if CONF.ovz_use_ubc:
            cls._setup_memory_with_ubc(instance_type, container)
            return

        cls._setup_memory_with_vswap(container, instance_type)

    def _setup_memory_with_ubc(cls, container, instance_type):
        instance_memory_mb = instance_type.get('memory_mb')

        instance_memory_bytes = ((instance_memory_mb * 1024) * 1024)
        instance_memory_pages = self._calc_pages(instance_memory_mb)

        container.set_vmguarpages(instance_memory_pages)
        container.set_privvmpages(instance_memory_pages)
        container.set_kmemsize(instance_memory_bytes)

    def _setup_memory_with_vswap(cls, container, instance_type):
        memory = int(instance_type.memory_mb)
        swap = instance_type.extra_specs.get('vswap', None)

        # If no swap has been setup under the flavor extra specs then calculate
        # double the amount of RAM (this is really bad for large flavor sizes)
        if not swap:
            swap = memory * 2

        container.set_vswap(instance, memory, swap)

    def _setup_cpu(cls, container, instance_type):
        """
        """
        pass

    def _setup_networking(cls, container, instance_type):
        """
        """
        pass


class VswapResourceManager(object):
    """Vswap method of managing resources"""
    pass


class UBCResourceManager(object):
    """User Bean Counters method of managing resources"""
    pass
