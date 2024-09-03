import argparse
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL or video ID")

def get_transcript(video_id, languages=['en']):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Fetch and display YouTube video transcripts.")
    parser.add_argument('video_url', nargs='+', help="YouTube video URL(s)")
    parser.add_argument('--languages', nargs='+', default=['en'], help="Preferred languages for the transcript")
    parser.add_argument('--save', metavar='FILE', help="Save the transcript to a file")
    parser.add_argument('--no-print', action='store_true', help="Do not print the transcript to the terminal")

    args = parser.parse_args()

    for video_url in args.video_url:
        try:
            video_id = extract_video_id(video_url)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            continue

        transcript = get_transcript(video_id, args.languages)
        transcript_text = "\n".join([entry['text'] for entry in transcript])

        if not args.no_print:
            print(transcript_text)

        if args.save:
            with open(args.save, 'w', encoding='utf-8') as file:
                file.write(transcript_text)
            print(f"Transcript saved to {args.save}")

if __name__ == "__main__":
    main()
