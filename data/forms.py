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
		'combustivel': forms.TextInput(attrs={'placeholder':'Combutivél do carro'}),
		'quilometragem': forms.NumberInput(attrs={'placeholder':'Quilometragem do carro'}),
		'preco': forms.NumberInput(attrs={'placeholder':'Preço final do carro na compra ou venda'}),
		'lucro': forms.NumberInput(attrs={'placeholder':'Lucro ou prejuízo pós venda do carro, insira 0 caso seja compra'}),
		}
		fields = ['marca','modelo','ano','status','cor','combustivel','quilometragem','preco','lucro']


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
