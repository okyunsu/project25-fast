from enum import Enum

class CustomerAction(Enum):
    CREATE_CUSTOMER = "create_customer"
    DELETE_CUSTOMER = "delete_customer"
    REMOVE_CUSTOMER = "remove_customer"

    FIND_CUSTOMER = "find_customer"

    GET_ALL_CUSTOMER = "get_all_customer"

    GET_CUSTOMER_BY_ID = "get_customer_by_id"

    UPDATE_CUSTOMER = "update_customer"
    PATCH_CUSTOMER = "patch_customer"
