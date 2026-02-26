
#Pet Endpoints
ADD_PET = "/pet"
UPDATE_PET = "/pet"
GET_PET_BY_STATUS = "/pet/findByStatus"
GET_PET_BY_ID = "/pet/{petId}"
UPDATE_PET_BY_ID = "/pet/{petId}"
DELETE_PET = "/pet/{petId}"

#Store Endpoints
GET_INVENTORY = "/store/inventory"
PLACE_ORDER = "/store/order"
GET_ORDER_BY_ID = "/store/order/{orderId}"
DELETE_ORDER = "/store/order/{orderId}"

#User Endpoints
CREATE_USER = "/user"
LOGIN_USER = "/user/login"
LOGOUT_USER = "/user/logout"
GET_USER = "/user/{username}"
UPDATE_USER = "/user/{username}"
DELETE_USER = "/user/{username}"