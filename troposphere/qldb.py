# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 6.1.0


from . import AWSObject
from troposphere import Tags
from .validators import boolean


class Ledger(AWSObject):
    resource_type = "AWS::QLDB::Ledger"

    props = {
        'DeletionProtection': (boolean, False),
        'Name': (basestring, False),
        'PermissionsMode': (basestring, True),
        'Tags': (Tags, False),
    }
