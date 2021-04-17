from django import forms
from .models import DataDB


class InsiraDadosForm(forms.ModelForm):
	class Meta:
		model = DataDB
		widgets = {
		'marca': forms.TextInput(attrs={'placeholder':'Marca do carro'}),
		'modelo': forms.TextInput(attrs={'placeholder':'Modelo do carro'}),
		'ano': forms.NumberInput(attrs={'placeholder':'Ano do carro'}),
		'status': forms.TextInput(attrs={'placeholder':'Status do carro'}),
		'cor': forms.TextInput(attrs={'placeholder':'Cor do carro'}),
		'lcoalidade': forms.TextInput(attrs={'placeholder':'Local onde a venda foi concretizada'}),
		'combustivel': forms.TextInput(attrs={'placeholder':'Combutivél do carro'}),
		'quilometragem': forms.NumberInput(attrs={'placeholder':'Quilometragem do carro'}),
		'preco': forms.NumberInput(attrs={'placeholder':'Preço final do carro na compra ou venda'}),
		'lucro': forms.NumberInput(attrs={'placeholder':'Lucro ou prejuízo pós venda do carro, insira 0 caso seja compra'}),
		}

		fields = ['marca','modelo','ano','status','cor','localidade','combustivel','quilometragem','preco','lucro']


	def clean_marca(self, *args, **kwargs):
		marca= self.cleaned_data.get('marca')
		marcas=['Acura','Agrale','Alfo Romeo','Am Gen','Asia motors','ASTON MARTIN','Audi','Baby','BMW','BRM','BUGRE','Cadillac',
                                'CBT Jipe','CHANA','CHANGAN','CHERY','Chrysler','Citroën','Cross Lander','Daewoo','Daihatsu',
                                'Dodge','EFFA','Engesa','Envemo','Ferrari','Fiat','Fibravan','Ford','FOTON','Fyber','GEELY','GM CHEVROLET',
                                'GREAT WALL','Gurgel','HAFEI','HITECH ELECTRIC','HONDA','HYUNDAY','ISUZU','IVECO','JAC','Jaguar','Jeep','JINBEI','JPX',
                                'Kia Motors','Lada','Lamborghini','Land Rover','Lexus','LIFAN','LOBINI','Lotus','Mahindra','Maserati','Matra','Mazda',
                                'Mclaren','Mercedez Benz','Mercury','MG','MINI','Mitsubishi','Miura','Nissan','Peugeot','Plymouth','Pontiac','Porsche',
                                'RAM','RELY','Renault','Rolls-Royce','Rover','Saab','Saturn','Seat','SHINERAY','smart','SSANGYONG','Subaru','Suzuki',
                                'TAC','Toyota','Troller','Volvo','VW-VOLKSWAGEN','Wake','Walk']
		if marca not in marcas:
			raise forms.ValidationError("""
								Essa marca não e valida, nossa database somente aceita as seguintes marcas:
								Acura,Agrale,Alfo Romeo,Am Gen,Asia motors,ASTON MARTIN,Audi,Baby,BMW,BRM,BUGRE,Cadillac,
                                CBT Jipe,CHANA,CHANGAN,CHERY,Chrysler,Citroën,Cross Lander,Daewoo,Daihatsu,
                                Dodge,EFFA,Engesa,Envemo,Ferrari,Fiat,Fibravan,Ford,FOTON,Fyber,GEELY,GM CHEVROLET,
                                GREAT WALL,Gurgel,HAFEI,HITECH ELECTRIC,HONDA,HYUNDAY,ISUZU,IVECO,JAC,Jaguar,Jeep,JINBEI,JPX,
                                Kia Motors,Lada,Lamborghini,Land Rover,Lexus,LIFAN,LOBINI,Lotus,Mahindra,Maserati,Matra,Mazda,
                                Mclaren,Mercedez Benz,Mercury,MG,MINI,Mitsubishi,Miura,Nissan,Peugeot,Plymouth,Pontiac,Porsche,
                                RAM,RELY,Renault,Rolls-Royce,Rover,Saab,Saturn,Seat,SHINERAY,smart,SSANGYONG,Subaru,Suzuki,
                                TAC,Toyota,Troller,Volvo,VW-VOLKSWAGEN,Wake,Walk""")
		else:
			return marca

	def clean_status(self, *args, **kwargs):
		status= self.cleaned_data.get('status')
		statuses=["Excelente","Bom","Mediano","Ruim","Terrível"]
		if status not in statuses:
			raise forms.ValidationError(f'Os statuses aceitos são: { statuses }')
		else:
			return status

	def clean_cor(self, *args, **kwargs):
		cor= self.cleaned_data.get('cor')
		cores=["Amarelo","Azul","Bege","Branco","Bronze","Cinza","Dourado","Indefinida","Laranja","Marrom","Prata","Preto","Rosa","Roxo","Verde","Vermelho","Vinho"]
		if cor not in cores:
			raise forms.ValidationError(f'''Caso a cor não seja aceita e porque ela é muito atípica. 
                        Ou não é constatada no banco de cores.
                        Favor inserir indefinida no campo nesse caso
                        As cores aceitas são: { Cores }''')
		else:
			return cor

	def clean_localidade(self, *args, **kwargs):
		local= self.cleaned_data.get('localidade')
		locais=["Limeira","Piracicaba"]
		if local not in locais:
			raise forms.ValidationError('Atualmente só trabalhamos com vendas realizadas em Limeira e Piracicaba')
		else:
			return local

	def clean_combustivel(self, *args, **kwargs):
		combustivel= self.cleaned_data.get('combustivel')
		combustiveis=["Amarelo","Azul","Bege","Branco","Bronze","Cinza","Dourado","Indefinida","Laranja","Marrom","Prata","Preto","Rosa","Roxo","Verde","Vermelho","Vinho"]
		if combustivel not in combustiveis:
			raise forms.ValidationError(f'Os combustiveis aceitos são: { combustiveis }')
		else:
			return combustivel


	