import os

from twitchio.ext import commands
from dotenv import load_dotenv
from datetime import date

load_dotenv()
TOKEN = os.getenv('TWITCH_TOKEN')


class Logger:

    def info(self, message):
        print(f'INFO: {message}')

    def error(self, message):
        print(f'ERROR: {message}')

    def critical(self, message):
        print(f'CRITICAL: {message}')

class BTSTwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TOKEN,
            prefix='!',
            initial_channels=['becksandtedsshow']
        )
        self.logger = Logger()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command(name="so")
    async def shoutout(self, ctx, message):
        if len(message.split()) < 2 and ctx.author.is_mod:
            self.logger.info(f"Shoutout - {ctx.author.name} - {date.today()}")
            await ctx.send(
                f'Be sure to check out {message} over at twitch.tv/{message}'
            )

    @commands.command(name="discord")
    async def discord(self, ctx):
        self.logger.info(f"Discord - {ctx.author.name} - {date.today()}")
        await ctx.send(
            "Be sure to check us out on Discord at https://discord.gg/kRuKwdRdJw"
        )

    @commands.command(name="facebook")
    async def facebook(self, ctx):
        self.logger.info(f"Facebook - {ctx.author.name} - {date.today()}")
        await ctx.send(
            "Wanna get updates on what we are up to? Check out and follow our "
            "facebook at https://facebook.com/BecksAndTedsShow"
        )

    @commands.command(name="twitter")
    async def twitter(self, ctx):
        self.logger.info(f"Twitter - {ctx.author.name} - {date.today()}")
        await ctx.send(
            "Catch up an what we have coming up and going on! Follow us on Twitter"
            " at https://twitter.com/BecksAndTedsSho"
        )
    
    @commands.command(name="follow")
    async def follow(self, ctx):
        self.logger.info(f"Follow - {ctx.author.name} - {date.today()}")
        await ctx.send(
            "Make sure to follow us! We are working hard to get to 50 followers!"
        )


if __name__ == '__main__':
    bot = BTSTwitchBot()
    bot.run()