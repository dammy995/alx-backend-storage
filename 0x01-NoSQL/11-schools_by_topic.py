#!/usr/bin/env python3
"""returns the list of school having a specific topic:"""


def schools_by_topic(mongo_collection, topic):
    """returns a list matching topic"""
    return list(mongo_collection.find({"topics": topic}))
