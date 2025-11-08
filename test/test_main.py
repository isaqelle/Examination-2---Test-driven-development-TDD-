from unittest.mock import patch, MagicMock

from src import main as main_module  # adjust import path if needed


@patch("src.main.Game")
def test_main_calls_game_run(mock_game_class):
    """Test that main() creates a Game instance and calls run()."""
    mock_game_instance = MagicMock()
    mock_game_class.return_value = mock_game_instance

    main_module.main()

    # Verify Game() was instantiated
    mock_game_class.assert_called_once()
    # Verify run() was called on that instance
    mock_game_instance.run.assert_called_once()
