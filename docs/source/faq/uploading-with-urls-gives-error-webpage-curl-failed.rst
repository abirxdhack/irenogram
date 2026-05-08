Uploading with URLs gives error WEBPAGE_CURL_FAILED
---------------------------------------------------

This error means Telegram's servers were unable to fetch the file from the URL you provided.
Common reasons:

- The URL is behind a login wall, CAPTCHA, or Cloudflare protection.
- The server is blocking Telegram's IP ranges.
- The URL returns a redirect that Telegram does not follow.
- The file at the URL is too large for Telegram's downloader.

Solution: Download the file locally and upload it directly instead of passing a URL.
