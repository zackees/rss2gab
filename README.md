# rss2gab
Takes an RSS feed and auto posts to gab


# Api investigation

## Posting
Looks like it's hitting this api endpoint:

  * Request URL: https://gab.com/api/v1/statuses
  * Request method: POST
  * status code: 200
  * referrer Policy: origin

:authority: gab.com
:method: POST
:path: /api/v1/statuses
:scheme: https
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
authorization: Bearer CaPMDbAuGjnFe1tfEkZdWvpneDMZm602PikEzhi3JRc
content-length: 225
content-type: application/json;charset=UTF-8
cookie: __cfruid=c463f36313344d8a197490ff6303f649b3e58fa6-1650816554; cf_clearance=HyW.p8Npda2PGihXYFCtltvPaJ2rF4eSlrxqrErO5p8-1650818551-0-150; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczFOemt3TkRBelhTd2laa3RxY0hnM1IwMXlUSGg2YVdWWlMwUjJSak1pTENJeE5qVXdPVEF5T1RFeExqRTFOemcwTWpJaVhRPT0iLCJleHAiOiIyMDIzLTA0LTI1VDE2OjA4OjMxLjE1N1oiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--334e883635154a3cec6295c7e8f24b6fdc223091; _session_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqVXpNakF4TVRGa09ETTVNV1F4WkRGbE1UQXlNamRrTm1Fd01USTVaalppSWc9PSIsImV4cCI6IjIwMjMtMDQtMjVUMTY6MTc6NTkuMTE0WiIsInB1ciI6ImNvb2tpZS5fc2Vzc2lvbl9pZCJ9fQ%3D%3D--20a012ac92de134815ad9ac4d53b0fde7e7663b3; _gabsocial_session=Bw8FtFULBS7%2FLZbEfb8NDIj0KFoLwPPfFKY3OgH5xcMZ2FuMC1U6bWYWj4jYvPAUHRiQv%2BhkGwHJxz2YSeSEQHVKbBd0WnHdqhESkdDOCxG7yB6HhFiBP8RXRx4Z75KYXdQKAebDjz%2FfjZyL0qDimQNpiWwOE3Oa7iUFEzJuvGjmwZsHnobgnsQjgTwmuyJVE4S0GHeomBIDCYRjgm680Zr4g5Xl9D0uWjPMS7iEUjFajVQQdL4XJa2AbSPPLcyBNcCr%2FEaCV7xK9lwvRD52kJrbrXmuf%2FABZTMExd8%2B0F%2B8DU6hbYOqyquGZLCJygMmaoYFYkQ06uKtVKh5OCblfaxJHyIhxMFWP8XJW0nFEf9gWdCfdE271ZZQJa%2BWl3FXh7O69FgAC33KwrxMb004k6ODgSo%2F02UzFZJgANoLseKl1lmgTvNM%2FfWolPQdBALpFCN2pIQon0tOJ%2F1zqGIi1Xbx2PUDu2sT5FDAAsAcI8EZKCLfhlP8IpYKcfxrpwGK3fLIo1w1w67AgTvOO%2B5KKAkZfxBJTu%2BSBkFiUe8Nb%2FMYWSeAxdb63531hGGxwhbU7mSmbOaVbTwGLDIxXN5Jw6lgLWM%3D--ktkrP3KxhAXFjxc5--gJx2TN%2BkOZhrcBlqUdmQGQ%3D%3D
idempotency-key: 55204daf-4bf9-4493-b5df-22b8374c3bda
origin: https://gab.com
referer: https://gab.com/
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
sec-gpc: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36
x-csrf-token: 8/3OnmZjvU2aenyNDNP3jNLNPkmkuAFqouIhcS1BnC/VLQrd59zcEdLS8F4Yo51f9fyTrAiWIKZuXWNDd1kUtw==

Payload:

{
    "status": "test post",
    "expires_at": null,
    "scheduled_at": null,
    "isPrivateGroup": false,
    "in_reply_to_id": null,
    "quote_of_id": null,
    "media_ids": [],
    "sensitive": false,
    "spoiler_text": "",
    "visibility": "public",
    "poll": null,
    "group_id": null
}