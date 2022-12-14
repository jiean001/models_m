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

DATA_DIR=$1
OUT_DATA_DIR=$2
DATASET_TYPE=$3

dir="../output"
if [ ! -d "$dir" ];then
mkdir $dir
fi

python ../create_dataset.py --data_dir $DATA_DIR --out_data_dir $OUT_DATA_DIR --datasetType $DATASET_TYPE &> ../output/data_process_log &

