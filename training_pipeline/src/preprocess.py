# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# ruff: noqa: E501

"""Pipeline Preprocessing Step: Train and test text data is tokenized and the targets are encoded"""
import numpy as np
import pandas as pd
import os
import logging

from utils.ml_pipeline_components import MyTokenizer, Encoder


def preprocess():
    logging.info("fetching dataset")
    df_train = pd.read_csv(os.path.join("/opt/ml/processing/input/train", "train.csv"))
    df_test = pd.read_csv(os.path.join("/opt/ml/processing/input/test", "test.csv"))
    df_val = pd.read_csv(os.path.join("/opt/ml/processing/input/val", "val.csv"))

    logging.info("tokenizing dataset")
    tokenizer = MyTokenizer()
    x_train = [tokenizer.tokenize(v) for v in df_train.transcription.values]
    x_test = [tokenizer.tokenize(v) for v in df_test.transcription.values]
    [tokenizer.tokenize(v) for v in df_val.transcription.values]
    encoder = Encoder(df_train, df_test, df_val)
    y_train = [encoder.encode(c) for c in df_train.medical_specialty.values]
    y_test = [encoder.encode(c) for c in df_test.medical_specialty.values]
    [encoder.encode(c) for c in df_val.medical_specialty.values]

    logging.info("saving dataset")

    # save data
    np.save(os.path.join("/opt/ml/processing/output/train", "x_train.npy"), x_train)
    np.save(os.path.join("/opt/ml/processing/output/train", "y_train.npy"), y_train)

    np.save(os.path.join("/opt/ml/processing/output/test", "x_test.npy"), x_test)
    np.save(os.path.join("/opt/ml/processing/output/test", "y_test.npy"), y_test)

    np.save(os.path.join("/opt/ml/processing/output/val", "x_val.npy"), x_test)
    np.save(os.path.join("/opt/ml/processing/output/val", "y_val.npy"), y_test)


if __name__ == "__main__":
    preprocess()
