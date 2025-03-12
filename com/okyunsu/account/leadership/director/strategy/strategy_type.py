from enum import Enum


class StrategyType(Enum):
    DEFAULT_CREATE = "default_create"
    VALID_CREATE = "valid_create"
    DEFAULT_DELETE = "default_delete"
    SOFT_DELETE = "soft_delete"
    HARD_DELETE = "hard_delete"
    GET_ALL = "get_all"
    GET_DETAIL = "get_detail"
    FULL_UPDATE = "full_update"
    PARTIAL_UPDATE = "partial_update"