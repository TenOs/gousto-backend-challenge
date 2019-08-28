from utils import load_csv_data


def test_load_csv_data():
    assert load_csv_data('tests/data/test.csv') == [{
        'Column1': 'value1',
        'Column2': 'value2'
    }]
