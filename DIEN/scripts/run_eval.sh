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

echo "Please run the script as: "
echo "bash scripts/run_eval.sh [DEVICE_ID/CUDA_VISIBLE_DEVICES] [DEVICE_TARGET] [MINDRECORD_PATH] [DATA_PATH] [DATA_TYPE] [CHECKPOINT_PATH]"
echo "for example: bash scripts/run_eval.sh 0 GPU ./dataset_mindrecord ./Books Books ./ckpt"
echo "It is better to use the absolute path.After running the script, the network runs in the background,the log will be generated in ms_log/log_dien_eval.log"
echo "=============================================================================================================="

DEVICE_TARGET=$2

if [ "$DEVICE_TARGET" = "GPU" ]
then
  export CUDA_VISIBLE_DEVICES=$1
fi

if [ "$DEVICE_TARGET" = "Ascend" ];
then
  export DEVICE_ID=$1
fi
MINDRECORD_PATH=$3
DATA_URL=$4
DATA_TYPE=$5
CHECKPOINT_PATH=$6

mkdir -p ms_log
CUR_DIR=`pwd`
export GLOG_log_dir=${CUR_DIR}/ms_log
export GLOG_logtostderr=0

python -u eval.py \
--device_target=$DEVICE_TARGET \
--mindrecord_path=$MINDRECORD_PATH \
--dataset_type=$DATA_TYPE \
--save_checkpoint_path=$CHECKPOINT_PATH \
--dataset_file_path=$DATA_URL > ms_log/log_dien_eval.log 2>&1 &