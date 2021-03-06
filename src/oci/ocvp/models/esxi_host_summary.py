# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EsxiHostSummary(object):
    """
    A summary of the ESXi host.
    """

    #: A constant which can be used with the lifecycle_state property of a EsxiHostSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a EsxiHostSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a EsxiHostSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EsxiHostSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a EsxiHostSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a EsxiHostSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new EsxiHostSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EsxiHostSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this EsxiHostSummary.
        :type display_name: str

        :param sddc_id:
            The value to assign to the sddc_id property of this EsxiHostSummary.
        :type sddc_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EsxiHostSummary.
        :type compartment_id: str

        :param compute_instance_id:
            The value to assign to the compute_instance_id property of this EsxiHostSummary.
        :type compute_instance_id: str

        :param time_created:
            The value to assign to the time_created property of this EsxiHostSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EsxiHostSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EsxiHostSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EsxiHostSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EsxiHostSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'sddc_id': 'str',
            'compartment_id': 'str',
            'compute_instance_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'sddc_id': 'sddcId',
            'compartment_id': 'compartmentId',
            'compute_instance_id': 'computeInstanceId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._sddc_id = None
        self._compartment_id = None
        self._compute_instance_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EsxiHostSummary.
        The `OCID`__ of the ESXi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this EsxiHostSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EsxiHostSummary.
        The `OCID`__ of the ESXi host.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this EsxiHostSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this EsxiHostSummary.
        A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this EsxiHostSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EsxiHostSummary.
        A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this EsxiHostSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def sddc_id(self):
        """
        **[Required]** Gets the sddc_id of this EsxiHostSummary.
        The `OCID`__ of the SDDC that the
        ESXi host belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sddc_id of this EsxiHostSummary.
        :rtype: str
        """
        return self._sddc_id

    @sddc_id.setter
    def sddc_id(self, sddc_id):
        """
        Sets the sddc_id of this EsxiHostSummary.
        The `OCID`__ of the SDDC that the
        ESXi host belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sddc_id: The sddc_id of this EsxiHostSummary.
        :type: str
        """
        self._sddc_id = sddc_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this EsxiHostSummary.
        The `OCID`__ of the compartment that
        contains the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this EsxiHostSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EsxiHostSummary.
        The `OCID`__ of the compartment that
        contains the SDDC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this EsxiHostSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compute_instance_id(self):
        """
        Gets the compute_instance_id of this EsxiHostSummary.
        In terms of implementation, an ESXi host is a Compute instance that
        is configured with the chosen bundle of VMware software. The `computeInstanceId`
        is the `OCID`__ of that Compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compute_instance_id of this EsxiHostSummary.
        :rtype: str
        """
        return self._compute_instance_id

    @compute_instance_id.setter
    def compute_instance_id(self, compute_instance_id):
        """
        Sets the compute_instance_id of this EsxiHostSummary.
        In terms of implementation, an ESXi host is a Compute instance that
        is configured with the chosen bundle of VMware software. The `computeInstanceId`
        is the `OCID`__ of that Compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compute_instance_id: The compute_instance_id of this EsxiHostSummary.
        :type: str
        """
        self._compute_instance_id = compute_instance_id

    @property
    def time_created(self):
        """
        Gets the time_created of this EsxiHostSummary.
        The date and time the ESXi host was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EsxiHostSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EsxiHostSummary.
        The date and time the ESXi host was created, in the format defined by
        `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EsxiHostSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EsxiHostSummary.
        The date and time the ESXi host was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this EsxiHostSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EsxiHostSummary.
        The date and time the ESXi host was updated, in the format defined by
        `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this EsxiHostSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this EsxiHostSummary.
        The current state of the ESXi host.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EsxiHostSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EsxiHostSummary.
        The current state of the ESXi host.


        :param lifecycle_state: The lifecycle_state of this EsxiHostSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this EsxiHostSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this EsxiHostSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EsxiHostSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this EsxiHostSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this EsxiHostSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this EsxiHostSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EsxiHostSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this EsxiHostSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
