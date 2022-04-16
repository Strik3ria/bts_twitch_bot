import os

from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TWITCH_TOKEN')


class logger:

    def __init__(self, message):
        self.message = message

class BTSTwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TOKEN,
            prefix='!',
            initial_channels=['strik3ria']
        )

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command(name="so")
    async def shoutout(self, ctx, message):
        if len(message.split()) < 2 and ctx.author.is_mod:
            await ctx.send(
                f'Be sure to check out {message} over at twitch.tv/{message}'
            )

    @commands.command(name="discord")
    async def discord(self, ctx):
        await ctx.send(
            "Be sure to check us out on Discord at https://discord.gg/kRuKwdRdJw"
        )

    @commands.command(name="facebook")
    async def facebook(self, ctx):
        await ctx.send(
            "Wanna get updates on what we are up to? Check out and follow our "
            "facebook at https://facebook.com/BecksAndTedsShow"
        )

    @commands.command(name="twitter")
    async def twitter(self, ctx):
        await ctx.send(
            "Catch up an what we have coming up and going on! Follow us on Twitter"
            " at https://twitter.com/BecksAndTedsSho"
        )


if __name__ == '__main__':
    bot = BTSTwitchBot()
    bot.run()