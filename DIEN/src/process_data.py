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

"""process_data"""

import sys
import random
import ast

def process_meta(file):
    """process meta"""
    fi = open(file, "r")
    fo = open("item-info", "w")
    for line in fi:
        obj = ast.literal_eval(line)
        cat = obj["categories"][0][-1]
        print(obj["asin"] + "\t" + cat, file=fo)


def process_reviews(file):
    """process reviews"""
    fi = open(file, "r")
    user_map = {}
    fo = open("reviews-info", "w")
    user_map = user_map
    for line in fi:
        obj = ast.literal_eval(line)
        userID = obj["reviewerID"]
        itemID = obj["asin"]
        rating = obj["overall"]
        time = obj["unixReviewTime"]
        print(userID + "\t" + itemID + "\t" + str(rating) + "\t" + str(time), file=fo)


def manual_join():
    """manual join"""
    f_rev = open("reviews-info", "r")
    user_map = {}
    item_list = []
    for line in f_rev:
        line = line.strip()
        items = line.split("\t")
        if items[0] not in user_map:
            user_map[items[0]] = []
        user_map[items[0]].append(("\t".join(items), float(items[-1])))
        item_list.append(items[1])
    f_meta = open("item-info", "r")
    meta_map = {}
    for line in f_meta:
        arr = line.strip().split("\t")
        if arr[0] not in meta_map:
            meta_map[arr[0]] = arr[1]
            arr = line.strip().split("\t")
    fo = open("jointed-new", "w")
    for key in user_map:
        sorted_user_bh = sorted(user_map[key], key=lambda x: x[1])
        for line, t in sorted_user_bh:
            t = t
            items = line.split("\t")
            asin = items[1]
            j = 0
            while True:
                asin_neg_index = random.randint(0, len(item_list) - 1)
                asin_neg = item_list[asin_neg_index]
                if asin_neg == asin:
                    continue
                items[1] = asin_neg
                print("0" + "\t" + "\t".join(items) + "\t" + meta_map[asin_neg], file=fo)
                j += 1
                if j == 1:
                    break
            if asin in meta_map:
                print("1" + "\t" + line + "\t" + meta_map[asin], file=fo)
            else:
                print("1" + "\t" + line + "\t" + "default_cat", file=fo)


def split_test():
    """split test"""
    fi = open("jointed-new", "r")
    fo = open("jointed-new-split-info", "w")
    user_count = {}
    for line in fi:
        line = line.strip()
        user = line.split("\t")[1]
        if user not in user_count:
            user_count[user] = 0
        user_count[user] += 1
    fi.seek(0)
    i = 0
    last_user = "A26ZDKC53OP6JD"
    for line in fi:
        line = line.strip()
        user = line.split("\t")[1]
        if user == last_user:
            if i < user_count[user] - 2:  # 1 + negative samples
                print("20180118" + "\t" + line, file=fo)
            else:
                print("20190119" + "\t" + line, file=fo)
        else:
            last_user = user
            i = 0
            if i < user_count[user] - 2:
                print("20180118" + "\t" + line, file=fo)
            else:
                print("20190119" + "\t" + line, file=fo)
        i += 1


process_meta(sys.argv[1])
process_reviews(sys.argv[2])
manual_join()
split_test()
