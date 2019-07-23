# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EndpointRegistrationApiModel(Model):
    """Endpoint registration model.

    :param id: Registered identifier of the endpoint
    :type id: str
    :param endpoint_url: Original endpoint url of the endpoint
    :type endpoint_url: str
    :param site_id: Registered site of the endpoint
    :type site_id: str
    :param endpoint: Endpoint information of the registration
    :type endpoint: ~azure-iiot-opc-history.models.EndpointApiModel
    :param security_level: Security level of the endpoint
    :type security_level: int
    :param certificate: Endpoint cert that was registered.
    :type certificate: bytearray
    :param authentication_methods: Supported authentication methods that can
     be selected to
     obtain a credential and used to interact with the endpoint.
    :type authentication_methods:
     list[~azure-iiot-opc-history.models.AuthenticationMethodApiModel]
    """

    _validation = {
        'id': {'required': True},
        'endpoint': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'site_id': {'key': 'siteId', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'EndpointApiModel'},
        'security_level': {'key': 'securityLevel', 'type': 'int'},
        'certificate': {'key': 'certificate', 'type': 'bytearray'},
        'authentication_methods': {'key': 'authenticationMethods', 'type': '[AuthenticationMethodApiModel]'},
    }

    def __init__(self, id, endpoint, endpoint_url=None, site_id=None, security_level=None, certificate=None, authentication_methods=None):
        super(EndpointRegistrationApiModel, self).__init__()
        self.id = id
        self.endpoint_url = endpoint_url
        self.site_id = site_id
        self.endpoint = endpoint
        self.security_level = security_level
        self.certificate = certificate
        self.authentication_methods = authentication_methods
