#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""Moxing adapter for ModelArts"""

import os
from .config import config

_global_sync_count = 0

def get_device_id():
    if config.device_target == "ascend":
        device_id = os.getenv('DEVICE_ID', '0')
    elif config.device_target == "GPU":
        device_id = os.getenv('OMPI_COMM_WORLD_LOCAL_RANK', '0')
    else:
        device_id = 0
    return int(device_id)


def get_device_num():
    if config.device_target == "ascend":
        local_device_num = os.getenv('RANK_SIZE', '1')
    elif config.device_target == "GPU":
        local_device_num = os.getenv('OMPI_COMM_WORLD_SIZE', '1')
    else:
        local_device_num = 1
    return int(local_device_num)


def get_local_device_num():
    if config.device_target == "ascend":
        local_device_num = min(get_device_num, 8)
    elif config.device_target == "GPU":
        local_device_num = os.getenv('OMPI_COMM_WORLD_LOCAL_SIZE', '1')
    else:
        local_device_num = 1
    return int(local_device_num)


def get_rank_id():
    if config.device_target == "ascend":
        global_rank_id = os.getenv('RANK_ID', '0')
    elif config.device_target == "GPU":
        global_rank_id = os.getenv('OMPI_COMM_WORLD_RANK', '0')
    else:
        global_rank_id = 0
    return int(global_rank_id)


def get_job_id():
    job_id = os.getenv('JOB_ID')
    job_id = job_id if job_id != "" else "default"
    return job_id
