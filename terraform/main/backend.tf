// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
/******************************************
  Remote backend configuration
 *****************************************/

terraform {
  backend "s3" {
    bucket  = "123971416876-operations-terraform"
    key     = "terraform_state"
    region  = "eu-west-3"
    profile = "operations"
  }
}
