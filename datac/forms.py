from django import forms
from .models import DataDBC


class InsiraDadosFormC(forms.ModelForm):
		class Meta:
			model = DataDBC
			fields = ['marca','modelo','motor','ano','status','cor','localidade','combustivel','quilometragem','preco']
			widgets = {
			'marca': forms.TextInput(attrs={'placeholder':'Marca do carro', 'id':'marca'}),
			'modelo': forms.TextInput(attrs={'placeholder':'Modelo do carro de acordo com o renavan','id':'modelo'}),
			'motor': forms.TextInput(attrs={'placeholder':'Motor do carro','id':'motor'}),
			'ano': forms.NumberInput(attrs={'placeholder':'Ano do carro'}),
			'cor': forms.TextInput(attrs={'placeholder':'Cor do carro','id':'cor'}),
			'quilometragem': forms.NumberInput(attrs={'placeholder':'Quilometragem do carro'}),
			'preco': forms.NumberInput(attrs={'placeholder':'Preço final do carro na compra'}),
			}
			labels= {'combustivel':'Combustível',
				     'localidade':'Local da compra'}

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


			def clean_cor(self, *args, **kwargs):
				cor= self.cleaned_data.get('cor')
				cores=['Amarelo','Azul','Bege','Branco','Bronze','Cinza','Dourado','Indefinida','Laranja','Marrom','Prata','Preto','Rosa','Roxo','Verde','Vermelho','Vinho']
				if cor not in cores:
					raise forms.ValidationError(f'''Caso a cor não seja aceita e porque ela é muito atípica. 
		                        Ou não é constatada no banco de cores.
		                        Favor inserir indefinida no campo nesse caso
		                        As cores aceitas são: { cores }''')
				else:
					return cor
