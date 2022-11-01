import nextcord 
import discord_components.button

from nextcord import slash_command, Interaction
from nextcord.ext.commands import Cog

class role_options(Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    ID = 1035593393381838888
    
    @slash_command(name = 'roles', description = 'select your role in a blue team', guild_ids = [ID])
    async def roles(self, interaction: Interaction): 
        button = discord_components.button.roles()
        await interaction.response.send_message("Choose your role and we gonna give you the description for each role.")
        await interaction.followup.send(view=button)
        await button.wait()
        
        if button.value == None:
            return
        elif button.value == 'alert':
            await interaction.followup.send('As mentioned above, let\'s try typing /log_files or /other_messages')
        elif button.value == 'response':
            await interaction.followup.send('As mentioned above, let\'s try typing /list_tasks')
        elif button.value == 'environment':
            print("So you want to simulate a vulnerable environment")
    
    @slash_command(name = 'test', description = 'Run the test slash_command', guild_ids = [ID],)
    async def test(self, interaction: Interaction, message):
        await interaction.response.send_message(f'you`ve just said what? {message} ha!')
            
def setup(bot):
    bot.add_cog(role_options(bot))
            

        
    
    


