from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, text, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, mapped_column, Session
import os

# -- Anexar os bancos de dados
# ATTACH DATABASE 'D:\_Programas\SA_Solution\Planilha Compatibilidade\database\SASCOMCLIENTE.db' AS SASCOMCLIENTE;
# ATTACH DATABASE 'D:\_Programas\SA_Solution\Planilha Compatibilidade\database\SASOLUTIONS.db' AS SASOLUTIONS;

# -- Inserir os dados da tabela Cliente para a tabela Clientes
# INSERT INTO SASOLUTIONS.Clientes
# SELECT * FROM SASCOMCLIENTE.Clientes;

# -- Desanexar os bancos de dados
# DETACH DATABASE SASCOMCLIENTE;
# DETACH DATABASE SASOLUTIONS;




#db = create_engine("sqlite:///SASOLUTIONS.db")
caminho = os.getcwd()  
pathDataBase = os.path.join(caminho,'database','SASOLUTIONS.db') 
db = create_engine(f"sqlite:///{pathDataBase}")
Base = declarative_base()

#Criar a Tabela Cliente
class Cliente(Base):
    __tablename__ = "Clientes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    empresa = Column("empresa", String(50))
    cnpj = Column("cnpj", String(15))
    cep = Column("cep", String(9))
    ende = Column("endereco", String(50))
    cidade = Column("cidade", String(30))
    uf = Column("uf", String(2))
    contato = Column("contato", String(40))
    depto = Column("departamento", String(15))
    tel = Column("telefone", String(15))
    mob = Column("mobile", String(15))
    email = Column("email", String(40))

    
    
    def __init__(self, empresa, cnpj, cep, ende, cidade, uf, contato, depto, tel, mob, email):
         
         self.empresa = empresa
         self.cnpj = cnpj
         self.cep = cep
         self.ende = ende
         self.cidade = cidade
         self.uf = uf
         self.contato = contato
         self.depto = depto
         self.tel = tel
         self.mob = mob
         self.email = email

