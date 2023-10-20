class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.capacidade_tanque = 50  # Capacidade padrão do tanque em litros
        self.quantidade_combustivel = 0  # Tanque vazio por padrão
        self.consumo_medio = 10  # Consumo médio em Km por litro

    def previsao_km_restantes(self):
        if self.quantidade_combustivel <= 0:
            return 0
        return self.quantidade_combustivel * self.consumo_medio

    def andar(self, distancia_km):
        combustivel_necessario = distancia_km / self.consumo_medio
        if combustivel_necessario <= self.quantidade_combustivel:
            self.quantidade_combustivel -= combustivel_necessario
            return True
        else:
            print("Combustível insuficiente para percorrer a distância desejada.")
            return False

    def get_cor(self):
        return self.cor

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def get_capacidade_tanque(self):
        return self.capacidade_tanque

    def set_capacidade_tanque(self, nova_capacidade):
        self.capacidade_tanque = nova_capacidade

    def get_consumo_medio(self):
        return self.consumo_medio

    def set_consumo_medio(self, novo_consumo):
        self.consumo_medio = novo_consumo

# Exemplo de uso:
meu_carro = Carro("Sedan", "Vermelho")
print(f"Modelo: {meu_carro.modelo}")
print(f"Cor: {meu_carro.get_cor()}")
print(f"Capacidade do tanque: {meu_carro.get_capacidade_tanque()} litros")
print(f"Consumo médio: {meu_carro.get_consumo_medio()} Km/Litro")
print(f"Combustível no tanque: {meu_carro.quantidade_combustivel} litros")
print(f"Previsão de KM restantes: {meu_carro.previsao_km_restantes()} Km")
meu_carro.set_cor("Azul")
meu_carro.set_capacidade_tanque(60)
meu_carro.set_consumo_medio(12)
meu_carro.quantidade_combustivel = 40
print(f"Nova cor: {meu_carro.get_cor()}")
print(f"Nova capacidade do tanque: {meu_carro.get_capacidade_tanque()} litros")
print(f"Novo consumo médio: {meu_carro.get_consumo_medio()} Km/Litro")
print(f"Combustível no tanque: {meu_carro.quantidade_combustivel} litros")
print(f"Previsão de KM restantes: {meu_carro.previsao_km_restantes()} Km")
meu_carro.andar(200)
print(f"Combustível no tanque após dirigir 200 Km: {meu_carro.quantidade_combustivel} litros")
