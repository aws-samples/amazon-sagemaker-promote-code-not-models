# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""A class for reading and listing AWS profiles from a user profile file."""


class UserProfiles:
    def __init__(self, path="profiles.conf") -> None:
        self.profiles = {}
        with open(path, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                self.profiles[key.strip()] = int(value.strip())

    def list_profiles(self):
        return self.profiles.keys()

    def get_profile_id(self, profile_name: str) -> str:
        return self.profiles[profile_name]

    def get_profile_name(self, profile_id: str) -> str:
        for key, val in self.profiles.items():
            if val == profile_id:
                return key

        raise ValueError(f"Profile with id: '{profile_id}' not found")