class Relatorio(Base):
    __tablename__ = "template"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    noRelat = Column("_0000", String(10))
    produto = Column("_0001", String(50))
    cliente = Column("_0002", String(50))
    uf = Column("_0003", String(3))
    _0004 = Column("_0004", String(30))
    _0005 = Column("_0005", String(30))
    _0006 = Column("_0006", String(30))
    _0007 = Column("_0007", String(30))
    _0008 = Column("_0008", String(30))
    _0009 = Column("_0009", String(30))
    _0010 = Column("_0010", String(100))
    _0011 = Column("_0011", String(30))
    _0012 = Column("_0012", String(30))
    _0013 = Column("_0013", String(30))
    _0014 = Column("_0014", String(30))
    _0015 = Column("_0015", String(30))
    _0016 = Column("_0016", String(30))
    _0017 = Column("_0017", String(30))
    _0018 = Column("_0018", String(30))
    _0019 = Column("_0019", String(30))
    _0020 = Column("_0020", String(30))
    _0021 = Column("_0021", String(30))
    _0022 = Column("_0022", String(30))
    _0023 = Column("_0023", String(30))
    _0024 = Column("_0024", String(30))
    _0025 = Column("_0025", String(30))
    _0026 = Column("_0026", String(30))
    _0027 = Column("_0027", String(30))
    _0028 = Column("_0028", String(30))
    _0029 = Column("_0029", String(30))
    _0030 = Column("_0030", String(30))
    _0031 = Column("_0031", String(30))
    _0032 = Column("_0032", String(30))
    _0033 = Column("_0033", String(20))
    _0034 = Column("_0034", String(20))
    _0035 = Column("_0035", String(20))
    _0036 = Column("_0036", String(20))
    _0037 = Column("_0037", String(20))
    _0038 = Column("_0038", String(20))
    _0039 = Column("_0039", String(20))
    _0040 = Column("_0040", String(20))
    _0041 = Column("_0041", String(20))
    _0042 = Column("_0042", String(20))
    _0043 = Column("_0043", String(20))
    _0044 = Column("_0044", String(20))
    _0045 = Column("_0045", String(20))
    _0046 = Column("_0046", String(20))
    _0047 = Column("_0047", String(20))
    _0048 = Column("_0048", String(20))
    _0049 = Column("_0049", String(20))
    _0050 = Column("_0050", String(20))
    _0051 = Column("_0051", String(20))
    _0052 = Column("_0052", String(20))
    _0053 = Column("_0053", String(20))
    _0054 = Column("_0054", String(20))
    _0055 = Column("_0055", String(20))
    _0056 = Column("_0056", String(20))
    _0057 = Column("_0057", String(20))
    _0058 = Column("_0058", String(20))
    _0059 = Column("_0059", String(20))
    _0060 = Column("_0060", String(20))
    _0061 = Column("_0061", String(20))
    _0062 = Column("_0062", String(20))
    _0063 = Column("_0063", String(20))
    _0064 = Column("_0064", String(20))
    _0065 = Column("_0065", String(20))
    _0066 = Column("_0066", String(20))
    _0067 = Column("_0067", String(20))
    _0068 = Column("_0068", String(20))
    _0069 = Column("_0069", String(20))
    _0070 = Column("_0070", String(20))
    _0071 = Column("_0071", String(20))
    _0072 = Column("_0072", String(20))
    _0073 = Column("_0073", String(20))
    _0074 = Column("_0074", String(20))
    _0075 = Column("_0075", String(20))
    _0076 = Column("_0076", String(20))
    _0077 = Column("_0077", String(20))
    _0078 = Column("_0078", String(20))
    _0079 = Column("_0079", String(20))
    _0080 = Column("_0080", String(20))
    _0081 = Column("_0081", String(30))
    _0082 = Column("_0082", String(255))
    _0083 = Column("_0083", String(255))
    _0084 = Column("_0084", String(255))
    _0085 = Column("_0085", String(255))
    _0086 = Column("_0086", String(255))
    _0087 = Column("_0087", String(255))
    _0088 = Column("_0088", String(255))
    _0089 = Column("_0089", String(255))
    _0090 = Column("_0090", String(255))
    _0091 = Column("_0091", String(255))
    _0092 = Column("_0092", String(255))
    _0093 = Column("_0093", String(30))
    _0094 = Column("_0094", String(30))
    _0095 = Column("_0095", String(30))
    _0096 = Column("_0096", String(30))
    _0097 = Column("_0097", String(30))
    _0098 = Column("_0098", String(30))
    _0099 = Column("_0099", String(30))
    _0100 = Column("_0100", String(30))

    def __init__(self, noRelat, produto, cliente, uf, _0004, _0005, _0006, _0007, _0008,  _0009,
                      _0010, _0011, _0012, _0013, _0014, _0015, _0016, _0017, _0018,  _0019,
                      _0020, _0021, _0022, _0023, _0024, _0025, _0026, _0027, _0028,  _0029,
                      _0030, _0031, _0032, _0033, _0034, _0035, _0036, _0037, _0038,  _0039,
                      _0040, _0041, _0042, _0043, _0044, _0045, _0046, _0047, _0048,  _0049,
                      _0050, _0051, _0052, _0053, _0054, _0055, _0056, _0057, _0058,  _0059,
                      _0060, _0061, _0062, _0063, _0064, _0065, _0066, _0067, _0068,  _0069,
                      _0070, _0071, _0072, _0073, _0074, _0075, _0076, _0077, _0078,  _0079,
                      _0080, _0081, _0082, _0083, _0084, _0085, _0086, _0087, _0088,  _0089,
                      _0090, _0091, _0092, _0093, _0094, _0095, _0096, _0097, _0098,  _0099,
                      _0100):
         
         self.noRelat = noRelat
         self.produto = produto
         self.cliente = cliente
         self.uf = uf
         self._0004 = _0004
         self._0005 = _0005
         self._0006 = _0006
         self._0007 = _0007
         self._0008 = _0008
         self._0009 = _0009
         self._0010 = _0010
         self._0011 = _0011
         self._0012 = _0012
         self._0013 = _0013
         self._0014 = _0014
         self._0015 = _0015
         self._0016 = _0016
         self._0017 = _0017
         self._0018 = _0018
         self._0019 = _0019
         self._0020 = _0020
         self._0021 = _0021
         self._0022 = _0022
         self._0023 = _0023
         self._0024 = _0024
         self._0025 = _0025
         self._0026 = _0026
         self._0027 = _0027
         self._0028 = _0028
         self._0029 = _0029
         self._0030 = _0030
         self._0031 = _0031
         self._0032 = _0032
         self._0033 = _0033
         self._0034 = _0034
         self._0035 = _0035
         self._0036 = _0036
         self._0037 = _0037
         self._0038 = _0038
         self._0039 = _0039
         self._0040 = _0040
         self._0041 = _0041
         self._0042 = _0042
         self._0043 = _0043
         self._0044 = _0044
         self._0045 = _0045
         self._0046 = _0046
         self._0047 = _0047
         self._0048 = _0048
         self._0049 = _0049
         self._0050 = _0050
         self._0051 = _0051
         self._0052 = _0052
         self._0053 = _0053
         self._0054 = _0054
         self._0055 = _0055
         self._0056 = _0056
         self._0057 = _0057
         self._0058 = _0058
         self._0059 = _0059
         self._0060 = _0060
         self._0061 = _0061
         self._0062 = _0062
         self._0063 = _0063
         self._0064 = _0064
         self._0065 = _0065
         self._0066 = _0066
         self._0067 = _0067
         self._0068 = _0068
         self._0069 = _0069
         self._0070 = _0070
         self._0071 = _0071
         self._0072 = _0072
         self._0073 = _0073
         self._0074 = _0074
         self._0075 = _0075
         self._0076 = _0076
         self._0077 = _0077
         self._0078 = _0078
         self._0079 = _0079
         self._0080 = _0080
         self._0081 = _0081
         self._0082 = _0082
         self._0083 = _0083
         self._0084 = _0084
         self._0085 = _0085
         self._0086 = _0086
         self._0087 = _0087
         self._0088 = _0088
         self._0089 = _0089
         self._0090 = _0090
         self._0091 = _0091
         self._0092 = _0092
         self._0093 = _0093
         self._0094 = _0094
         self._0095 = _0095
         self._0096 = _0096
         self._0097 = _0097
         self._0098 = _0098
         self._0099 = _0099
         self._0100 = _0100

