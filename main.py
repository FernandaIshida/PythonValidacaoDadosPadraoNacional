from cpf_cnpj import Documento

#cpf_um = Cpf("15316264754")
#print(cpf_um)
#exemplo_cnpj = "35379838000112"
exemplo_cpf = "15316264754"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))

documento = Documento.cria_documento(exemplo_cpf)
print(documento)