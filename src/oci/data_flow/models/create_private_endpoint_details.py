# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePrivateEndpointDetails(object):
    """
    The create private endpoint details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePrivateEndpointDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePrivateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this CreatePrivateEndpointDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreatePrivateEndpointDetails.
        :type display_name: str

        :param dns_zones:
            The value to assign to the dns_zones property of this CreatePrivateEndpointDetails.
        :type dns_zones: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePrivateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param max_host_count:
            The value to assign to the max_host_count property of this CreatePrivateEndpointDetails.
        :type max_host_count: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreatePrivateEndpointDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this CreatePrivateEndpointDetails.
        :type subnet_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'dns_zones': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'max_host_count': 'int',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'dns_zones': 'dnsZones',
            'freeform_tags': 'freeformTags',
            'max_host_count': 'maxHostCount',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._dns_zones = None
        self._freeform_tags = None
        self._max_host_count = None
        self._nsg_ids = None
        self._subnet_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePrivateEndpointDetails.
        The OCID of a compartment.


        :return: The compartment_id of this CreatePrivateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePrivateEndpointDetails.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this CreatePrivateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreatePrivateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreatePrivateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this CreatePrivateEndpointDetails.
        A user-friendly description. Avoid entering confidential information.


        :return: The description of this CreatePrivateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePrivateEndpointDetails.
        A user-friendly description. Avoid entering confidential information.


        :param description: The description of this CreatePrivateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this CreatePrivateEndpointDetails.
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.


        :return: The display_name of this CreatePrivateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePrivateEndpointDetails.
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this CreatePrivateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def dns_zones(self):
        """
        **[Required]** Gets the dns_zones of this CreatePrivateEndpointDetails.
        An array of DNS zone names.
        Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`


        :return: The dns_zones of this CreatePrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this CreatePrivateEndpointDetails.
        An array of DNS zone names.
        Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`


        :param dns_zones: The dns_zones of this CreatePrivateEndpointDetails.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePrivateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreatePrivateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePrivateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreatePrivateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def max_host_count(self):
        """
        Gets the max_host_count of this CreatePrivateEndpointDetails.
        The maximum number of hosts to be accessed through the private endpoint. This value is used
        to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
        multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
        to 512.


        :return: The max_host_count of this CreatePrivateEndpointDetails.
        :rtype: int
        """
        return self._max_host_count

    @max_host_count.setter
    def max_host_count(self, max_host_count):
        """
        Sets the max_host_count of this CreatePrivateEndpointDetails.
        The maximum number of hosts to be accessed through the private endpoint. This value is used
        to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
        multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
        to 512.


        :param max_host_count: The max_host_count of this CreatePrivateEndpointDetails.
        :type: int
        """
        self._max_host_count = max_host_count

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreatePrivateEndpointDetails.
        An array of network security group OCIDs.


        :return: The nsg_ids of this CreatePrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreatePrivateEndpointDetails.
        An array of network security group OCIDs.


        :param nsg_ids: The nsg_ids of this CreatePrivateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreatePrivateEndpointDetails.
        The OCID of a subnet.


        :return: The subnet_id of this CreatePrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreatePrivateEndpointDetails.
        The OCID of a subnet.


        :param subnet_id: The subnet_id of this CreatePrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other