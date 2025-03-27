import lightgbm as lgb
import numpy as np
params = {
    "objective": "binary",
    "num_trees": 10
}

bst = lgb.train(
    train_set=lgb.Dataset("binary.train"),
    params=params
)
bst.save_model("LightGBM-python-model.txt")
