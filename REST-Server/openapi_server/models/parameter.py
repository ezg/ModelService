# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Parameter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, type=None, default_value=None, minimum=None, maximum=None, choices=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI

        :param name: The name of this Parameter.  # noqa: E501
        :type name: str
        :param description: The description of this Parameter.  # noqa: E501
        :type description: str
        :param type: The type of this Parameter.  # noqa: E501
        :type type: str
        :param default_value: The default_value of this Parameter.  # noqa: E501
        :type default_value: object
        :param minimum: The minimum of this Parameter.  # noqa: E501
        :type minimum: object
        :param maximum: The maximum of this Parameter.  # noqa: E501
        :type maximum: object
        :param choices: The choices of this Parameter.  # noqa: E501
        :type choices: List
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'type': str,
            'default_value': object,
            'minimum': object,
            'maximum': object,
            'choices': List
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'default_value': 'default_value',
            'minimum': 'minimum',
            'maximum': 'maximum',
            'choices': 'choices'
        }

        self._name = name
        self._description = description
        self._type = type
        self._default_value = default_value
        self._minimum = minimum
        self._maximum = maximum
        self._choices = choices

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Parameter.

        The name of the parameter  # noqa: E501

        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.

        The name of the parameter  # noqa: E501

        :param name: The name of this Parameter.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Parameter.

        Natural language description of parameter  # noqa: E501

        :return: The description of this Parameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parameter.

        Natural language description of parameter  # noqa: E501

        :param description: The description of this Parameter.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this Parameter.

        The parameter's type  # noqa: E501

        :return: The type of this Parameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Parameter.

        The parameter's type  # noqa: E501

        :param type: The type of this Parameter.
        :type type: str
        """
        allowed_values = ["NumberParameter", "ChoiceParameter", "TimeParameter", "GeoParameter", "StringParameter"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def default_value(self):
        """Gets the default_value of this Parameter.

        The parameter's default value. Type depends on the parameter's type.  # noqa: E501

        :return: The default_value of this Parameter.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this Parameter.

        The parameter's default value. Type depends on the parameter's type.  # noqa: E501

        :param default_value: The default_value of this Parameter.
        :type default_value: object
        """

        self._default_value = default_value

    @property
    def minimum(self):
        """Gets the minimum of this Parameter.

        The parameter's minimum allowed value. Type depends on the parameter's type.  # noqa: E501

        :return: The minimum of this Parameter.
        :rtype: object
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this Parameter.

        The parameter's minimum allowed value. Type depends on the parameter's type.  # noqa: E501

        :param minimum: The minimum of this Parameter.
        :type minimum: object
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this Parameter.

        The parameter's maximum allowed value. Type depends on the parameter's type.  # noqa: E501

        :return: The maximum of this Parameter.
        :rtype: object
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this Parameter.

        The parameter's maximum allowed value. Type depends on the parameter's type.  # noqa: E501

        :param maximum: The maximum of this Parameter.
        :type maximum: object
        """

        self._maximum = maximum

    @property
    def choices(self):
        """Gets the choices of this Parameter.

        An array of choices available for a parameter of type ChoiceParameter  # noqa: E501

        :return: The choices of this Parameter.
        :rtype: List
        """
        return self._choices

    @choices.setter
    def choices(self, choices):
        """Sets the choices of this Parameter.

        An array of choices available for a parameter of type ChoiceParameter  # noqa: E501

        :param choices: The choices of this Parameter.
        :type choices: List
        """

        self._choices = choices