#Criar a Tabela de Compatibilidade Quimica
class Planilha(Base):
    __tablename__ = "comp_quimica"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    cat_membr = Column("cat_membr", String())           # Categoria da Membrana
    lote1 = Column("lote1", String())                   # Lote 1
    lote2 = Column("lote2", String())                   # Lote 2
    lote3 = Column("lote3", String())                   # Lote 3
    serial1 = Column("serial1", String())               # Serial 1
    serial2 = Column("serial2", String())               # Serial 2
    serial3 = Column("serial3", String())               # Serial 3
    poro_cat_membr = Column("poro_cat_membr", String()) # Poro
    fabri = Column("fabri", String())                   # Fabricante
    linha = Column("linha", String())                   # Linha
    cat_disp = Column("cat_disp", String())             # Categoria Dispositivo
    poro_cat_disp = Column("poro_cat_disp", String())   # Poro Dispositivo µm
    lote_disp = Column("lote_disp", String())           # Lote Dispositivo
    fabri_disp = Column("fabri_disp", String())         # Fabricante Dispositivo
    serial_cat_disp = Column("serial_cat_disp", String())   # Serial Dispositivo
    linha_cat_disp = Column("linha_cat_disp", String()) # Linha Dispositivo
    produto = Column("produto", String())               # Produto
    temp_filtra = Column("temp_filtra", String())       # Temperatura de Filtração
    manu_temp = Column("manu_temp", String())           # Manutenção de Temperatura
    tmp_contato = Column("tmp_contato", String())       # Tempo de contato
    id_sala = Column("id_sala", String())               # ID Sala
    sala_temp = Column("sala_temp", String())           # Temperatura
    sala_umid = Column("sala_umid", String())           # Umidade
    pi_memb_1 = Column("pi_memb_1", Float(precision=3)) # Membrana Inicial 1
    pi_memb_2 = Column("pi_memb_2", Float(precision=3)) # Membrana Inicial 2
    pi_memb_3 = Column("pi_memb_3", Float(precision=3)) # Membrana Inicial 3
    pf_memb_1 = Column("pf_memb_1", Float(precision=3)) # Membrana Final 1
    pf_memb_2 = Column("pf_memb_2", Float(precision=3)) # Membrana Final 2
    pf_memb_3 = Column("pf_memb_3", Float(precision=3)) # Membrana Final 3
    fli_memb_1 = Column("fli_memb_1", Float(precision=2))   # Membr 1 Inic - 100 ml
    fli_memb_2 = Column("fli_memb_2", Float(precision=2))   # Membr 2 Inic - 100 ml
    fli_memb_3 = Column("fli_memb_3", Float(precision=2))   # Membr 3 Inic - 100 ml
    flf_memb_1 = Column("flf_memb_1", Float(precision=2))   # Membr 1 Final - 100 ml
    flf_memb_2 = Column("flf_memb_2", Float(precision=2))   # Membr 2 Final - 100 ml
    flf_memb_3 = Column("flf_memb_3", Float(precision=2))   # Membr 3 Final - 100 ml
    pb_padrao = Column("pb_padrao", Float(precision=2))     # PB Padrão
    memb_1_fr = Column("memb_1_fr", Float(precision=1))     # Membr 1 Fluido Padrão
    memb_2_fr = Column("memb_2_fr", Float(precision=1))     # Membr 2 Fluido Padrão
    memb_3_fr = Column("memb_3_fr", Float(precision=1))     # Membr 3 Fluido Padrão
    memb_1_pr = Column("memb_1_pr", Float(precision=1))     # Membr 1 Produto
    memb_2_pr = Column("memb_2_pr", Float(precision=1))     # Membr 2 Produto
    memb_3_pr = Column("memb_3_pr", Float(precision=1))     # Membr 3 Produto
    pb_prod = Column("pb_prod", Float(precision=1))         # PB Produto > PB estimado
    fp_memb_1 = Column("fp_memb_1", Float(precision=1))     # Membrana 1 Fluido Padrão
    fp_memb_2 = Column("fp_memb_2", Float(precision=1))     # Membrana 2 Fluido Padrão
    fp_memb_3 = Column("fp_memb_3", Float(precision=1))     # Membrana 3 Fluido Padrão
    dt_inicial = Column("dt_inicial", DateTime)             # Data Inicial
    hr_inicial = Column("hr_inicial", DateTime)             # Hora Inicial
    dt_final = Column("dt_final", DateTime)                 # Data Final
    hr_final = Column("hr_final", DateTime)                 # Hora Final
    
    
    def __init__(self, empresa, cnpj, cep, ende, cidade, uf, contato, depto, tel, mob, email):
         
         self.empresa = empresa
         self.cnpj = cnpj
         self.cep = cep
         self.ende = ende
         self.cidade = cidade
         self.uf = uf
         self.contato = contato
         self.depto = depto
         self.tel = tel
         self.mob = mob
         self.email = email





Base.metadata.create_all(bind=db)


