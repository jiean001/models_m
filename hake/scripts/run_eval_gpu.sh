#!/bin/bash
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

if [ $# != 3 ] ; then
echo "=============================================================================================================="
echo "Please run the script as: "
echo "bash scripts/run_eval_gpu.sh DEVICE_ID DATA_PATH CKPT_PATH"
echo "for example: bash scripts/run_eval_gpu.sh 3 data/wn18rr wn18rr/CKP-120_339.ckpt"
echo "It is better to use absolute path."
echo "=============================================================================================================="
exit 1;
fi

DEVICE_ID=$1
DATA_PATH=$2
CKPT_PATH=$3

if [ -d "eval" ];
then
    rm -rf ./eval
fi
mkdir ./eval

python -u eval.py  \
    --device_id=$DEVICE_ID \
    --data_path=$DATA_PATH \
    --checkpoint_path=$CKPT_PATH \
    > ./eval/eval.log 2>&1 &
