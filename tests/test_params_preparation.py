def test_one_level(b24):
    params = {"fruit": "apple"}
    param_string = b24._prepare_params(params)
    assert param_string == "fruit=apple&"


def test_one_level_several_items(b24):
    params = {"fruit": "apple", "vegetable": "broccoli"}
    param_string = b24._prepare_params(params)
    assert param_string == "fruit=apple&vegetable=broccoli&"


def test_multi_level(b24):
    params = {"fruit": {"citrus": "lemon"}}
    param_string = b24._prepare_params(params)
    assert param_string == "fruit[citrus]=lemon&"


def test_multi_level_deep(b24):
    params = {"root": {"level 1": {"level 2": {"level 3": "value"}}}}
    param_string = b24._prepare_params(params)
    assert param_string == "root[level 1][level 2][level 3]=value&"


def test_list_dict_mixed(b24):
    params = {"root": {"level 1": [{"list_d 1": "value 1"}, {"list_d 2": "value 2"}]}}
    param_string = b24._prepare_params(params)
    assert param_string == "root[level 1][0][list_d 1]=value 1&root[level 1][1][list_d 2]=value 2&"


def test_multi_level_several_items(b24):
    params = {"fruit": {"citrus": "lemon", "sweet": "apple"}}
    param_string = b24._prepare_params(params)
    assert param_string == "fruit[citrus]=lemon&fruit[sweet]=apple&"


def test_list(b24):
    params = {"fruit": ["lemon", "apple"]}
    param_string = b24._prepare_params(params)
    assert param_string == "fruit[0]=lemon&fruit[1]=apple&"


def test_tuple(b24):
    params = {"fruit": ("lemon", "apple")}
    param_string = b24._prepare_params(params)
    assert param_string == "fruit[0]=lemon&fruit[1]=apple&"


def test_string(b24):
    param_string = b24._prepare_params("")
    assert param_string == ""
