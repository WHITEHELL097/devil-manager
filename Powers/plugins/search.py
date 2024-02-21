from traceback import format_exc

from pyrogram.types import InputMediaPhoto, Message
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.myanimelist import Search as AnimeSearch
from search_engine_parser.core.engines.stackoverflow import \
    Search as StackSearch
from search_engine_parser.core.exceptions import (NoResultsFound,
                                                  NoResultsOrTrafficError)

from Powers import LOGGER, SUPPORT_CHANNEL
from Powers.bot_class import Gojo
from Powers.utils.custom_filters import command
from Powers.utils.http_helper import *
from Powers.utils.kbhelpers import ikb

#have to add youtube

gsearch = GoogleSearch()
anisearch = AnimeSearch()
stsearch = StackSearch()

@Gojo.on_message(command('google'))
async def g_search(c: Gojo, m: Message):
    split = m.text.split(None, 1)
    if len(split) == 1:
        return await m.reply_text("No query given\nDo `/help search` to see how to use it")
    to_del = await m.reply_text("Searching google...")
    query = split[1]
    try:
        result = await gsearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"Here are the results of requested query **{query.upper()}**"
        await to_del.delete()
        await m.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await m.reply_text("No result found corresponding to your query")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await m.reply_text("No result found due to too many traffic")
        return
    except Exception as e:
        await to_del.delete()
        await m.reply_text(f"Got an error:\nReport it at @{SUPPORT_CHANNEL}")
        LOGGER.error(e)
        LOGGER.error(format_exc())
        return


@Gojo.on_message(command('anime'))
async def anime_search(c: Gojo, m: Message):
    split = m.text.split(None, 1)
    if len(split) == 1:
        return await m.reply_text("No query given\nDo `/help search` to see how to use it")
    to_del = await m.reply_text("Searching myanimelist...")
    query = split[1]
    try:
        result = await anisearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"Here are the results of requested query **{query.upper()}**"
        await to_del.delete()
        await m.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await m.reply_text("No result found corresponding to your query")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await m.reply_text("No result found due to too many traffic")
        return
    except Exception as e:
        await to_del.delete()
        await m.reply_text(f"Got an error:\nReport it at @{SUPPORT_CHANNEL}")
        LOGGER.error(e)
        LOGGER.error(format_exc())
        return

@Gojo.on_message(command('stack'))
async def stack_search(c: Gojo, m: Message):
    split = m.text.split(None, 1)
    if len(split) == 1:
        return await m.reply_text("No query given\nDo `/help search` to see how to use it")
    to_del = await m.reply_text("Searching Stackoverflow...")
    query = split[1]
    try:
        result = await stsearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"Here are the results of requested query **{query.upper()}**"
        await to_del.delete()
        await m.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await m.reply_text("No result found corresponding to your query")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await m.reply_text("No result found due to too many traffic")
        return
    except Exception as e:
        await to_del.delete()
        await m.reply_text(f"Got an error:\nReport it at @{SUPPORT_CHANNEL}")
        LOGGER.error(e)
        LOGGER.error(format_exc())
        return


async def getText(message: Message):
    # Credits: https://t.me/whitehell097
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
        except Exception:
            return None
    else:
        return None

@Gojo.on_message(command(["images","imgs"]))
async def okgoogle(img):
    """For .reverse command, Google search images and stickers."""
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await tbot.download_media(message, photo)
    else:
        await img.reply("`Reply to photo or sticker fu*ker`")
        return

    if photo:
        dev = await img.reply("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await dev.edit("`Unsupported sexuality, most likely.`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            await dev.edit(
                "`Image successfully uploaded to Google. Maybe.`"
                "\n`Parsing source now. Maybe.`"
            )
        else:
            await dev.edit("`Google told me to fu*k off.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]

        if guess and imgspage:
            await dev.edit(f"[{guess}]({fetchUrl})\n\n`Looking for this Image...`")
        else:
            await dev.edit("`Can't find this piece of shit.`")
            return

        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await tbot.send_file(
                entity=await tbot.get_input_entity(img.chat_id),
                file=yeet,
                reply_to=img,
            )
        except TypeError:
            pass
        await dev.edit(
            f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})"
        )



__PLUGIN__ = "search"


__alt_name__ = [
    "google",
    "anime",
    "stack",
]

__HELP__ = """
**Search**

**Available commands:**
• /google `<query>` : Search the google for the given query.
• /anime `<query>`  : Search myanimelist for the given query.
• /stack `<query>`  : Search stackoverflow for the given query.
• /images (/imgs) `<query>` : Get the images regarding to your query

**Example:**
`/google pyrogram`: return top 5 reuslts.
"""
