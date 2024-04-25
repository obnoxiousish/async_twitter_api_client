from asyncTwitter.asyncAccount import AsyncAccount
from asyncTwitter.asyncSearch import AsyncSearch
from anyio import run


async def testSearch():
    search = AsyncSearch(debug=True)
    await search.asyncAuthenticate(
        cookies="C:/Users/a/Documents/Git/infiniteMoneyTwitterBot/cookies/obJellyfin.cookies"
    )
    results = await search.asyncRun(
        queries=[{"query": "kanye west", "category": "Top"}],
        limit=100,
        out="data/search_results",
    )
    results = results [0]
    print(f'Found {len(results)}')


async def testAccount():
    twitter = AsyncAccount()

    # cookies = {
    #    "ct0": "b6e7f4a7c7b0f8d3b6e7f4a7c7b0f8d329t3i4320t9u432t902t430932ty4902u3t923tu329tu32t9u",
    #    "auth_token": "egfwiopjgew90pgj4w9gugh89u0f",
    # }

    await twitter.asyncAuthenticate(
        cookies="C:/Users/a/Documents/Git/infiniteMoneyTwitterBot/cookies/obJellyfin.cookies"
    )

    # results = await twitter.asyncTweet(text="A test tweet from the asyncTwitter module!")
    scheduleTweetResults = await twitter.asyncScheduleTweet(
        text="A test tweet from the asyncTwitter module!",
        date="2021-08-01 08:21",
    )

    print(scheduleTweetResults)


if __name__ == "__main__":
    run(testSearch)
