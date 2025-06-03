import sqlite3
#conectando um banco de dados
banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('file.db')

#criando um curso para operar comandos SQL
cursor = banco.cursor()

# 1 criando tabela nomes
cursor.execute("""CREATE TABLE names (
  Nomes TEXT NOT NULL
)""");
banco.commit()

# cadastrando tabela nomes
cursor.execute("""INSERT INTO names (names)
VALUES
('victor machado'),
('carlos antonio'),
('pedro alves'),
('fabio santos'),
('patricia ferreira')""");

#consultando dados da tabela nomes
cursor.execute("SELECT * FROM names ")
print(cursor.fetchall())


# criando tabela cidades
cursor.execute("""CREATE TABLE Cyty (
  Cidades TEXT NOT NULL
)""");
banco.commit()

# cadastrando tabela cidades
cursor.execute("""INSERT INTO City (City)
VALUES
('sao paulo'),
('rio de janeira'),
('belo horizonte'),
('vitoria es'),
('santa catarina')""");

#consultado dados da tabela cidades
cursor.execute("SELECT * FROM City")
print(cursor.fetchall())

# criando tabela salarios
cursor.execute("""CREATE TABLE salaries(
  salaries INTERGER NOT NULL)""");
banco.commit()

# cadastrando tabela salarios
cursor.execute("""INSERT INTO salaries (salaries)
VALUES
(1000,),
(1500,),
(1200,),
(1600,),
(1800,)""");


#consultando dados da tabela salario
cursor.execute("SELECT * FROM salaries")
print(cursor.fetchall())

# criando tabela data de nascimento
cursor.execute("""CREATE TABLE datebirth (
  Datanascimento INTEGER NOT NULL,
)""");

# cadastrando dados na tabela
cursor.execute("""INSERT INTO datebirth (datebirth)
VALUES
(29/04/1998),
(11/11/1997),
(05/03/1996),
(03/12/2004),
(05/09/2003) """);
banco.commit()

#consultando dados da tabel
cursor.execute("SELECT * FROM datebirth")
print(cursor.fatchall())

# criando tabela folha de pagamento
cursor.execute(""" CREATE TABLE pamantoleaf (
  folha de pagamento INTEGER NOT NULL
)""");

# adicionando valor a tabela fohadepagamento
cursor.execute("""INSERT INTO pamantoleaf (pamantoleaf)
VALUES
(1000),
(1500),
(1200),
(1600),
(1800)""");

#consultado dados da tabela folhade pagamentos
cursor.execute("SELECT * FRO folhadepagamento")
print(cursor.fatchall())

# criando  tabela nome do departamento
cursor.execite ("""CREATE TABLE department (
  departamento TEXT NOT NULL
)""");

#adicionando dados da tabela departamento
cursor.execute("""INSERT INTO department (department)
VALUES
('vendas'),
('RH'),
('financeiro').
('gerente'),
('assistente')""");

#consultado dado da tabela
cursor.execute ("SELECT * FROM department")
print(cursor.fetchall())

# criando tabela lista de fucionarios
cursor.execute("""CREATE TABLE list (
  lista INTEGER NOT NULL
)""");

#adicionando dados na tabela
cursor.execute(""" INSERT INTO list (list)
VALUES
(1),
(2),
(3),
(4),
(5),""");
banco.commit()

#consultando dados da tabela
cursor.execute("SELECT * FROM list")
print(cursor.fetchall())

# lista nomes do departamentos ordenado por fucionarios
cursor.execute("""CREATE TABLE  departmentnames(
  nomes TEXT NOT NULL
)""");

#adicionando dados na tabela
cursor.execute("""INSERT INTO departmentnames (departmentnames)
VALUES)
VALUES
('victor vendas'),
('carlos RH'),
('pedro financeiro'),
('fabio gerente'),
('patricia assistente')""");

#consultado dados da tabela
cursor.execute("SELECT * FROM departmentnames")
print(cursor.fetchall())
print(cursor.fetchall())
# fim

