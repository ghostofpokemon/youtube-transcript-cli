import unittest
from unittest.mock import patch
from youtube_transcript_cli.cli import main, extract_video_id, get_transcript
import argparse

class TestYouTubeTranscriptCLI(unittest.TestCase):

    def test_extract_video_id(self):
        url = "https://www.youtube.com/watch?v=Y-KztRvRyl0"
        self.assertEqual(extract_video_id(url), "Y-KztRvRyl0")

    @patch('youtube_transcript_cli.cli.YouTubeTranscriptApi.get_transcript')
    def test_get_transcript(self, mock_get_transcript):
        video_id = "Y-KztRvRyl0"
        mock_get_transcript.return_value = [{'text': 'Hello', 'start': 0, 'duration': 5}]
        transcript = get_transcript(video_id)
        self.assertEqual(transcript, [{'text': 'Hello', 'start': 0, 'duration': 5}])

    @patch('sys.stdout')
    @patch('youtube_transcript_cli.cli.get_transcript')
    def test_main_function(self, mock_get_transcript, mock_stdout):
        mock_get_transcript.return_value = [{'text': 'Hello', 'start': 0, 'duration': 5}]
        with patch('argparse.ArgumentParser.parse_args') as mock_args:
            mock_args.return_value = argparse.Namespace(
                video_url=["https://www.youtube.com/watch?v=Y-KztRvRyl0"],
                languages=['en'],
                save=None,
                no_print=False
            )
            main()
        mock_get_transcript.assert_called_once_with("Y-KztRvRyl0", ['en'])

if __name__ == '__main__':
    unittest.main()
