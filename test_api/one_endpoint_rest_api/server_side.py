from typing import Union

from one_endpoint_rest_api.data import *
from one_endpoint_rest_api.functions import functions_sequence


def _parsing_dict_to_variables(dict_data: dict):
    """
    Parsing dictionary into operable values
    :param dict_data: dictionary should contain keys 'data' and 'rule'
    returns values: list, keys: list
    """
    try:
        values = dict_data['data']
        keys = dict_data['rule']
        return values, keys
    except ValueError:
        return ValueError
    except KeyError:
        return KeyError


def _rules_check(rules: list):
    """  A simple check whether the rules are valid  """
    unique_rules_list = ['a', 'b', 'c', 'd', 'e', 'f']
    for rule in rules:
        if rule not in unique_rules_list:
            return 1
    return 0


def _numbers_check(numbers_sequence: list):
    """  Checking whether the numbers' sequence contains only integers and float values  """
    for number in numbers_sequence:
        if not isinstance(number, int):
            if not isinstance(number, float):
                return 1
    return 0


def _data_recognizing_and_check(dict_data: dict):
    """  Checking whether the given dict_data contains valid data  """
    numbers, rules = _parsing_dict_to_variables(dict_data)
    if isinstance(numbers, list) and isinstance(rules, list):
        if _rules_check(rules) != 0:
            raise ValueError
        elif _numbers_check(numbers) != 0:
            raise TypeError
        else:
            return numbers, rules
    else:
        raise TypeError


def _data_calculation(number: Union[int, float], rule: str):
    """  Applying a function on a number according to given rule  """
    number = functions_sequence[rule](number)
    return number


def data_processing(dict_data: dict):
    """  Constructing the dictionary response after some simple checks  """
    try:
        raw_list = []
        numbers, rules = _data_recognizing_and_check(dict_data)
        for number in numbers:
            for rule in rules:
                number = _data_calculation(number, rule)
            raw_list.append(number)

        return {'result': raw_list}
    except TypeError:
        return type_error_text
    except ValueError:
        return value_error_text
    except KeyError:
        return key_error_text
    except Exception as error:
        return f'Ann unknown error has appeared, please, check the parameters. {error}'

