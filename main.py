#Todos os Imports
import asyncio
import random
from discord.ext import commands
from discord.utils import get
from discord import app_commands
import discord
import datetime

id_do_servidor = 1198249545189040210

#Mensagens RPC
mensagensrpc = [
    "A espiar pessoas...",
    "A Fazer Milagres...",
    "A Dormir...",
    "Comer brocolos",
    "A Aspirar as vossas almas",
    "RicFazeres",
    "A Cristina Ferreira",
    "Explorando o vazio do universo",
    "Conversando com as plantas 🌱",
    "Ensinando peixes a voar 🐠",
    "😶‍🌫️",
    "🐊",
    "🦑",
    "",
]

#Sorteio de Ações
Indianokazio = [discord.ActivityType.watching, discord.ActivityType.listening, discord.ActivityType.playing]
comidadokazio = random.choice(Indianokazio)


class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        self.botactivity = None
        self.estafetadaglovo = None

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=id_do_servidor))
            self.synced = True
        print(f"MR.{self.user} TÁ ON!")

    

        while not self.is_closed():
            mensagem = random.choice(mensagensrpc)
            await self.update_status(mensagem)

            # Esperar 1 hora antes de atualizar o RPC novamente
            await asyncio.sleep(3600)

    async def update_status(self, mensagem):
        escolhasdaglovo = [discord.Status.do_not_disturb, discord.Status.online, discord.Status.idle]

        if mensagem == "A Dormir...":
            self.estafetadaglovo = discord.Status.idle
        else:
            self.estafetadaglovo = random.choice(escolhasdaglovo)

        self.botactivity = discord.Activity(type=comidadokazio, name=mensagem)

        await self.change_presence(activity=self.botactivity, status=self.estafetadaglovo)
        print(f"RPC atualizado: {mensagem} | Status: {self.estafetadaglovo} | Ação: {comidadokazio}")

    async def delete_old_messages(self):
        canal_id = 'Canal das mensagens'  # Substitua pelo ID do canal onde as mensagens devem ser verificadas
        canal = self.get_channel(int(canal_id))

        if canal:
            utc_now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)  # Adiciona informação de fuso horário UTC
            async for message in canal.history():
                created_at = message.created_at.replace(tzinfo=datetime.timezone.utc)  # Adiciona informação de fuso horário UTC
                if (utc_now - created_at).total_seconds() >= 15:
                    await message.delete()

        # Aguarde um tempo antes de verificar novamente
        await asyncio.sleep(20) 
        



aclient = client()
tree = app_commands.CommandTree(aclient)


@tree.command(guild=discord.Object(id=id_do_servidor), name='ativar_falas', description='Ativa as falas do armindo')
async def enviar_ensagens(interaction: discord.Interaction):
    print("O Modo Fala foi ativo por um Admin")
    await aclient.wait_until_ready()

    while not aclient.is_closed():
        canal_id = '1198249545822376068'  # Substitua pelo ID do canal onde você quer enviar as mensagens
        canal = aclient.get_channel(int(canal_id))

        if canal:
            mensagens = ["Aqui o meu grande amigalhasso https://thumbs.web.sapo.io/?W=1200&H=627&crop=center&delay_optim=1&epic=MjQzb4sTZji4VFvkCIzkhc6ZXNX77F6S+vUmw3/+s3Z6gE49jTQBsjyui29fgeOqwuc6enXG2YQ9OSoufG7VCwUHwa9qmi8xEndMF2ipMDP9djs=",
                        "Olá mortais",
                        "Acima de mim, só eu mesmo",
                        "[Eu sou um link clica em mim](<https://www.youtube.com/watch?v=dQw4w9WgXcQ>)",
                        "Não gosto de bagels",
                        "Juro que de mim ninguem te tira, valiosa como pedra de safira",
                        "A Torre Eiffel, em Paris, é um dos marcos mais conhecidos do mundo. Construída por Gustave Eiffel em 1889 para a Exposição Universal, ela atrai milhões de visitantes todos os anos. Com mais de 300 metros de altura, oferece vistas deslumbrantes da cidade e é um símbolo icônico da França e de seu progresso tecnológico. https://cdn.discordapp.com/attachments/1199341651722764358/1206593346307489802/9884bbc84c3d354ecf8951c25989ab73.jpg?ex=65dc929f&is=65ca1d9f&hm=c1acf6c44ea3f03ec7ba95ec0ba69619695bcbb46b30601d1b39f2995821db80&",
                        "Bora jogar mario kart o meu nick na switch é mrArmindo123",
                        "óh joka, não doi, não doi, juro pela minha morte",
                        "Ca puta zé - Ricardo Fazeres",
                        "3.67g de grão de arroz que vem doa Burkina Faso cas cabras da montanha trazem pendoradas nos almeices das bordas da Ti Jaquina",
                        "vou te deserdar",
                        "Malta vou jogar make it meme com o Armindo",
                        "Olhem o que comprei https://www.amazon.com/What-Meme-Emotional-Support-Nuggets/dp/B0CFBBBSHY?th=1",
                        "https://www.amazon.com/gp/product/B0CLXRMH5Y/ref=ewc_pr_img_1?smid=AJHM1SL49SVZV&th=1",
                        "CRISTINA **PARA DE BERRAR!!!**",
                        "Sempre falamos sobre ser alérgico a animais, mas nunca sobre animais serem alérgicos a humanos.",
                        "Por que pressionamos com mais força o comando quando sabemos que as baterias estão a acabar?",
                        "Você se torna o que você come, então os canibais são os mais humanos de todos nós",
                        "No Futuro, as pessoas poderão viajar para planetas com a gravidade maior para se exercitar e depois voltar.",
                        "Se tu forem um espião famoso, és uma porcaria no teu trabalho",
                        "Bater palmas é literalmente baters-te por cena de algo que gostste",
                        "Uma mulher grávida tem a capacidade de prodizir um cérebroque poderá ser mais inteligente e esperto do que o próprio cérebro dela um dia",
                        "Olha ai a minha conta da nintendo: [htps://nintendo.com\profile\Armind0_203](<https://www.youtube.com/watch?v=dQw4w9WgXcQ>)",
                       ]

            mensagem_aleatoria = random.choice(mensagens)
            await canal.send(mensagem_aleatoria)

            # Aguarde um tempo aleatório antes de enviar a próxima mensagem
            print("A mensagem enviada foi: ", mensagem_aleatoria)
            await asyncio.sleep(random.randint(5000, 12000))

    await interaction.response.send_message("O Modo fala Foi Ativo", ephemeral=True)

