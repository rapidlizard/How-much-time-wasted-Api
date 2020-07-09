import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.transformers import User_transformer
from models.user import User

def test_user_transformer_turns_json_dict_into_user_obj():
    data = {
        'name': 'jeff',
        'img': 'img',
        'url': 'url',
        'created': 'now'
    }
    expected = User_transformer().transform(data)
    assert type(expected) == User