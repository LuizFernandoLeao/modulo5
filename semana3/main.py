#Importação de bibliotecas
from serial.tools import list_ports
import pydobot
import inquirer
from yaspin import yaspin

#Listas as portas disponíveis
available_ports = list_ports.comports()

#O usuário pode escolher uma das portas disponíveis
porta_escolhida = inquirer.prompt([
    inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
])["porta"]

#Animação do carregamento do braço robótico
spinner = yaspin(text="Carregando...", color="yellow")

#Cria uma instância do robô, define sua velocidade e algumas variáveis
robo = pydobot.Dobot(port=porta_escolhida, verbose=False)
robo.speed(200)
posicoes = robo.pose()
comandos = ["home", "mover", "posicao_atual", "sair"]

#Define a função dos comandos do robô
def tarefas(tarefa):

    match tarefa:
         
        case "home":
            spinner.start()
            robo.move_to(242.23,0,151.35, 0, wait=True)
            spinner.stop()
            return "O robô retornou à sua posição inicial."
         
        case "ligar_ferramenta":
                robo.suck(True)
                comandos.remove("ligar_ferramenta")
                comandos.insert(1, "desligar_ferramenta")
                return "Você ligou a ferramenta"
         
        case "desligar_ferramenta":
                robo.suck(False)
                comandos.remove("desligar_ferramenta")
                comandos.insert(1, "ligar_ferramenta")
                return "Você desligou a ferramenta"

        case "mover":
            distancia_x = inquirer.prompt([inquirer.Text("distancia_x", message="Digite a distância no eixo X")])["distancia_x"]
            distancia_y = inquirer.prompt([inquirer.Text("distancia_y", message="Digite a distância no eixo Y")])["distancia_y"]
            distancia_z = inquirer.prompt([inquirer.Text("distancia_z", message="Digite a distância no eixo Z")])["distancia_z"]
            distancia_r = inquirer.prompt([inquirer.Text("distancia_r", message="Digite a distância de rotação")])["distancia_r"]
            posicoes = robo.pose()
            nova_posicao_x = posicoes[0] + int(distancia_x)
            nova_posicao_y = posicoes[1] + int(distancia_y)
            nova_posicao_z = posicoes[2] + int(distancia_z)
            nova_posicao_r = posicoes[3] + int(distancia_r)
            spinner.start()
            robo.move_to(nova_posicao_x, nova_posicao_y, nova_posicao_z, nova_posicao_r, wait=True)
            spinner.stop()
            return f"Você moveu o robô para a posição {robo.pose()}."
         
        case "posicao_atual":
            return f"A posição atual do robô é: {robo.pose()}"
         
        case _:
            return "Erro no comando"
         
if __name__ == "__main__":
    comandos.insert(1, "ligar_ferramenta")
    questions = [
        inquirer.List('action',
                      message="Escolha uma ação",
                      choices=comandos,
                      ),
    ]

    while True:
        perguntas = [
        inquirer.List("comando", message="Escolha um comando", choices=comandos)
    ]
        
        resposta = inquirer.prompt(perguntas)
        if resposta["comando"] == "sair":
            break
        resultado = tarefas(resposta["comando"])
        print(resultado)