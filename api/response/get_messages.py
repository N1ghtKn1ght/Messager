import datetime

from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto


class ResponseGetMessagesDtoSchema(Schema):
    id = fields.Int()
    sender_id = fields.Int()
    recipient_id = fields.Int()
    message = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @pre_load
    @post_load
    def deserialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = self.datetime_to_iso(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = self.datetime_to_iso(data['updated_at'])
        return data

    @staticmethod
    def datetime_to_iso(dt):
        if isinstance(dt, datetime.datetime):
            return dt.isoformat()
        return dt


class ResponseGetMessagesDto(ResponseDto, ResponseGetMessagesDtoSchema):
    __schema__ = ResponseGetMessagesDtoSchema


