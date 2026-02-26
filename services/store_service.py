from base.base_test import BaseTest
from constants.endpoints import (
    GET_INVENTORY, PLACE_ORDER, GET_ORDER_BY_ID, DELETE_ORDER
)

class StoreService(BaseTest):

    def get_inventory(self):
        return self.get(GET_INVENTORY)

    def place_order(self, body):
        return self.post(PLACE_ORDER,body)

    def get_order_by_id(self, order_id):
        return self.get(GET_ORDER_BY_ID.format(orderId=order_id))

    def delete_order(self, order_id):
        return self.delete(DELETE_ORDER.format(orderId=order_id))