@tree.command(guild=discord.Object(id=id_do_servidor), name='ping', description='Verifica a latência do bot')
async def ping(interaction: discord.Interaction):
    latency = aclient.latency * 1000  # Convertendo para milissegundos
    await interaction.response.send_message(f'Pong! Latência: {latency:.2f}ms')

# Processar usuário
@tree.command(guild=discord.Object(id=id_do_servidor), name='processar', description='Inicia uma votação para processar um usuário.')
async def processar(interaction: discord.Interaction, user: discord.User, tempo: int):
    # Adicione reações para votação
    await interaction.response.send_message(f"**Foi Iniciado um processo**")
    mensagem = await interaction.followup.send(f"Votação iniciada para processar {user.mention}. Tempo de votação: 90 segundos.")
    print (f"Foi Iniciado um processo contra {user.mention}")

    await mensagem.add_reaction("🟢")  # Reação para 'Sim'
    await mensagem.add_reaction("🔴")  # Reação para 'Não'

    # Atualiza a mensagem a cada 10 segundos
    for i in range(9, -1, -1):
        await asyncio.sleep(10)
        await mensagem.edit(content=f"Votação iniciada para processar {user.mention}. Tempo restante: {i*10} segundos.")

    # Obtenha as reações
    mensagem = await interaction.channel.fetch_message(mensagem.id)
    reacoes = {str(reacao.emoji): reacao.count for reacao in mensagem.reactions}

    if "🟢" in reacoes and "🔴" in reacoes:
        if reacoes["🟢"] > reacoes["🔴"]:
            await interaction.followup.send(f"A maioria votou em 'Sim'. {user.mention} está processado!")
            # Coloca o usuário em timeout pelo tempo especificado
            maltinha_role = discord.utils.get(user.guild.roles, id=1198251766945435648)
            await user.remove_roles(maltinha_role)
            await asyncio.sleep(tempo)
            await user.add_roles(maltinha_role)
        else:
            await interaction.followup.send(f"A maioria votou em 'Não'. {user.mention} não está processado.")

games = []

@tree.command(guild=discord.Object(id=id_do_servidor), name='addgame', description='Adicionar um jogo à roleta')
async def add_game(interaction: discord.Interaction, game: str):
    games.append(game)
    await interaction.response.send_message(f'O jogo {game} foi adicionado à roleta!')

@tree.command(guild=discord.Object(id=id_do_servidor), name='roleta', description='Sortear um jogo da roleta')
async def roulette(interaction: discord.Interaction):
    if games:
        selected_game = random.choice(games)
        await interaction.response.send_message(f'O jogo sorteado foi: {selected_game}!')
    else:
        await interaction.response.send_message('Não há jogos na roleta. Use /addgame para adicionar um.')



aclient.run("Adiciona aqui a tua Token")
