import logging
import slackweb


class SlackHandler(logging.Handler):

    def __init__(self, url, channel, username, icon_emoji):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Our custom argument
        self.slack_obj = slackweb.Slack(url=url)
        self.channel = channel
        self.username = username
        self.icon_emoji = icon_emoji

    def emit(self, record):
        self.slack_obj.notify(
            text=record.exc_text or record.msg, channel="#{}".format(self.channel), username=self.username, icon_emoji=self.icon_emoji)
