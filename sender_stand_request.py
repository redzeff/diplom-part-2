import config
import data
import requests
def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_NEW_ORDER,
                         json=body)
def get_order_track():
    track = post_new_order(data.order_body).json()["track"]
    return track
def get_order_by_track():
    return requests.get(config.URL_SERVICE + config.ORDER_BY_NUMBER + str(get_order_track()))

