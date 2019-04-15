import command
import module
import util

class CoreModule(module.Module):
    name = 'Core'

    @command.desc('List the commands')
    def cmd_help(self, msg):
        out = 'Command list:'

        for name, cmd in self.bot.commands.items():
            # Don't count aliases as separate commands
            if name != cmd.name:
                continue

            desc = cmd.desc if cmd.desc else '__No description provided__'
            aliases = ''
            if cmd.aliases:
                aliases = f' (aliases: {", ".join(cmd.aliases)})'

            out += f'\n    \u2022 **{cmd.name}**: {desc}{aliases}'

        return out

    @command.desc('Get how long the bot has been up for')
    def cmd_uptime(self, msg):
        delta_us = util.time_us() - self.bot.start_time_us
        return f'Uptime: {util.format_duration_us(delta_us)}'
