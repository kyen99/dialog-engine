from dataclasses import dataclass
from marshmallow import Schema, fields, post_load


class InboundCommandType:
    INBOUND_SMS = "INBOUND_SMS"
    START_DRILL = "START_DRILL"
    TRIGGER_REMINDER = "TRIGGER_REMINDER"


@dataclass
class InboundCommand:
    command_type: InboundCommandType
    sequence_number: str
    payload: dict


class InboundCommandSchema(Schema):
    command_type = fields.Str(required=True)
    sequence_number = fields.Str(required=True)
    payload = fields.Dict(required=True)

    @post_load
    def make_sms(self, data, **kwargs):
        return InboundCommand(**data)
