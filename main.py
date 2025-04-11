# ================================================================
# ⚠️ LEGAL DISCLAIMER:
# This script is provided for educational and personal use only.
# Downloading content from Instagram may violate their Terms of Use.
# https://help.instagram.com/581066165581870
#
# This tool is NOT affiliated with Instagram or Meta Platforms.
# You are solely responsible for using it legally and ethically.
# ================================================================

import instaloader
import logging
import os
import re
import argparse
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def sanitize_filename(name: str) -> str:
    name = name.lower()
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = name.strip().replace('\n', ' ')
    name = re.sub(r'\s+', '_', name)  # Replace all whitespace with underscores
    return name

def download_reel(url: str, target_dir: str):
    loader = instaloader.Instaloader(
        download_pictures=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=True,
        post_metadata_txt_pattern="{caption}"
    )

    try:
        if "/reel/" in url or "/p/" in url:
            shortcode = url.split("/")[-2]
        else:
            logging.error("Invalid Instagram URL.")
            return

        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        username = sanitize_filename(post.owner_username)
        caption = post.caption or "no caption"
        clean_caption = sanitize_filename(caption)[:40]

        os.makedirs(target_dir, exist_ok=True)
        loader.download_post(post, target=target_dir)

        timestamp_str = post.date_utc.strftime("%Y-%m-%d_%H-%M-%S_UTC")
        base_old_path = os.path.join(target_dir, timestamp_str)

        old_video = base_old_path + ".mp4"
        old_txt = base_old_path + ".txt"
        old_json = base_old_path + ".json.xz"

        base_filename = f"@{username}-{clean_caption}"
        new_video = os.path.join(target_dir, base_filename + ".mp4")
        new_txt = os.path.join(target_dir, base_filename + "_video_description.txt")

        if os.path.exists(old_video):
            os.rename(old_video, new_video)
            logging.info(f"🎬 Renamed video -> {new_video}")
        else:
            logging.warning(f"Video file not found: {old_video}")

        if os.path.exists(old_txt):
            with open(old_txt, "r", encoding="utf-8") as f:
                original_caption = f.read().strip()

            with open(new_txt, "w", encoding="utf-8") as f:
                f.write(original_caption + "\n\n")
                f.write("This is the original caption from the video creator.")

            os.remove(old_txt)
            logging.info(f"📝 Saved and renamed caption -> {new_txt}")
        else:
            logging.warning(f"Caption file not found: {old_txt}")

        if os.path.exists(old_json):
            os.remove(old_json)
            logging.info(f"🧹 Deleted metadata file: {old_json}")

    except Exception as e:
        logging.error(f"🔥 Download failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram Reels Downloader: clean and precise.")
    parser.add_argument("url", help="Instagram Reel/Post URL")
    parser.add_argument("-o", "--output", default="downloads", help="Output folder")
    args = parser.parse_args()

    download_reel(args.url, args.output)