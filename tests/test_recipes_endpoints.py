from starlette.testclient import TestClient


def test_get_by_id(test_client: TestClient):
    result = test_client.get('/recipes/1')
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['id'] == 1


def test_get_by_id_not_found(test_client: TestClient):
    result = test_client.get('/recipes/999')
    json_response = result.json()

    assert result.status_code == 404
    assert json_response['error']['error_id'] == 'RecipeNotFoundException'
    assert json_response['error']['status_code'] == 404


def test_update_by_id(test_client: TestClient):
    result = test_client.patch('/recipes/1', json={'title': 'test'})
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['id'] == 1
    assert json_response['title'] == 'test'


def test_update_by_id_not_found(test_client: TestClient):
    result = test_client.patch('/recipes/999', json={'title': 'test'})
    json_response = result.json()

    assert result.status_code == 404
    assert json_response['error']['error_id'] == 'RecipeNotFoundException'
    assert json_response['error']['status_code'] == 404


def test_search(test_client: TestClient):
    result = test_client.get('/recipes', params={'cuisine': 'british'})
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['total'] == 4
    assert json_response['next_offset'] is None
    assert len(json_response['data']) == 4


def test_search_no_results(test_client: TestClient):
    result = test_client.get('/recipes', params={'cuisine': 'no-result'})
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['total'] == 0
    assert json_response['next_offset'] is None
    assert len(json_response['data']) == 0


def test_search_pagination_beginning(test_client: TestClient):
    result = test_client.get(
        '/recipes',
        params={
            'cuisine': 'british',
            'nb': 2,
        }
    )
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['total'] == 4
    assert json_response['next_offset'] == 2
    assert len(json_response['data']) == 2


def test_search_pagination_middle(test_client: TestClient):
    result = test_client.get(
        '/recipes',
        params={
            'cuisine': 'british',
            'nb': 1,
            'offset': 1
        }
    )
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['total'] == 4
    assert json_response['next_offset'] == 2
    assert len(json_response['data']) == 1


def test_search_pagination_end(test_client: TestClient):
    result = test_client.get(
        '/recipes',
        params={
            'cuisine': 'british',
            'nb': 2,
            'offset': 2
        }
    )
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['total'] == 4
    assert json_response['next_offset'] is None
    assert len(json_response['data']) == 2


def test_search_pagination_end_nb_greater_than_total(test_client: TestClient):
    result = test_client.get(
        '/recipes',
        params={
            'cuisine': 'british',
            'nb': 10,
            'offset': 2
        }
    )
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['total'] == 4
    assert json_response['next_offset'] is None
    assert len(json_response['data']) == 2


def test_search_pagination_end_offset_greater_than_total(
        test_client: TestClient
):
    result = test_client.get(
        '/recipes',
        params={
            'cuisine': 'british',
            'nb': 2,
            'offset': 4
        }
    )
    json_response = result.json()

    assert result.status_code == 200
    assert json_response['total'] == 4
    assert json_response['next_offset'] is None
    assert len(json_response['data']) == 0
