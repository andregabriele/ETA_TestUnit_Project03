class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        return f"Esse restaturante chama {self.restaurant_name} and serve {self.cuisine_type}. " \
               f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto."

        # BUG - Nome restaurante estava passando o que ele serve no lugar. Informação (nome) duplicado.
        # MELHORIAS - Substituir print e Juntar ambas strings em uma só.

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""

        if not self.open:
            self.open = True
            self.number_served = 2
            msg = f"{self.restaurant_name} agora está aberto!"
            return self.open and msg
        else:
            return f"{self.restaurant_name} já está aberto!"

        # MELHORIA - substituir print
        # MELHORIA - Retornar tanto o status de aberto quanto a mensagem proposta.
        # MELHORIA - Substituição do sinal pois não da pra servir pessoas com o numero negativo.
        # BUG - Ao entrar no if (quando o self.open = False), ele estava mantendo =False, ao invés de colocar o =True.

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""

        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

        # MELHORIA - substituir print

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            return f"{total_customers} de pessoas atendidas por este restaurante até o momento"
        else:
            return f"{self.restaurant_name} está fechado!"

        # MELHORIAS - Substituir print e retornar mensagem com o total de customers atendidos.

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers
            return f"{self.number_served} de pessoas atendidas por este restaurante"
        else:
            return f"{self.restaurant_name} está fechado!"

        # MELHORIA - substituir print
        # BUG - Sobrescrição do valor na lógica aplicada no "if". Não estava incrementando.
