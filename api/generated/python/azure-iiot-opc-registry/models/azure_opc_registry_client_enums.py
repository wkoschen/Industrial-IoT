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

from enum import Enum


class CallbackMethodType(Enum):

    get = "Get"
    post = "Post"
    put = "Put"
    delete = "Delete"


class SecurityMode(Enum):

    best = "Best"
    sign = "Sign"
    sign_and_encrypt = "SignAndEncrypt"
    none = "None"


class ApplicationType(Enum):

    server = "Server"
    client = "Client"
    client_and_server = "ClientAndServer"


class DiscoveryMode(Enum):

    off = "Off"
    local = "Local"
    network = "Network"
    fast = "Fast"
    scan = "Scan"


class CredentialType(Enum):

    none = "None"
    user_name = "UserName"
    x509_certificate = "X509Certificate"
    jwt_token = "JwtToken"


class SecurityAssessment(Enum):

    unknown = "Unknown"
    low = "Low"
    medium = "Medium"
    high = "High"


class EndpointActivationState(Enum):

    deactivated = "Deactivated"
    activated = "Activated"
    activated_and_connected = "ActivatedAndConnected"


class EndpointConnectivityState(Enum):

    connecting = "Connecting"
    not_reachable = "NotReachable"
    busy = "Busy"
    no_trust = "NoTrust"
    certificate_invalid = "CertificateInvalid"
    ready = "Ready"
    error = "Error"


class SupervisorLogLevel(Enum):

    error = "Error"
    information = "Information"
    debug = "Debug"
    verbose = "Verbose"
