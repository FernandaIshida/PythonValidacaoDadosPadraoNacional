from cpf_cnpj import CpfCnpj

#cpf_um = Cpf("15316264754")
#print(cpf_um)
exemplo_cnpj = "35379838000112"
exemplo_cpf = "15316264754"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))

documento = CpfCnpj(exemplo_cpf,'cpf')
print(documento)