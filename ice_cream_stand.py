from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list: list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

        # MELHORIA - Incluir uma lista

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if len(self.flavors) > 1:
            msg = "No momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                if flavor == self.flavors[-1]:
                    msg = f'{msg} {flavor}'
                    break
                msg = f'{msg} {flavor},'
            return msg
        else:
            return "Estamos sem estoque atualmente!"

        # BUG - O código não entra no else pois obrigatoriamente passa algum valor para 'self.flavors';
        # MELHORIA - Criação de uma lógica para o código entrar no if e, em caso de erro, no else;
        # MELHORIA - Criação de uma lógica de mensagem de retorno positivo = concatenação;
        # MELHORIA - Substituir print por return;

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""

        if flavor in self.flavors:
            return f"Temos no momento {flavor}!"
        else:
            return f"Não temos no momento {flavor}!"

        # BUG - Não retornava o item pesquisado, retornando a lista inteira;
        # BUG - O código não entra no else pois obrigatoriamente passa algum valor para flavors;
        # MELHORIA - Substituir print por return;
        # MELHORIA - Para evitar duplicidade de retorno negtivo, foi retirado o "if (self.flavors):" e "ELSE".

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if flavor in self.flavors:
            return "Sabor já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"

        # BUG - O código não entra no else pois obrigatoriamente passa algum valor para flavors;
        # MELHORIA - Substituir print por return;
        # MELHORIA - Como a validação é apenas para adição de sabores, para validar a função foi retirado o "if(self.flavors)" e "ELSE".