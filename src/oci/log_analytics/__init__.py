# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import


from .log_analytics_client import LogAnalyticsClient
from .log_analytics_client_composite_operations import LogAnalyticsClientCompositeOperations
from . import models

__all__ = ["LogAnalyticsClient", "LogAnalyticsClientCompositeOperations", "models"]