from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.booking.models import Room
from app.db import set_room, get_rooms, delete_room, get_room, update_room


class RoomResource(Resource):
    """
    """
    def get(self):
        body = request.get_json()
        try:
            if body['flag'] == 1:
                result = get_rooms(body)
            elif body['flag'] == 2:
                room_id = body['room_id']
                result = get_room(room_id)
        except KeyError as ex:
            result = ({'msg': 'Flag missing!'}, 404)
        return result

    @jwt_required
    def post(self):
        body = request.get_json()
        room = Room(**body)
        result = set_room(room)
        return result

    @jwt_required
    def put(self):
        body = request.get_json()
        room = Room(**body)
        result = update_room(room)
        return result

    @jwt_required
    def delete(self):
        body = request.get_json()
        room_id = body['room_id']
        result = delete_room(room_id)
        return result

    @jwt_required
    def patch(self):
        body = request.get_json()
        pass