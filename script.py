class Script(object):

    START_MSG = """<b>Hy {}😻,</b>

<i>Im a simple bot which is designed and built for adding filters in any group.

See <b>/help</b> for commands and more details.</i>
"""
    HELP_MSG = """<b>What is a filter bot?</b>
<i>A bot were group admins can set replies for a particular keyword and the bot will automatically send preset replies whenever that keyword enountered in the chat.</i>

<b>Usual commands:</b>
/start - <code>check whether im online</code>
/help - <code>get this help message</code>
/about - <code>about me</code>

<b>© @IET_Owner</b>"""
    COCT_MSG = """<b>Connections:</b>
Used to connect bot to PM which let will you to execute both normal filter related commands and some other sensitive commands right from the PM that will
reflect in the group which helps you to keep the filter additions and other stuffs private and helps to prevent flooding.

<b>NOTE:</b>
<i>1. Only admins can add a connection.
2. Chat owner can enable/disable connection permission of admins by using </i><i>/permissions</i> <i>command.
3. In a chat you can simply use the </i><i>/connect</i> <i>for starting a connection and in PM you must specify chat id right after the command.</i>

<b>Commands and Usage:</b>
/connect <chat id> - <code>connect a particular chat to your PM</code>
/disconnect <chat id> - <code>disconnect from a chat</code>
/connections - <code>list all your connections</code>

<b>© @IET_Owner</b>"""
    FLTR_MSG = """<b>Filters:</b>
Filter is the feature were users can set automated replies for a particular keyword and the bot will respond whenever a keyword is found the message

<b>NOTE:</b>
<i>1. bot should have admin privillage in order to reply filters in a chat.
2. only admins can add filters in a chat.
3. filters does support all the telegram markdowns, medias and buttons.
4. alert buttons are also supported with a limit of 64 characters.
5. there are some easter eggs, try to find it out.</i>

<b>Commands and Usage:</b>
/add   - <code>add a filter</code>
/view - <code>list all the filters of a chat</code>
/del  - <code>delete a specific filter (separate keywords with spaces for deleting multiple filters at a time)</code>
/delall - <code>delete the whole filters in a chat (chat owner only)</code>

<b>© @IET_Owner</b>"""
    BTN_MSG = """<b>Buttons:</b>
<i>@betterfiltersbot</i> <i>supports both url and alert inline buttons, now lets see how to implement it.</i>

<b>NB:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly formatted as below or else result will be malformed.

<b><u>Url Button</u>
</b>
<code>[Button Url](buttonurl://https://t.me/betterfiltersbot)</code>

<b><u>Alert Button
</u></b>
<code>[Button alert](buttonalert://🔥 This is a test buttonalert)</code>

<b>© @IET_Owner</b>"""
    EXTR_MSG = """<b>Extras;</b>

/status  -  Shows current status of your bot (Auth User Only)

/id  -  Shows ID information

<code>/info userid</code>  -  Shows User Information. Use <code>/info</code> as reply to some message for their details!

<b>© @IET_Owner</b>"""

    


    ABOUT_MSG = """<u>🔴 </u><b><u>My Name : </u></b><u><b><i>Filter Bot</i></b> 🔴</u>

🔻 <b>Creater      :</b> @IET_Owner   
🔻 <b>Server        : </b> <a href='http://heroku.com/'>Heroku</a>
🔻 <b>Language  :</b> <code>Python3</code>
🔻 <b>Database   : </b><a href='http://mongodb.com/'>Mongo DB</a>
🔻 <b>Library        :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a>"""
