class Cliente:
  def __init__(self, codigo, nome, email, telefone):
      self.codigo = codigo
      self.nome = nome
      self.email = email
      self.telefone = telefone

  def validar(self):
      return all([self.codigo, self.nome, self.email, self.telefone])

  def to_dict(self):
      return {
          "codigo": self.codigo,
          "nome": self.nome,
          "email": self.email,
          "telefone": self.telefone
      }
