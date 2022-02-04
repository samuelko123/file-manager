from file_manager.publisher import Publisher


def test_attach_notify(mocker):
    # Arrange
    p = Publisher()
    topic = "Test Topic 1"

    # Action
    fn = mocker.Mock()
    p.attach(topic, fn)
    p.notify(topic, test_arg="Hello World")

    # Assert
    assert len(p._observers[topic]) == 1
    fn.assert_called_once_with(test_arg="Hello World")


def test_detach(mocker):
    # Arrange
    p = Publisher()
    topic = "Test Topic 2"

    # Action
    fn = mocker.Mock()
    p.attach(topic, fn)
    p.detach(topic, fn)
    p.notify(topic, test_arg="Hello World")

    # Assert
    assert len(p._observers[topic]) == 0
    fn.assert_not_called()
