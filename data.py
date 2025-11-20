from typing import Callable, Any


class Data:
    @staticmethod
    def validate_field(data: dict, field_name: str, required_type: type | list, rule: bool | Callable[[Any], bool] = True) -> bool:
        field = data.get(field_name)
        if (field is None):
            return False
        if (isinstance(required_type, type)):
            if not isinstance(field, required_type):
                return False
        else:
            if not any((lambda x: isinstance(field, x))(x) for x in required_type):
                return False
        return isinstance(rule, bool) or rule(field)

    @staticmethod
    def validate_fields(data: dict) -> bool:
        return all([
            Data.validate_field(data, 'algorythm', str,
                              lambda x: x in ['random.randint']),
            Data.validate_field(data, 'seed', [int, str], lambda x: isinstance(
                x, int) or x == 'default'),
            Data.validate_field(data, 'frequency', int, lambda x: x > 0),
            Data.validate_field(data, 'frequency_units', str,
                              lambda x: x in ['s', 'm', 'h']),
            Data.validate_field(data, 'saving', int, lambda x: x > 0),
            Data.validate_field(data, 'saving_units', str,
                              lambda x: x in ['s', 'm', 'h']),
            Data.validate_field(data, 'status', bool),
            Data.validate_field(data, 'time_started', [
                              bool, str], lambda x: isinstance(x, str) or x == False),
            Data.validate_field(data, 'time_ended', [
                              bool, str], lambda x: isinstance(x, str) or x == False)
        ])
