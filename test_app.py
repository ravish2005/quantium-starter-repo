from app import app


def test_header(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert "Soul Foods Pink Morsel Sales Dashboard" in header.text


def test_graph(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None