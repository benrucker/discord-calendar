import os


class GuildInfo():
    def __init__(self, guild):
        self.id = guild.id
        self.name = guild.name
        self.resources = os.path.join('guilds', self.name + str(self.id))

    def __repr__(self):
        return 'GuildInfo Object: ' + self.name + ':' + self.id
